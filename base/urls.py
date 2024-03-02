from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoints),
    path('advocates/', views.advocates_list),
    #path('advocates/<str:username>/', views.advocate_detail),
    path('advocates/<str:username>/', views.Advocate_detail.as_view()),
    
    # companies/
    path('companies/', views.company_list)
    # companies/id
    
]