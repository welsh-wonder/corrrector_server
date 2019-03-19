from django.urls import path
from  . import views

app_name = 'notes'

urlpatterns = [
    path('', views.ListNotes, name="all"),
    path('nueva/', views.CreateNote.as_view(), name="create"),
    path(r'notas/in/(?P<slug>[-\w]+)/$', views.SingleNote.as_view(), name="single"),
    path(r'borrar/(?P<pk>\d+)/$', views.DeleteNote.as_view(), name="delete"),
]
