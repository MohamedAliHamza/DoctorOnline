from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import CreateReportSerializer
from .utils import create_report

from user.api.permissions import IsActive, IsDoctor


class CreateReportApi(APIView):

    permission_classes = [
        IsAuthenticated, IsDoctor, IsActive
    ]
    
    def post(self, request):
        serializer = CreateReportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        create_report(request.user.doctor, data['patient_id'], data['content'])
 
        return Response(status=status.HTTP_201_CREATED)


# class ListReportApi(APIView):

#     permission_classes = [
#         IsAuthenticated, IsDoctor, IsActive
#         ]
    
#     def get(self, request):
        
        
#         return Response(data, status=status.HTTP_200_OK)
