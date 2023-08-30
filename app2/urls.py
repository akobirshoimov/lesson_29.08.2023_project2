from django.urls import path
from .views import all_info,detail

urlpatterns = [
    path('all/',all_info),
    path('detail/<int:laptop_id>,phone_id',detail)
] 