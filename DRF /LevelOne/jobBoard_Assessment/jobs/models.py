from django.db import models

# Create your models here.
class jobOffer(models.Model):

    company_name = models.CharField(max_length=60)
    company_email = models.EmailField(max_length=60)
    job_title = models.CharField(max_length=60)
    job_description = models.TextField()
    salary = models.FloatField()
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now=True)
    available= models.BooleanField(default=True)

    def __str__(self):

        return self.job_title
