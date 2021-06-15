from django.urls import path, include

from product import views as views

urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
]