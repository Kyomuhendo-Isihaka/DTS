from django.contrib import admin
from django.urls import path, include
from dts import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('dts/', include('dts.urls')),
    path('dtsClients/', include('dtsClients.urls'))
   
]
