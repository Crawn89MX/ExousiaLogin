from django.db import models
from user.models import User

class Score(models.Model):
    id = models.AutoField(primary_key=True)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.BigIntegerField()
    karma = models.IntegerField()
    timePlayed = models.BigIntegerField()
    deaths = models.IntegerField()
    attempt = models.IntegerField()
    decisions = models.TextField()
    updateAt = models.DateTimeField(auto_now=True, null=True)
    createdAt = models.DateTimeField(auto_now=True, null=True)