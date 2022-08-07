from statistics import mode
from django.db import models

# Create your models here.

class User(models.Model):
    f_name = models.CharField("FirstName", max_length=240)
    m_name = models.CharField("MiddleName", max_length=240)
    l_name = models.CharField("LastName", max_length=240)
    email = models.EmailField("Email", max_length=240)
    username = models.CharField("Username", max_length=240)
    password = models.CharField("Password", max_length=240)
    c_password = models.CharField("ConfirmPassword", max_length=240)
    registrationDate = models.DateField("Registration Date", auto_now_add=True)

