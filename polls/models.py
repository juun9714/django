from mysite.settings import TIME_ZONE
from django.db import models
import datetime

class Question(models.Model):
    #two field
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= TIME_ZONE.now() 


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)#foreign key, cascade
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text