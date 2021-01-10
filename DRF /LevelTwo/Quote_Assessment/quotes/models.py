from django.db import models

# Create your models here.
class Quotes(models.Model):

    quote_author = models.CharField(max_length=200)
    quote_body = models.CharField(max_length=200)
    context = models.TextField()
    source = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.quote_author
