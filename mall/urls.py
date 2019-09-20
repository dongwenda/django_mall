from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^prod/list/$', views.product_list, name='procut_list'),
    url(r'^prod/detail/(?P<pk>\S+)/$', views.product_detail, name='product_detail'),
]



for path in path_list:
    try:
        os.remove(path)
    except:
        pass