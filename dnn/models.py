from django.db import models


# Create your models here.

class NNModel(models.Model):
    # A database index will be created for this field
    coords = models.CharField(db_index=True, unique=True, max_length=500)
    nn = models.CharField(max_length=500)
    modified = models.DateTimeField(auto_now=True)
    pass
