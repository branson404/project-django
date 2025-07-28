from django.db import models

class UserAccounts(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # store hashed passwords ideally

    def __str__(self):
        return self.username
