django-admin startproject DjNearestNeighbour
python manage.py runserver 0.0.0.0:8000
python manage.py startapp dnn
python manage.py makemigrations
python manage.py migrate
python manage.py shell


# Generate an rsa hashed ssh key
ssh-keygen -t rsa

import dnn.tests as t

from dnn.utils.nn import get_nn_str
get_nn_str('2,2;-1,30;20,11;4,5')


curl -d '2,2;-1,30;20,11;4,5' http://127.0.0.1:8000/nn/
curl -s -B -d '2,2;-1,30;20,11;4,5' -H 'Content-type: text/plain' http://127.0.0.1:8000/nn/

