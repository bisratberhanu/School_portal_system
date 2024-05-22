from . import views
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter

router = DefaultRouter()

router.register('initialuser', views.InitialUserViewSet, basename='initialuser')

urlpatterns = router.urls