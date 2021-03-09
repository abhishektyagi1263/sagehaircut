from django.conf.urls import url
from . import views

#template urls
app_name ='sagecut'

#urls

urlpatterns = [
    url(r'^book/$',views.book,name='book'),
    url(r'^reservations/$',views.reservations,name='reservations'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]
