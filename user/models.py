from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime

class User(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.TextField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    token = models.CharField(max_length=100)
    updateAt = models.DateTimeField(auto_now=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True, null=True)

    def set_password(self, raw_password):
        if raw_password == "" or raw_password == self.password:
            return
        self.password = make_password(raw_password)

    def set_token(self, raw_token):
        if raw_token == "" or raw_token == self.token:
            return
        self.token = make_password(raw_token + str(datetime.now))