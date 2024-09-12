from django_filters import FilterSet
from .models import Faculty


class FacultyFilter(FilterSet):
    class Meta:
        model = Faculty
        fields = {
            'name':['exact'],
            'professor':['exact'],
            'course':['exact'],




        }
