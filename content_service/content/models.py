from django.db import models

# Create your models here.


class Series(models.Model):
    series_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.series_id) + " " + self.name

class Chapter(models.Model):
    chapter_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE ,default=1,related_name='chapters')

    def __str__(self):
        return str(self.chapter_id) + " " + self.name+ " (" + self.series.name + ")"