from django.db import models

# Create your models here.
class List(models.Model):
	name = models.CharField(max_length=264)
	done = models.BooleanField(default=False)

	def __str__(self):
		return self.name + "|" + str(self.done) 

