from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import BlogPost

# Create your views here.
class ArchiveListView(ListView):

	model = BlogPost
	template_name = "bear_blog_app/archive.html"

class BlogPostView(TemplateView):

	template_name = "bear_blog_app/blog_post.html"

	def get_context_data(self, **kwargs):

		data = super(BlogPostView, self).get_context_data(**kwargs)

		blog_post_slug = self.kwargs.get("blog_post_slug")

		blog_post = BlogPost.objects.get(slug=blog_post_slug)

		data.update({"blog_post": blog_post})

		return data
