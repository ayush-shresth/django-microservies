from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_first_name = models.CharField(max_length=50)
    user_last_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=50)
    user_phone = models.CharField(max_length=50)
    user_state = models.CharField(max_length=50)
    user_country = models.CharField(max_length=50)
    user_created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user_id) + " "+self.user_first_name+" "+self.user_last_name
