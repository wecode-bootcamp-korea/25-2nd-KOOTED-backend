from django.db        import models

from core.models      import TimeStamp
from users.models     import User
from companies.models import Company, Job

class Post(TimeStamp):
    title              = models.CharField(max_length=100)
    working_year       = models.IntegerField()
    recommender_reward = models.DecimalField(max_digits=10, decimal_places=3)
    applicant_reward   = models.DecimalField(max_digits=10, decimal_places=3)
    content            = models.TextField(max_length=5000)
    deadline           = models.DateField(null=True)
    job                = models.ForeignKey(Job, on_delete=models.CASCADE)
    company            = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        db_table = 'posts'

class PostImage(models.Model):
    image_url = models.CharField(max_length=2000)
    post      = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        db_table = 'post_images'

class Bookmark(models.Model):
    post  = models.ForeignKey(Post, on_delete=models.CASCADE)
    user  = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'bookmarks'

class WorkingYear(models.Model):
    years = models.IntegerField()

    class Meta:
        db_table = 'working_years'

class UserWorkingYear(models.Model):
    working_year = models.ForeignKey(WorkingYear, on_delete=models.CASCADE)
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    job          = models.ForeignKey(Job, on_delete=models.CASCADE)

    class Meta:
        db_table = 'users_working_years'