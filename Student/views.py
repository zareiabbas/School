import datetime
from rest_framework import viewsets
from . import models, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


# code haye permission va authentication ham neveshtam va faqat baraye sade sazi felan comment kardam
class StudentsViewSet(viewsets.ModelViewSet):
    queryset = models.Students.objects.all()
    serializer_class = serializers.StudentsSerializer
    http_method_names = ['get']
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


# rahe dovom mitoone in bashe ke az tariqe query params age ro bgirim ke dynamic tare
# be khatere kamboode vaqt in rahe sade tar ro neveshtam
class StudentsFatherOlderSixty(viewsets.ModelViewSet):
    delta = datetime.datetime.now() - datetime.timedelta(days=21900)
    queryset = models.Students.objects.filter(father_birthday__lt=delta)
    serializer_class = serializers.StudentsSerializer
    http_method_names = ['get']


# in mored ro ham ba raveshe decoratator neveshtam ke az do ravesh motefavet baraye test estefade karde basham
@api_view(['GET', ])
def vaccinated_students(request):
    vaccine_status = request.query_params['vaccine']
    if vaccine_status == 'firstDose':
        try:
            result = models.Students.objects.filter(vaccination_status='First Dose')
            ser = serializers.StudentsSerializer(result, many=True)
            return Response(ser.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif vaccine_status == 'secondDose':
        try:
            result = models.Students.objects.filter(vaccination_status='Second Dose')
            ser = serializers.StudentsSerializer(result, many=True)
            return Response(ser.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
