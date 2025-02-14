
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

from authentication.views import home, about, logout_user,registration,LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name='home'),
    path('about/', about, name='about'),
    path('registrations/', registration, name='registrations'),
    path('login/', LoginView.as_view(template_name='crm_project/login.html'),name='login'),
    path('logout/', logout_user, name='logout'),
    path('dashboard/', include('dashboard.urls')),
    path('dashboard/product/', include('product.urls')),
    path('dashboard/customer/', include('customer.urls')),
    path('api/v1/', include('api.urls'))

]
