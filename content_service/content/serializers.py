from rest_framework import serializers
from .models import Chapter, Series


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('chapter_id', 'name', 'description', 'text', 'series_id')


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ('series_id', 'series_name', 'series_text')
