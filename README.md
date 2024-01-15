# DjNearestNeighbour

Create a Django application with an API that receives a set of points on a 
grid as semicolon separated values. And then it finds the points that are closest to each other. 
Store the received set of points and the closest points on a DB.

An example input would look like this: `2,2;-1,30;20,11;4,5`
And then in this case the result would be: `2,2;4,5`

Additionally, please add an admin interface for viewing values stored on the DB. 
And add unit tests where it makes sense.
