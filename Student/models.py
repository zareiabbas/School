from django.db import models


class Students(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    father_birthday = models.DateField(null=True, blank=True)
    field = models.ForeignKey('Fields', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    enroll_date = models.DateField(auto_now=True)
    graduate_date = models.DateField(null=True, blank=True)

    VACCINATION_STATUS = (
        ('Unvaccinated', 'Unvaccinated'),
        ('First Dose', 'First Dose'),
        ('Second Dose', 'Second Dose')
    )
    vaccination_status = models.CharField(max_length=12, choices=VACCINATION_STATUS, default='Unvaccinated')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Fields(models.Model):
    field_name = models.CharField(max_length=150)

    def __str__(self):
        return self.field_name


class Courses(models.Model):
    course_name = models.CharField(max_length=150)
    field = models.ManyToManyField(Fields)

    def __str__(self):
        return f'{self.course_name}({self.field.last().field_name})'
