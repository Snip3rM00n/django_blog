from django.contrib.syndication.views import Feed
from django.urls import reverse

from blogging.models import Post

class LatestPostsFeed(Feed):
    title = "Recent Posts"
    link = "/"
    description = "The most recent posts from my blog!"

    def items(self):
        published = Post.objects.exclude(published_date__exact=None)
        posts = published.order_by("-published_date")[:5]
        return posts
    
    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text
    
    def item_link(self, item):
        return reverse("blog_detail", args=[item.pk])
