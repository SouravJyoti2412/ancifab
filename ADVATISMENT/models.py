from django.db import models
class product_add_slot(models.Model):
    PRODUCT_ADD_SLOT_274X366px = models.FileField(upload_to='advatisment_img/',)
    PRODUCT_ADD_lINK = models.CharField(max_length = 255)


