from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users import views as user_views
from contacts.views import contact 


urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('contacts/', include('contacts.urls')),
    path('accounts/', include('accounts.urls')),
    path('partners/', include('partners.urls')),
    path('testaments/', include('testaments.urls')),
    path('profile/', user_views.profile, name='profile'),
 
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
