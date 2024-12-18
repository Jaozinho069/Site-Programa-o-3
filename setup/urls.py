from django.contrib import admin
from django.urls import path
from sites.views import home
from django.conf import settings
from django.conf.urls.static import static
from sites import views
from django.contrib.auth import views as auth_views
from sites.views import login_view, register_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Aqui é a URL inicial (home)
    path('atividades/', views.atividades, name='atividades'),  # Corrigido para 'atividades'
    path('login/', views.login_view, name='login'),
    path('register/', register_view, name='register'),
   path('logout/', auth_views.LogoutView.as_view(), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
