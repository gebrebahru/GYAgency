from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    admin.site.login_template = 'admin/login.html'
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),
    
    # 🌟 እይታ ለመቁጠር የተጨመረ አዲስ ሊንክ
    path('post/<str:obj_type>/<int:obj_id>/', views.post_detail, name='post_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)