from . import views
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter

router = DefaultRouter()

router.register('departments', views.DepartmentView, basename='department')

departments_router = NestedDefaultRouter(router, 'departments', lookup='department')
departments_router.register('courses', views.CourseView, basename='department-course')

urlpatterns = router.urls + departments_router.urls