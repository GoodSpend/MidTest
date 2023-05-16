from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    publish_date = models.DateField()

    def __str__(self):
        return self.title
