from django.test import TestCase
from rest_framework.test import APIRequestFactory

# Create your tests here.

# Test the /nn/ endpoint
factory = APIRequestFactory()
request = factory.post('/nn/', '2,2;-1,30;20,11;4,5')
print(request.body)
