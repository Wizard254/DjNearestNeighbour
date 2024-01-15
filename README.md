# DjNearestNeighbour

Create a Django application with an API that receives a set of points on a 
grid as semicolon separated values. And then it finds the points that are closest to each other. 
Store the received set of points and the closest points on a DB.

An example input would look like this: `2,2;-1,30;20,11;4,5`
And then in this case the result would be: `2,2;4,5`

Additionally, please add an admin interface for viewing values stored on the DB. 
And add unit tests where it makes sense.

## Solution

Given a set of points, this solution efficiently calculates the manhattan distance
between a given point and the rest of the points. Any two points with the least 
manhattan distance between them are recorded as the closest to each other.

## Endpoints

1. `/nn/`: 

- Receives a set of points on a grid as semicolon separated values, from a `POST` request
with `utf-8` encoded text, and finds the points that are closest to each other; 
returns the points also in plain text. 
- On `GET` request, displays an interface to easily interact with the API

2. `/admin/dnn/nnmodel`: Provides an admin interface for viewing values stored on the DB.
