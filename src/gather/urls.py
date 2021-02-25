from django.urls import path
from gather import views

urlpatterns = [
    path('', views.get_btc_rows),
    path('update_btc', views.update_btc_info),
]