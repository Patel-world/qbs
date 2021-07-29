from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import ArticleSitemap

app_name='story'

sitemaps = {
    'blog':ArticleSitemap
}

urlpatterns = [
    path('topics/', views.topics, name='topics'),
     path('', views.story_list, name='story_list'),
  
     path('search/',views.search,name='search'),
     path('<slug:category_slug>', views.story_list, name='story_by_category'),
     path('<slug:slug>/', views.story_detail, name='story_detail'),
     
     
     path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

   # path('admin/', admin.site.urls),

]
