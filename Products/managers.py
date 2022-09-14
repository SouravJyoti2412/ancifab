from django.db import models

class main_categoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(parent=None)
    
class categoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(parent=None)
class sub_categoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(parent=categoryManager)