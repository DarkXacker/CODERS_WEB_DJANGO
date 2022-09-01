from .views import *
from django.urls import path

urlpatterns = [
    path('', ProgramsListView, name='programs_list'),
    path('<int:pk>/', ProgramsDetailView.as_view(), name='programs_detail'),
    path('create/', ProgramsCreateView.as_view(), name='programs_create'),
    path('delete/<int:pk>', ProgramsDeleteView.as_view(), name='programs_delete'),
    path('update/<int:pk>', ProgramsUpdateView.as_view(), name='programs_update'),
]