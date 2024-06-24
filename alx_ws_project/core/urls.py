from django.urls import path
from . import views

urlpatterns = [
  path('signup/', views.signup, name='signup'),
  path('signin/', views.signin, name='signin'),
  path("user/profile/", views.profile, name="profile"),
  path("update_profile/", views.update_profile, name="update-profile"),
  path("signout/", views.signout, name="signout"),
]