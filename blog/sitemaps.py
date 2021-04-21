from django.contrib.sitemaps import Sitemap
from blog.models import Post

class PostSitemap(Sitemap):
    protocol = 'https'
    def items(self):
        return Post.objects.all()
