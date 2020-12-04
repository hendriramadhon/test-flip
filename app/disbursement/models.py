from django.db import models

# Create your models here.
class Disbursement(models.Model):
    result_id = models.IntegerField(blank=True, null=True)
    bank_code = models.CharField(max_length=500,null=True, blank=True)
    account_number = models.CharField(max_length=500,null=True, blank=True)
    amount = models.DecimalField(max_digits=25, decimal_places=2)
    receipt = models.CharField(max_length=500,null=True, blank=True)
    time_served = models.DateTimeField(null=True, blank=True)
    remark = models.CharField(max_length=500,null=True, blank=True)
    status = models.CharField(max_length=500,null=True, blank=True)
