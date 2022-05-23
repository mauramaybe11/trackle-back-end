from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.log import Log
from ..serializers import LogSerializer

# Create your views here.
class Logs(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = LogSerializer
    def get(self, request):
        """Index request"""
        # Get all the logs:
        # logs = Log.objects.all()
        # Filter the logs by owner, so you can only see your owned logs
        logs = Log.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = LogSerializer(logs, many=True).data
        return Response({ 'logs': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['log']['owner'] = request.user.id
        # Serialize/create log
        log = LogSerializer(data=request.data['log'])
        # If the log data is valid according to our serializer...
        if log.is_valid():
            # Save the created log & send a response
            log.save()
            return Response({ 'log': log.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(log.errors, status=status.HTTP_400_BAD_REQUEST)

# attempt at index for all
class LogAll(generics.ListAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = LogSerializer
    def get(self, request):
        """Index request"""
        # Get all the logs:
        # logs = Log.objects.all()
        # Filter the logs by owner, so you can only see your owned logs
        logs = Log.objects.all()
        # Run the data through the serializer
        data = LogSerializer(logs, many=True).data
        return Response({ 'logs': data })

class LogDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the log to show
        log = get_object_or_404(Log, pk=pk)
        # Only want to show owned logs?
        if request.user != log.owner:
            raise PermissionDenied('Unauthorized, you do not own this log')

        # Run the data through the serializer so it's formatted
        data = LogSerializer(log).data
        return Response({ 'log': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate log to delete
        log = get_object_or_404(Log, pk=pk)
        # Check the log's owner against the user making this request
        if request.user != log.owner:
            raise PermissionDenied('Unauthorized, you do not own this log')
        # Only delete if the user owns the  log
        log.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Log
        # get_object_or_404 returns a object representation of our Log
        log = get_object_or_404(Log, pk=pk)
        # Check the log's owner against the user making this request
        if request.user != log.owner:
            raise PermissionDenied('Unauthorized, you do not own this log')

        # Ensure the owner field is set to the current user's ID
        request.data['log']['owner'] = request.user.id
        # Validate updates with serializer
        data = LogSerializer(log, data=request.data['log'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
