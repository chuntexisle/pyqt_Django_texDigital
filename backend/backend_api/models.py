from django.db import models

# Create your models here.

class TexileAppTestqt(models.Model):
    tds_transaction_id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    customer = models.CharField(max_length=45, blank=True, null=True)
    gt_pipo_po = models.IntegerField(blank=True, null=True)
    processing_order = models.IntegerField(blank=True, null=True)
    wonumber = models.CharField(max_length=45, blank=True, null=True)
    od = models.FloatField(blank=True, null=True)
    wall = models.FloatField(blank=True, null=True)
    weight_per_ft = models.FloatField(blank=True, null=True)
    grade = models.CharField(max_length=45, blank=True, null=True)
    design = models.CharField(max_length=45, blank=True, null=True)
    manufacturer = models.CharField(max_length=45, blank=True, null=True)
    avg_length = models.FloatField(blank=True, null=True)
    totalqty_uv_coated = models.IntegerField(blank=True, null=True)
    totalqty_nouv_coating = models.IntegerField(blank=True, null=True)
    totalfeet = models.FloatField(blank=True, null=True)
    totaltons = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'texile_app_testqt'

class TexileAppReleasedLots(models.Model):
    lot_number = models.IntegerField(primary_key=True)
    qty_uv_coated = models.IntegerField(blank=True, null=True)
    qty_nouv_coating = models.IntegerField(blank=True, null=True)
    feet = models.FloatField(blank=True, null=True)
    tons = models.FloatField(blank=True, null=True)
    tds_transaction_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'texile_app_released_lots'
