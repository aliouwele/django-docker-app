from django.urls import path
from django.contrib import admin

from . import views




app_name = 'app'
urlpatterns = [
    path('', admin.site.urls),

]
