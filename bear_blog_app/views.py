from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import BlogPost

# Create your views here.
class BlogPostListView(ListView):

	model = BlogPost
	template_name = "bear_blog_app/blog_post_list.html"

	def get_queryset(self, **kwargs):

		qs = super(BlogPostListView, self).get_queryset(**kwargs)

		query_map = {
			"slug": "slug",
			"blog_post_tags__tag__name": "tag",
			"content__icontains": "search",
		}

		query_args = {}

		for k, v in query_map.items():
			param_value = self.request.GET.get(v)
			if param_value:
				query_args.update({k: param_value})

		qs = qs.filter(
			**query_args
		).order_by(
			"-created"
		)

		# Special filter to grab most recent post
		if self.request.GET.get("latest") == "True":
			qs = [qs.latest("created")]

		return qs

class BlogPostView(TemplateView):

	template_name = "bear_blog_app/blog_post.html"

	def get_context_data(self, **kwargs):

		data = super(BlogPostView, self).get_context_data(**kwargs)

		blog_post_slug = self.kwargs.get("blog_post_slug")

		blog_post = BlogPost.objects.get(slug=blog_post_slug)

		data.update({"blog_post": blog_post})

		return data
