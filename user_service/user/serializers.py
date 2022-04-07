from rest_framework import serializers
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id','user_first_name','user_last_name','user_email','user_phone','user_state','user_country','user_created_date')
