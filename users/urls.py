from django.urls import path
from .views import home_view, details1_view, details2_view, details3_view

urlpatterns = [
    path('', home_view, name='home'),
    path('details_1', details1_view , name='details_1'),
    path('details_2', details2_view , name='details_2'),
    path('details_3', details3_view , name='details_3'),
]