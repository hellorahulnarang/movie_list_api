from doctest import debug_script
from pydoc import describe
import uuid
from django.db import models
from user_auth.models import User

class MovieCollections(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default = uuid.uuid4, unique=True, db_index = True)
    title = models.CharField(max_length=200, default='')
    description = models.TextField(default='')
    collection_creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movie_collection_creator')
    date_created_on = models.DateTimeField(auto_now_add=True)
    date_updated_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.uuid.__str__()

class Movie(models.Model):
    uuid = models.CharField(max_length = 250)
    title = models.CharField(max_length=250)
    description = models.TextField()
    genre = models.CharField(max_length=250, db_index=True)
    collection_name = models.ForeignKey(MovieCollections, on_delete=models.CASCADE, related_name='movie_collection_creator',db_index=True)