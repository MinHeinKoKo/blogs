from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns= [
    path('search/',views.search, name='search'),
    path('',views.index, name='index'),
    path('base/',views.base, name='base'),
    path('<slug:slug>/', views.detail, name='post_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # path('detail/<str:pk>',views.detail, name='detail'),
    # path('<slug:slug>', views.detail, name='detail')