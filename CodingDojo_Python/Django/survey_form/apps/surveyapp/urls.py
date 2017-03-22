from django.conf.urls import url
from . import views           
urlpatterns = [
	url(r'^$', views.index),
	url(r'^add_user$', views.add_user),
	url(r'^results$', views.show_results), 
	# url(r'^results$', views.results),
  ]