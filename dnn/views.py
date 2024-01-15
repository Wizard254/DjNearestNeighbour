from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dnn.utils.nn import get_nn_str
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import parser_classes
from dnn.rest_framework.parsers import PlainTextParser
from dnn.models import NNModel


@api_view(['GET', 'POST'])
@parser_classes([PlainTextParser])
@csrf_exempt
def nn(request, format=None):
    """
    An API that receives a set of points on a
    grid as semicolon separated values. And then it finds the points that are closest to each other.
    Store the received set of points and the closest points on a DB
    """
    # if request.method == 'GET':
    #     # shouldn't end up here yet
    #     assert False
    #     pass

    if request.method == 'POST':
        # We registered a plain text parser for this view, the data should be some string
        s: str = request.data

        # Check if result is cached in the database
        prec = NNModel.objects.filter(coords=s).first()
        if prec is not None:
            return Response(prec.nn)

        ok, nn, err = get_nn_str(s)
        if not ok:
            # Couldn't get the nearest neighbor, bad resuest format
            return Response({'detail': err}, status=status.HTTP_400_BAD_REQUEST)
            pass

        m = NNModel()
        m.coords = s
        m.nn = nn

        m.asave()

        return Response(nn)
        pass
