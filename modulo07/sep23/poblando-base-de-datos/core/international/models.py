from django.db import models

class Countries(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(primary_key=True, max_length=2)

    class Meta:
        managed = False
        db_table = 'countries'

class CodesAll(models.Model):
    id = models.AutoField(primary_key=True)
    entity = models.CharField(db_column='Entity')  # Field name made lowercase.
    currency = models.CharField(db_column='Currency')  # Field name made lowercase.
    alphabeticcode = models.CharField(db_column='AlphabeticCode', blank=True, null=True)  # Field name made lowercase.
    numericcode = models.DecimalField(db_column='NumericCode', blank=True, null=True)  # Field name made lowercase.
    minorunit = models.CharField(db_column='MinorUnit', blank=True, null=True)  # Field name made lowercase.
    withdrawaldate = models.CharField(db_column='WithdrawalDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'codes-all'