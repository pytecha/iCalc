from django.urls import path
from .views import *

urlpatterns = [
    path('', calculator,name="calc"),
    path('ajax-math/', ajaxreq,name="ajax-math"),
    path('ajax-sci/', ajaxsci,name="ajax-sci"),
]