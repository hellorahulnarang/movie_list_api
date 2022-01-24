from urllib import request
from rest_framework import serializers
from .models import MovieCollections, Movie

class MovieCollectionSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    uuid = serializers.UUIDField(format='hex_verbose', required=False)
    description = serializers.CharField(required=True, allow_blank=True)
    movies = serializers.ListField(required=False)

    def create(self, validated_data):
        title = validated_data['title']
        description = validated_data['description']

        #creating collection
        collection = MovieCollections.objects.create(title=title, description=description, collection_creator=self.context.get('user'))

        # adding movies in collection
        movie_collection = list()
        for movie in validated_data['movies']:
            movie_collection.append(
                Movie(uuid=movie['uuid'], title=movie['title'], description=movie['description'], genre=movie['genres'], collection_name=collection)
            )
        Movie.objects.bulk_create(movie_collection)

        return collection


    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)

        if len(validated_data['movies']) > 0:
            Movie.objects.filter(collection=instance).delete()
                
            collection_movies=list()
            for movie in validated_data['movies']:
                collection_movies.append(
                    Movie(collection_name=instance, uuid=movie['uuid'], title=movie['title'], description=movie['description'], genres=movie['genres']) 
                )

                Movie.objects.bulk_create(collection_movies)
            # popping validated_data[movies]
            validated_data.pop('movies')
            # PUT for movie collection
            MovieCollections.objects.filter(pk=instance.pk).update(**validated_data)

        return instance


