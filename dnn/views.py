from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
from dnn.utils.nn import get_nn_str


# @api_view(['GET', 'POST'])
@api_view(['POST'])
def nn(request):
    """
    An API that receives a set of points on a
    grid as semicolon separated values. And then it finds the points that are closest to each other.
    Store the received set of points and the closest points on a DB
    """
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        s = request.data
        ok, least, err = get_nn_str(s)
        if not ok:
            return Response({'detail': err}, status=status.HTTP_400_BAD_REQUEST)
            pass

        if len(least) == 1:
            d = least[0]
            pass
        else:
            d = least
            pass

        return Response(d)
        pass

#
# @api_view(['GET', 'POST'])
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
