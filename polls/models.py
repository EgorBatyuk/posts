from django.db import models
from django.conf import settings
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.question_text


