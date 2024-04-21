from django.db import models

class Question(models.Model):
    question_text = models.TextField(null=True)
    answer_text = models.TextField(null=True)

    def __str__(self):
        return self.question_text

