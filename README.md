# Movie listing
This app fetches list of movies from Third-party API and allowa users to register and create their movie collections.
## Quickstart

To work in a sandbox, use virtual environment(virtualenv).

1. Running app

   ```bash
   1.pip install -r requirements.txt 
   2.python manage.py migrate
   3.python manage.py runserver
   ``` 
 2. Running tests
   
  ```bash
    python manage.py test
  ```
  

## API Documentation 

### `This Endpoint takes username and password and registers and gives the access token` 


1. `POST /register/` 

```json
 application/json - {
    "username": "username:,
    "password": "password",
}
```
##### `response`

```json
{
   "access_token": "access token"
}   
```

    

##### `For all the requests we would use this access token for authentication and permission in headers request`
```json
   Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9
    
```
    

### `This Endpoint gives the list of movies from third party API with pagination support ` 

1. `GET /movies/` 

##### `response`

```json
 application/json - {
 “count”: <total number of movies>,
 “next”: <link for next page, if present>,
 “previous”: <link for previous page>,
 “data”: [
 {
 “title”: <title of the movie>,
 “description”: <a description of the movie>,
 “genres”: <a comma separated list of genres, if
present>,
 “uuid”: <a unique uuid for the movie>
 },
 ...
 ]
}
```

### `This Endpoint takes movie collection and stores them and also returns top 3 genres` 

1. `POST /collection/` 

```json
 application/json - {
 “title”: “<Title of the collection>”,
 “description”: “<Description of the collection>”,
 “movies”: [
 {
 “title”: <title of the movie>,
 “description”: <description of the movie>,
 “genres”: <generes>,
 “uuid”: <uuid>
 }, ...
 ]
}
```
##### `response`

```json
{
 “collection_uuid”: <uuid of the collection item>
}   
```

2. `GET /collection` 

##### `response`

```json
 application/json - {
 “is_success”: True,
 “data”: {
 “collections”: [
 {
 “title”: “<Title of my collection>”,
 “uuid”: “<uuid of the collection name>”
 “description”: “My description of the collection.”
 },
 ...
 ],
 “favourite_genres”: “<My top 3 favorite genres based on the
movies I have added in my collections>.”
 }
}
```


3. `PUT /collection/<collection_uuid>/` 

```json
 application/json - {
 “title”: <Optional updated title>,
 “description”: <Optional updated description>,
 “movies”: <Optional movie list to be updated>,
}
```
##### `response`

```json
{
 “title”: <Title of the collection>,
 “description”: <Description of the collection>,
 “movies”: <Details of movies in my collection>

}
    
```
4. `DELETE /collection/<collection_uuid>/` 


##### `response`

```json
{"message": "Collection deleted successfully!"}
    
```
