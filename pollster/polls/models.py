from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

        
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete =models.CASCADE)        
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


























# Line 12: We connect Choice model to Question model. We set 'question' column in Choice table as foreign key, which takes the ids from Question table.
# "on_delete = models.CASCADE" : If a row is deleted in Question table, delete the corresponding row in Choice table.