from django.urls import path
from . import views
from notes import views as note_views

urlpatterns = [
    path('', note_views.ListNotes.as_view(), name="home"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('change_password/', views.change_password, name="change_password"),
    path('new_note/', views.new_note, name="new_note"),
]
# path('', views.home, name="home"),