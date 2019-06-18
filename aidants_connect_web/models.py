from datetime import timedelta
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

CONNECTION_EXPIRATION_TIME = 10


def default_expiration_date():
    now = timezone.now()
    return now + timedelta(minutes=CONNECTION_EXPIRATION_TIME)


class Connection(models.Model):
    state = models.TextField()
    code = models.TextField()
    nonce = models.TextField(default="No Nonce Provided")
    expiresOn = models.DateTimeField(default=default_expiration_date)
    sub_usager = models.TextField(default="No sub Provided")
    access_token = models.TextField(default="No token Provided")
    redirectUrl = models.CharField(max_length=100)


class User(AbstractUser):
    pass


class Usager(models.Model):
    given_name = models.TextField(blank=False)
    family_name = models.TextField(blank=False)
    preferred_username = models.TextField(blank=True)
    birthdate = models.DateField(blank=False)
    GENDER = (("F", "Femme"), ("H", "Homme"))
    gender = models.CharField(max_length=1, choices=GENDER, default="F", blank=False)
    birthplace = models.PositiveIntegerField(
        validators=[MinValueValidator(9999), MaxValueValidator(100000)], blank=False
    )
    birthcountry = models.IntegerField(
        validators=[MinValueValidator(99100), MaxValueValidator(99500)],
        default=99100,
        blank=False,
    )
    sub = models.TextField(default="No Sub yet")
    email = models.EmailField(blank=False)

    def __str__(self):
        return self.given_name + " " + self.family_name


class Demarche(models.Model):
    class Meta:
        ordering = ["-weight"]

    title = models.CharField(max_length=100, blank=False)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Mandat(models.Model):
    aidant = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    usager = models.ForeignKey(Usager, on_delete=models.CASCADE, default=0)
    perimeter = models.ForeignKey(Demarche, on_delete=models.CASCADE, default=0)
    creation_date = models.DateTimeField(default=timezone.now)
    perimeter_other = models.TextField(blank=True)
    personal_data = models.BooleanField(default=False)
    brief = models.BooleanField(default=False)
