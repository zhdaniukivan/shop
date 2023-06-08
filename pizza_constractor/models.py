from django.conf import settings
from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=4000)
    visible = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=4000)
    points = models.FloatField()
    locK_other = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choice = models.ForeignKey(Choice, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.choice.title

