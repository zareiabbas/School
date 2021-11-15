from . import models
from rest_framework import serializers


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Students
        fields = ('id', 'first_name', 'last_name', 'father_name', 'father_birthday', 'field', 'address', 'enroll_date',
                  'graduate_date', 'vaccination_status')
        read_only_fields = ('id', 'enroll_date')
