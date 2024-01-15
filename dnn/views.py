from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer, BrowsableAPIRenderer, JSONRenderer
from rest_framework.response import Response
from dnn.utils.nn import get_nn_str
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import parser_classes, renderer_classes
from dnn.rest_framework.parsers import PlainTextParser
from dnn.rest_framework.renderers import PlainTextRenderer
from dnn.models import NNModel

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


class GetNearestNeighbour(APIView):
    """
    API View that receives a set of points on a grid as semicolon separated values.
    And then it finds the points that are closest to each other.
    Stores the received set of points and the closest points on a DB.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    parser_classes = [PlainTextParser]
    renderer_classes = [BrowsableAPIRenderer, PlainTextRenderer, JSONRenderer]

    def get(self, request, format=None):
        """
        Allow display of the default browsable API
        """
        return Response('')

    def post(self, request, format=None):
        """
        Given POST request data of a set of points on a grid as semicolon separated values,
        finds the points that are closest to each other, as response
        """
        # We registered a plain text parser for this view, the data should be some string
        s: str = request.data

        # Check if result is cached in the database
        prec = NNModel.objects.filter(coords=s).first()
        if prec is not None:
            # return Response(prec.nn, content_type='text/plain')
            return Response(prec.nn)

        ok, nn, err = get_nn_str(s)
        if not ok:
            # Couldn't get the nearest neighbor, bad resuest format
            return Response({'detail': err},
                            status=status.HTTP_400_BAD_REQUEST,
                            content_type='application/json')
            pass

        m = NNModel()
        m.coords = s
        m.nn = nn

        m.save()

        # return Response(nn, content_type='text/plain')
        return Response(nn)
