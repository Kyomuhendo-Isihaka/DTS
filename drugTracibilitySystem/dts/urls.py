from django.urls import path 
from . import views

urlpatterns=[
    path('', views.login, name='login'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('healthcenters', views.healthcenters, name='healthcenters'),
    path('pharmaceuticals', views.pharmaceuticals, name='pharmaceuticals'),
    path('editpharmaceutical/<int:pk>/', views.editpharmaceutical, name='editpharmaceutical'),
    path('deletePharmaceutical/<int:pk>', views.deletePharmaceutical, name='deletePharmaceutical'),
    path('transactions', views.transactions, name='transactions'),
    path('administrators', views.administrators, name='administrators'),
    path('edithealthcenter/<int:pk>', views.edithealthcenter, name='edithealthcenter'),
    path('deletehealthcenter/<int:pk>', views.deleteHealthcenter, name='deletehealthcenter'),
    path('healthcenter/<int:pk>', views.healthcenter, name='healthcenter'),

]