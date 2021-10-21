from django.db    import models

from users.models import User

class JobGroup(models.Model):
    name      = models.CharField(max_length=100)
    image_url = models.CharField(max_length=2000)
    
    class Meta:
        db_table = 'job_groups'

class Job(models.Model):
    name      = models.CharField(max_length=100)
    image_url = models.CharField(max_length=2000)
    job_group = models.ForeignKey(JobGroup, on_delete=models.CASCADE)

    class Meta:
        db_table = 'jobs'

class Company(models.Model):
    name            = models.CharField(max_length=100)
    location        = models.TextField(max_length=5000)
    salary          = models.DecimalField(max_digits=15, decimal_places=3)
    employee_number = models.IntegerField()
    description     = models.CharField(max_length=2000)

    class Meta:
        db_table = 'companies'

class CompanyImage(models.Model):
    image_url = models.CharField(max_length=2000)
    company   = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        db_table = 'company_images'

class Tag(models.Model):
    name  = models.CharField(max_length=100)
    color = models.CharField(max_length=45)
    
    class Meta:
        db_table = 'tags'

class CompanyTag(models.Model):
    tag     = models.ForeignKey(Tag, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        db_table = 'companies_tags'