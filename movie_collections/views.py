from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from movie_collections.utils.get_movie_list import get_movie_list
from .serializers import MovieCollectionSerializer
from .models import MovieCollections,Movie
from django.db.models import Count
from rest_framework.generics import ListCreateAPIView
from user_auth.permissions import OwnerOrAdmin

class ThirdPartyMovie(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        page_number = request.query_params.get('page')
        response = get_movie_list(page_number)
        return response

class MovieColletionAPI(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request, *args, **kwargs):
        print(request.user)
        serializer = MovieCollectionSerializer(data = request.data, context ={'user':request.user})

        if serializer.is_valid():
            print(serializer.validated_data)
            collection = serializer.create(validated_data = serializer.validated_data)
            return Response({
                    "collection_uuid": collection.uuid
                })

        # serializer validation errors
        return Response({
                "error": serializer.errors
            })


    def get(self,request):
      
        queryset = MovieCollections.objects.filter(collection_creator =request.user)
        serializer = MovieCollectionSerializer(queryset, many=True)

        genres = Movie.objects.values('genre').annotate(genre_count=Count('genre')).order_by('-genre_count')
        print(genres)
        genres = genres[0:3]
        print(genres)

        for value in genres:
            value.pop('genre_count')

        return Response({
                "is_success": True,            
                "data": {
                    "collections": serializer.data,
                    "favourite_genres": genres,
                }
        })

class MovieListOperation(APIView):
    permission_classes = [IsAuthenticated, OwnerOrAdmin]
    authentication_classes = [JWTAuthentication]
    # serializer_class = MovieCollectionSerializer

    def get_queryset(self):
        return MovieCollections.objects.get(pk=self.kwargs['uuid'])

    def get(self, request, *args, **kwargs):
        """method for get request for  movie collection"""
        try:
            self.check_object_permissions(self.request, self.get_queryset())
            instance=self.get_queryset()
            serializer = MovieCollectionSerializer(instance)
            return Response({
                'collections': serializer.data
            })
        except MovieCollections.DoesNotExist:
            return Response({
                'error': 'Invalid UUID'
            })


    def put(self,request, *args, **kwargs):
        try:
            self.check_object_permissions(self.request, self.get_queryset())
            serializer = MovieCollectionSerializer(instance=self.get_queryset(), data=request.data, partial=True)
            if serializer.is_valid():
                collection = serializer.update(validated_data = serializer.validated_data)
                return Response({
                    'collection_uuid': collection.uuid
                })
            return Response({
                'error': serializer.errors
            })

        except MovieCollections.DoesNotExist:
            return Response({
                'error': 'Collection with given UUID does not exist'
            })

    def delete(self, request, *args, **kwargs):
        try:

            self.check_object_permissions(self.request, self.get_queryset())
            instance= self.get_queryset()
            instance.delete()
            return Response({
                'message': 'movie collection deleted successfully.'
            })
        except MovieCollections.DoesNotExist:
            return Response({
                'error': 'This UUID movie does not exist'
            })