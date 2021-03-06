"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from bear_blog_app.views import (
	BlogPostListView,
	BlogPostView,
)

urlpatterns = [
	url(
		r'^admin/',
		 include(admin.site.urls)
	),
	url(
		r'^$',
		view=BlogPostListView.as_view(),
		name='blog_post_list_view',
	),
	url(
		r'^post/(?P<blog_post_slug>[-\S]+)$',
		view=BlogPostView.as_view(),
		name='blog_post_view',
	),
]
