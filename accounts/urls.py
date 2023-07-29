from django.urls import path
from .views import Login, Logout, Profile, RegisterView, ProfileEditView, AdminPageView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/', Profile.as_view(), name='user_profile'),
    path('profile/edit/', ProfileEditView.as_view(), name='profile_edit'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('register/', RegisterView.as_view(), name='register'),
    path('admin/page/',AdminPageView.as_view(), name='admin_page'),

]