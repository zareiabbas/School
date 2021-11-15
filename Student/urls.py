from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('students', views.StudentsViewSet, basename='students')
router.register('studentsFatherSixty', views.StudentsFatherOlderSixty, basename='studentsFatherSixty')

urlpatterns = [
    path('', include(router.urls)),
    path('vaccination/', views.vaccinated_students)
]
