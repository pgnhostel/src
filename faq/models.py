from django.db import models


class Faq(models.Model):
    question = models.CharField(max_length=150)
    answer = models.TextField(max_length=500)

    def __str__(self):
        return self.question

