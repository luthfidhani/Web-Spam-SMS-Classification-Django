from django.db import models

class Data(models.Model):
    text = models.TextField(max_length=500)
    prediction = models.TextField(max_length=10)
    created_at = models.DateTimeField()

    # def __str__(self):
    #     return '%s: %s: %s' % (self.text, self.prediction, self.created_at)

