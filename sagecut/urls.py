from django.conf.urls import url
from . import views

#template urls
app_name ='sagecut'

#urls

urlpatterns = [
    url(r'^book/$',views.book,name='book'),
]
