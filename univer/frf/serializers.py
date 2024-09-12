from rest_framework import serializers
from .models import *





class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'




class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['user']



class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['name','code']




class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'




class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'




class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'



class FacultySerializer(serializers.ModelSerializer):
    professor = ProfessorSerializer(many=True,read_only=True)

    class Meta:
        model = Faculty
        fields = '__all__'

