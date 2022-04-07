from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Chapter, Series
from .serializers import ChapterSerializer
import requests
# Create your views here.

#functon to get all chapter's data
@api_view(['GET'])
def content(request, user_id, series_id):
    try:
        url ='http://127.0.0.1:8002/api/daily_pass/chapter_detail/%s/%s/' % (user_id, series_id)
        r = requests.get(url)
        unlock_chapter = r.json()
        chapter_text = Chapter.objects.filter( series_id=series_id).order_by('chapter_id')[:unlock_chapter]
        chapter_text = ChapterSerializer(chapter_text, many=True)
        return Response(chapter_text.data, status=200)
    except Chapter.DoesNotExist:
        return Response({'message':'User or Seires does not exist'}, status=400)
    
    
#function to get the no of series with respecrtive user_id and it will update the relation talbe in daily_pass
@api_view(['POST'])
def update(request):
    obj=list(Series.objects.values('series_id'))
    l=obj[len(obj)-1]['series_id']
    # l=[i['series_id'] for i in obj]
    if request.method == 'POST':
        s=request.POST.dict()
        s['series_id']=l
        url='http://127.0.0.1:8002/api/daily_pass/update/'
        r=requests.post(url,s) 
        return Response(status=202)
    return Response(status=400)    

#function is used to bulk load data in database
@api_view(['POST'])
def load(request):
    if request.method == 'POST':
        data=request.data
        for key1, val1 in data.items():
            sdes=val1['description']
            chapter=val1['chapter']
            series=Series.objects.create(name=key1, description=sdes)
            series.save()
            series_id=series.series_id
            url='http://127.0.0.1:8000/api/user/update/'
            r=requests.post(url,data={'series_id':series_id})
            for key2, val2 in chapter.items():
                cdes=val2['description']
                name=val2['name']
                text=val2['text']
                chapter=Chapter.objects.create(name=name, description=cdes, text=text, series_id=series_id)
                chapter.save()
        return Response(status=202)
    return Response(status=400)
      