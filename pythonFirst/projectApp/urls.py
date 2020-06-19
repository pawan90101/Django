from django.urls import path
from projectApp.views import App_View

urlpatterns = [ 
    path('', App_View), 
]