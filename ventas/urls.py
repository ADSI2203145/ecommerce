from django.urls import path
from ventas.views import ejemplo_view
#from .views import *

urlpatterns = [
    path('ejemplo/', ejemplo_view, name = 'ejemplo'),
]