from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenRefreshView
from user.view.auth import MyTokenObtainPairView, RegisterView
from user.view.user import UserDetailView, UserView

urlpatterns = [
    #Authentication
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),

    # User
    re_path(r'^user/$', UserView.as_view(), name='user_view'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail_view'),

]