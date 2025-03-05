
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('', include('core.urls', namespace='home')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/',auth_views.LogoutView.as_view(),name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)