from django.conf.urls import url
from app01 import views

urlpatterns = [
    url(r'^addbook/$', views.addbook, name='addbook'),
    url('delete/(\d+)', views.delbook, name="delbook"),
    url('edit/(\d+)', views.editbook, name="editbook"),
    url(r'^$', views.books,name="index"),

]
