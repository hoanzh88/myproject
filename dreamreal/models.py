from django.db import models

# Create your models here.
class Dreamreal(models.Model):
   website = models.CharField(max_length = 50)
   mail = models.CharField(max_length = 50)
   name = models.CharField(max_length = 50)
   mydata = models.JSONField('data', null=True, blank=True, editable=False)
   phonenumber = models.IntegerField()

   class Meta:
      db_table = "dreamreal"