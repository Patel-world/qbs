from django.contrib.sitemaps import Sitemap
from .models import Story
 
 
class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Story.objects.all()

    def lastmod(self, obj):
        return obj.article_published
        
    def location(self,obj):
        return '/quest/%s' % (obj.slug)
