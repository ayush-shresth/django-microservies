from django.db import models

# Create your models here.
class Relation(models.Model):
    user_id = models.IntegerField()
    series_id = models.IntegerField()
    unlock_chapter = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'User_Id {self.user_id}, Series_Id {self.series_id}, Chapter_Unlock {self.unlock_chapter}'