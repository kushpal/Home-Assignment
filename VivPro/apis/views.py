from rest_framework import generics
from rest_framework.response import Response
from apis.models import SongInfo
from apis.serializers import SongInfoSerializer
from rest_framework.pagination import PageNumberPagination
from VivPro.pagination import CustomPagination
class SongListView(generics.ListAPIView):
    queryset = SongInfo.objects.all()
    pagination_class = CustomPagination
    def get(self, request):
        title = request.query_params.get('title')
        if title:
            self.queryset = self.queryset.filter(title=title)
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(self.queryset, request)
        serializer = SongInfoSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)
    def put(self, request, *args, **kwargs):
        try:
            songinfo = self.queryset.get(song_id=kwargs['song_id'])
            rating = request.data.get('rating')
            songinfo.star_rating = rating
            songinfo.save()
            return Response({"message":"Rated the song successfully"},200)
        except SongInfo.DoesNotExist:
            return Response({'error': 'Song not found'}, status=404)

