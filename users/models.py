from django.db   import models

from core.models import TimeStamp

class User(TimeStamp):
    name              = models.CharField(max_length=100)
    kakao_id          = models.CharField(max_length=200)
    email             = models.EmailField(max_length=100, unique=True)
    password          = models.CharField(max_length=200, null=True)
    mobile_number     = models.CharField(max_length=100, null=True)
    college           = models.CharField(max_length=100, null=True)
    introduction      = models.CharField(max_length=1000, null=True)
    company_name      = models.CharField(max_length=100, null=True)
    duty              = models.CharField(max_length=100, null=True)
    salary            = models.DecimalField(max_digits=15, decimal_places=3, null=True)
    date_of_joining   = models.DateField(null=True)
    date_of_resigning = models.DateField(null=True)
    in_office         = models.BooleanField(null=True)

    class Meta:
        db_table = 'users'