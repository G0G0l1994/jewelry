
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

from core.views import home, about, logout_user
from authentication.views import registration


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name='home'),
    path('about/', about, name='about'),
    path('registrations/', registration, name='registrations'),
    path('login/', views.LoginView.as_view(template_name='crm_project/login.html'),name='login'),
    path('logout/', logout_user, name='logout'),
    path('dashboard/', include('dashboard.urls')),
    path('dashboard/product/', include('product.urls'))

]
