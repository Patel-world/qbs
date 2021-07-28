from django.contrib.sitemaps import Sitemap
from .models import Story
 
 
class ArticleSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Story.objects.all()

    def lastmod(self, obj):
        return obj.publish
        
    def location(self,obj):
        return '/quest/%s' % (obj.slug)
