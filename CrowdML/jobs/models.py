from django.db import models

class Job(models.Model):
    user = models.ForeignKey(User)

class Item(models.Model):
    url = models.Charfield(max_length = 200)
    label = models.Charfield(max_length = 200)
    job = models.ForeignKey(Job)

class Score(models.Model):
    value = models.Integerfield()
    item = models.ForeignKey(Item)
