from django.db import models
from django.utils.text import slugify
# Create your models here.

class BlogPost(models.Model):
	title = models.CharField(max_length=255)
	content	= models.TextField()
	date = models.DateTimeField(auto_now=True)
	slug = models.SlugField(blank=True, editable=False)

	def save(self):
		self.slug = slugify(self.title)
		super().save()

	def __str__(self):
		return "{}.{}".format(self.id, self.title)