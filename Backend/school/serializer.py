from . import models
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = ['id', 'name']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id', 'name', 'credit_hour']
    
    def create(self, validated_data):
        validated_data['department_id'] = self.context['department']
        return models.Course.objects.create(**validated_data)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['id', 'CGPA', ]