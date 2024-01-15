from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dnn.utils.nn import get_nn_str
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import parser_classes
from dnn.rest_framework.parsers import PlainTextParser


# @api_view(['GET', 'POST'])
@api_view(['POST'])
@parser_classes([PlainTextParser])
@csrf_exempt
def nn(request, format=None):
    """
    An API that receives a set of points on a
    grid as semicolon separated values. And then it finds the points that are closest to each other.
    Store the received set of points and the closest points on a DB
    """
    if request.method == 'GET':
        # shouldn't end up here yet
        assert False
        pass

    elif request.method == 'POST':
        # We registered a plain text parser for this view, the data should be some string
        s: str = request.data
        ok, least, err = get_nn_str(s)

        if not ok:
            # Couldn't get the nearest neighbor, bad resuest format
            return Response({'detail': err}, status=status.HTTP_400_BAD_REQUEST)
            pass

        return Response(least)
        pass
