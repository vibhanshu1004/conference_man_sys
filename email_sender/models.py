# from django.db import models

from django.db import models

class Email(models.Model):
    recipient_email = models.EmailField()
