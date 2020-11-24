
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/(?P<version>(v1))/', include('employees.urls'))
]