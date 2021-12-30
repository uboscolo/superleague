from django.urls import path
from . import views

app_name = 'league'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:league_id>/', views.league_view, name='league_view'),
    path('<int:league_id>/table/', views.table_view, name='table_view'),
    path('<int:league_id>/match/', views.match_view, name='match_view'),
]
