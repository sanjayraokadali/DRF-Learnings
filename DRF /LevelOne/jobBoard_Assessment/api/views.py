from django.shortcuts import render
from rest_framework.response import Response
from jobs.models import jobOffer
from rest_framework.views import APIView
from api.serializers import JobSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import status

# Create your views here.
class JobListAPI(APIView):

    def get(self,request):

        jobs = jobOffer.objects.all()

        serializer = JobSerializer(jobs, many=True)

        return Response({

            'Job List': serializer.data
        })

    def post(self,request):

        serializer = JobSerializer(data = request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({
                'status': 'job created!',
                'job':serializer.data
            })
        return Response(serializer.errors)

class JobDetailAPI(APIView):

    def get_object(self,pk):

        job = get_object_or_404(jobOffer,pk=pk)

        return job

    def get(self,request,pk):

        job = self.get_object(pk)

        serializer = JobSerializer(job)

        return Response({
        'job': serializer.data
        })

    def put(self,request, pk):

        job = self.get_object(pk)

        serializer = JobSerializer(job, data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({
                'status': 'job updated!',
                'job':serializer.data
            })
        return Response(serializer.errors)

    def delete(self,request,pk):

        job = self.get_object(pk)

        job.delete()

        return Response({
            'status': 'job deleted',
            'status': status.HTTP_204_NO_CONTENT,
        })
