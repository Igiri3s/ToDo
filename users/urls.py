from django.urls import path
from .views import RegisterView,UserViewSet, LoginView,UserView,LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register-user'),
    path('getLogedUser/', UserView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('getAllUsers/', UserViewSet.as_view({'get': 'list'}), name='get-all-users')
]
