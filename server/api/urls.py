from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

urlpatterns = [
    path('', views.getRoutes),

    path('users/register/', views.registerUser, name="create_user"),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('testEmail/', views.testEmail),
    path('products/', views.getProducts),
    path('product/<str:pk>/', views.getProduct),
    path('products/<str:pk>/vote/', views.productVote),

    path('cart/<str:pk>/', views.productVote),




]
