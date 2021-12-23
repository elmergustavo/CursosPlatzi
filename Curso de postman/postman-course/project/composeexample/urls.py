"""composeexample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework import routers
from courses import views

router = routers.DefaultRouter()
router.register(r'courses', views.CoursesViewSet, basename='courses')
router.register(
    r'private/courses', views.PrivateCoursesViewSet, basename='private_courses'
)
router.register(r'materials', views.MaterialViewSet, basename='materials')
router.register(r'comments', views.CommentViewSet, basename='comments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
