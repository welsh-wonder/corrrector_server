from django.urls import path, re_path
from django.conf.urls import url
from  . import views

app_name = 'notes'

urlpatterns = [
    path('', views.ListNotes.as_view(), name="all"),
    path('nueva/', views.CreateNote.as_view(), name="create"),
    path('by/<str:username>/<int:pk>/', views.SingleNote.as_view(), name="single"),
    path('update/', views.EditNote.as_view(), name="update"),
    path('by/<str:username>/<int:pk>/update/', views.EditNote.as_view(), name="update"),
    re_path(r'^borrar/(?P<pk>\d+)/$', views.DeleteNote.as_view(), name="delete"),
]
# url(r"by/(?P<username>[-\w]+)/(?P<pk>\d+)/$", views.SingleNote.as_view(), name="single"),
