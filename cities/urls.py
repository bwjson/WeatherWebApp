from django.urls import path, include
from . import views

app_name = 'cities'

urlpatterns = [
    path('', views.CityListView.as_view(), name='list'),
    path('search/', views.CityListView.as_view(), name='search'),
    path('<slug:slug>/', views.CityDetailView.as_view(), name='detail'),
    path('rate-city/<slug:slug>/', views.RateCityView.as_view(), name='rate_city')
]
