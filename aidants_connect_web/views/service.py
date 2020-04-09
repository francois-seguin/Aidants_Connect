from datetime import timedelta
import logging

from django.conf import settings
from django.contrib import messages as django_messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.utils import timezone
from django.utils.http import url_has_allowed_host_and_scheme

from aidants_connect_web.forms import OTPForm
from aidants_connect_web.models import Organisation, Aidant, Usager, Mandat, Journal


logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


def humanize_demarche_names(name: str) -> str:
    """
    >>> humanize_demarche_names('argent')
    "ARGENT: Crédit immobilier, Impôts, Consommation, Livret A, Assurance, "
            "Surendettement…"
    :param machine_names:
    :return: list of human names and description
    """
    demarches = settings.DEMARCHES
    return f"{demarches[name]['titre'].upper()}: {demarches[name]['description']}"


def home_page(request):
    return render(request, "aidants_connect_web/home_page.html",)


@login_required
def logout_page(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)


@login_required
def dashboard(request):
    aidant = request.user
    messages = django_messages.get_messages(request)
    return render(
        request,
        "aidants_connect_web/dashboard.html",
        {"aidant": aidant, "messages": messages},
    )


def guide_utilisation(request):
    return render(request, "aidants_connect_web/guide_utilisation.html")


def statistiques(request):
    # Indicateurs de base
    organisation_total = Organisation.objects.count()
    aidant_total = Aidant.objects.count()
    usager_total = Usager.objects.count()
    # Usagers
    active_usager_total = Usager.objects.active().count()
    # Mandats
    mandat_total = Mandat.objects.count()
    active_mandat_total = Mandat.objects.active().count()
    mandat_used_last_30_days = (
        Journal.objects.filter(action="create_mandat")
        .filter(creation_date__gt=timezone.now() - timedelta(days=30))
        .distinct("mandat")
        .count()
    )
    # Démarches
    demarches_aggregation = []
    for demarche in settings.DEMARCHES.keys():
        demarches_aggregation.append(
            {
                "title": demarche,
                "icon": settings.DEMARCHES[demarche]["icon"],
                "value": Mandat.objects.for_demarche(demarche).count(),
            }
        )
    demarches_aggregation.sort(key=lambda x: x["value"], reverse=True)

    return render(
        request,
        "footer/statistiques.html",
        {
            "statistiques_list": [
                {
                    "name": "Indicateurs de base",
                    "values": [
                        {"title": "Organisations", "value": organisation_total},
                        {"title": "Aidants", "value": aidant_total},
                        {"title": "Usagers", "value": usager_total},
                    ],
                },
                {
                    "name": "Usagers",
                    "values": [
                        {"title": "Total", "value": usager_total},
                        {
                            "title": "Actifs",
                            "subtitle": "Usagers avec au moins 1 mandat actif",
                            "value": active_usager_total,
                        },
                    ],
                },
                {
                    "name": "Mandats",
                    "values": [
                        {"title": "Total", "value": mandat_total},
                        {"title": "Actifs", "value": active_mandat_total},
                        {
                            "title": "Utilisés récemment",
                            "subtitle": "30 derniers jours",
                            "value": mandat_used_last_30_days,
                        },
                    ],
                },
            ],
            "statistiques_demarches": demarches_aggregation,
        },
    )


@login_required()
def activity_check(request):
    next_page = request.GET.get("next", settings.LOGIN_REDIRECT_URL)

    if not url_has_allowed_host_and_scheme(
        next_page, allowed_hosts={request.get_host()}, require_https=True
    ):
        log.warning(
            "[Aidants Connect] an unsafe URL was used through the activity check"
        )
        return HttpResponseNotFound()

    aidant = request.user
    if request.method == "POST":
        form = OTPForm(aidant=aidant, data=request.POST)

        if form.is_valid():
            Journal.objects.activity_check(aidant)
            return redirect(next_page)
    else:
        form = OTPForm(request.user)

    return render(
        request, "registration/activity_check.html", {"form": form, "aidant": aidant}
    )


def cgu(request):
    return render(request, "footer/cgu.html")


def mentions_legales(request):
    return render(request, "footer/mentions_legales.html")


def ressources(request):
    return render(request, "aidants_connect_web/ressource_page.html")


def about(request):
    return render(request, "aidants_connect_web/about_page.html")
