# encoding: utf-8

from django.conf.urls import url
from blog import views

urlpatterns = [

    url(r'^blog/$', views.IndexView.as_view(), name='index'),
    # 首页调用IndexView

    url(r'^blog/article/(?P<article_id>\d+)$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^blog/category/(?P<cate_id>\d+)$', views.CategoryView.as_view(), name='category'),

]

# 使用(?P<>\d+)的形式捕获值给<>中得参数，比如(?P<article_id>\d+)，当访问/blog/article/3时，将会将3捕获给article_id,这个值会传到views.ArticleDetailView,这样我们就可以判断展示哪个Article了
