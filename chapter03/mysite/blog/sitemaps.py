from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from taggit.models import Tag
from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated


class TagSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        # Get all tags that are used in published posts
        return Tag.objects.filter(
            taggit_taggeditem_items__object_id__in=Post.published.values_list('id', flat=True)
        ).distinct()

    def location(self, obj):
        return reverse('blog:post_list_by_tag', args=[obj.slug])

