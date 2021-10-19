from django.db    import models

from core.models  import TimeStamp
from users.models import User
from posts.models import Post

class Resume(TimeStamp):
    introduction     = models.CharField(max_length=1000, null=True)
    college          = models.CharField(max_length=100, null=True)
    resume_file_url  = models.CharField(max_length=2000, null=True)
    user             = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'resumes'

class Application(TimeStamp):
    recommender = models.CharField(max_length=100)
    resume      = models.ForeignKey(Resume, on_delete=models.SET_NULL, null=True)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    post        = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        db_table = 'applications'

class Career(models.Model):
    company_name      = models.CharField(max_length=100)
    duty              = models.CharField(max_length=100)
    date_of_joining   = models.DateField()
    date_of_resigning = models.DateField(null=True)
    in_office         = models.BooleanField()
    resume            = models.ForeignKey(Resume, on_delete=models.CASCADE)

    class Meta:
        db_table = 'careers'

class Skill(models.Model):
    name   = models.CharField(max_length=100)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    user   = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'skills'