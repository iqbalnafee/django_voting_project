from django.db import models

# Create your models here.

# create model question


class Question(models.Model):
    # id will be auto incremented
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published')

    # without def it will shoe whole Question object in the frontend
    def __str__(self):
        return self.question_text


class choice(models.Model):  # choice means option
    # link choice model to question we will use foreign key

    # on_delete=models.CASCADE means when a question is deleted all of its choice will be deletd from choice model
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # without def it will shoe whole Question object in the frontend
    def __str__(self):
        return self.choice_text
