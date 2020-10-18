from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet

from profiles_api import serializers


class HelloApiView(APIView):
    """TEST API VIEW."""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list"""

        data = ["one", "two", "three", "four", "five", "six", "seven"]

        return Response({"message": "Hello!", "data": data})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"

            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        return Response({"method": "delete"})


class HelloViewSet(ViewSet):
    def list(self, request):
        a_list = ["one", "two", "three", "four", "five", "six"]

        return Response({"message": "Hello", "a_viewset": a_list})

    def create_user(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"

            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response({"method": "this is a GET"})

    def update(self, request, pk=None):
        return Response({"method": "this is a PUT"})

    def partial_update(self, request, pk=None):
        return Response({"method": "this is a PATCH"})

    def destroy(self, request, pk=None):
        return Response({"method": "this is a DELETE"})
