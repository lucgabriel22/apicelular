from django.contrib import admin
from django.urls import path, include
from celulares.urls import router




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]

