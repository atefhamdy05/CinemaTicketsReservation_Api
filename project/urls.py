

from django.contrib import admin
from django.urls import path
from tickets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('django/nomodlenoframe/',views.no_rest_no_model),
    path('django/nomodlewithframe/',views.no_rest_with_model),
    path('rest/fbv/',views.FBV),
    path('rest/fbv/<int:pk>',views.FBV_PK),
    path('rest/cbv/',views.CBV.as_view()),
    path('rest/cbv/<int:pk>',views.CBV_PK.as_view()),
    path('rest/mixins/',views.mixins_list.as_view()),
    path('rest/mixins/<int:pk>',views.mixins_pk.as_view()),
    path('rest/guests/', views.GuestList.as_view(), name='guest-list'),
    path('rest/guests/<int:pk>',views.GuestDetail.as_view(), name='guest-detail'),
    
    

]
