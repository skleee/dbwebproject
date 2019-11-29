from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
import shop.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shop.views.home, name='home'),

    path('filter/<str:f>/<str:select>', shop.views.filter, name='filter'),
    path('searchitem/', shop.views.searchitem, name='search'),
    path('buy/', shop.views.buy, name='buy'),
    path('mypage/', shop.views.mypage, name='mypage'),
    
    path('shop/', include('shop.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
