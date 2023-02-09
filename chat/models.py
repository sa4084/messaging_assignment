from django.db import models

# Create your models here.
class Message(models.Model):
    message_id = models.CharField(max_length = 100)
    sender = models.EmailField()
    recipent = models.EmailField()
    title = models.CharField(max_length = 500)
    message = models.CharField(max_length = 1000)



