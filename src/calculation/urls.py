from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'calculation'
urlpatterns = [
    #path('', TemplateView.as_view(template_name='index.html'))
    path('', views.index, name='index')
]