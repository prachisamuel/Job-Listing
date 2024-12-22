from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  # Import this
from .models import Job
from .serializers import JobSerializer
from rest_framework.decorators import api_view

@api_view(['POST'])
def add_job(request):
    if request.method == 'POST':
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Job added successfully'}, status=201)
        return Response(serializer.errors, status=400)

class JobListView(APIView):
    def get(self, request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)  # Debugging received data
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
