from django.db import models

class Interview(models.Model):
    company_name = models.CharField(max_length=100)
    date = models.DateTimeField()
    stage = models.IntegerField(null=True)
    method = models.TextField()
    verdict = models.CharField(max_length=100)
