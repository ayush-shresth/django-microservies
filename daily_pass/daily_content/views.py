from .models import Relation
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

# function to unlock the chapter for the given user and series
@api_view(['GET'])
def unlock_chapter(request, user_id, series_id):
    try:
        user = Relation.objects.get(user_id=user_id, series_id=series_id)
        user.unlock_chapter = user.unlock_chapter+1
        user.save()
        return Response({'message': 'Chapter Successfully unlocked', 'user': user.unlock_chapter}, status=200)
    except Relation.DoesNotExist:
        return Response({'message': 'User or Seires does not exist'}, status=400)

# function it will receive user_id and series_id and it will update the relation talbe in daily_pass
# it is used to update the relation table on load of series and chapter
@api_view(['POST'])
def user_update(request):
    if request.method == 'POST':
        s = request.POST.dict()
        user_id = int(s['user_id'])
        series_id = int(s['series_id'])
        for i in range(series_id):
            user = Relation.objects.create(
                user_id=user_id, series_id=i+1, unlock_chapter=4)
            user.save()
        return Response(status=201)
    return Response(status=400)

# function to get total no of unlock chapter for the given user and series
@api_view(['GET'])
def chapter_detail(request, user_id, series_id):
    try:
        user = Relation.objects.get(user_id=user_id, series_id=series_id)
        return Response(user.unlock_chapter, status=200)
    except Relation.DoesNotExist:
        return Response({'message': 'User or Seires does not exist'}, status=400)

# function to update the relation table on new user creations
@api_view(['POST'])
def user_update1(request):
    if request.method == 'POST':
        s = request.data
        user_id = int(s['user_id'])
        series_id = int(s['series'])
        for i in range(user_id):
            user = Relation.objects.create(
                user_id=i+1, series_id=series_id, unlock_chapter=4)
            user.save()

        return Response(status=201)
    return Response(status=400)
