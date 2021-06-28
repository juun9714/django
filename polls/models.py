from mysite.settings import TIME_ZONE
from django.db import models
import datetime

class Question(models.Model):
    #two field
    #장고의 model은 내부적으로 SQL을 사용하여 id field를 생성한다. 
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
        #table의 각 record의 제목이 될 값 반환

    def was_published_recently(self):
        return self.pub_date >= TIME_ZONE.now() 


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)#foreign key, cascade
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text