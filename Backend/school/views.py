from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializer
from . import permission

class DepartmentView(ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializer.DepartmentSerializer
    permission_classes = [permission.IsAdminOrReadOnly]

class CourseView(ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializer.CourseSerializer
    permission_classes = [permission.IsAdminOrReadOnly]
    def get_serializer_context(self):
        return {
            'department': self.kwargs['department_pk'],
        }