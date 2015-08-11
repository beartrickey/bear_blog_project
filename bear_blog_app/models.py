# ======================================================
# IMPORTS
# ======================================================
# Python

# Django
from django.contrib.auth.models import User
from django.db import models

# Third Party
from model_utils.models import TimeFramedModel, TimeStampedModel

# Local



# ======================================================
# MODELS
# ======================================================
class BlogPost(TimeStampedModel):

	title = models.CharField(
		max_length=200,
		null=True,
		blank=True,
	)

	slug = models.CharField(
		max_length=200,
		null=True,
		blank=True,
	)

	content = models.TextField()

	user = models.ForeignKey(
		to=User,
		related_name="blog_posts",
	)

	def __unicode__(self):
		return '{0}'.format(self.title)

	def __str__(self):
		return self.__unicode__()


class Tag(models.Model):
	
	name = models.CharField(
		max_length=100,
	)

	def __unicode__(self):
		return '{0}'.format(self.name)

	def __str__(self):
		return self.__unicode__()


class BlogPostTag(models.Model):
	
	blog_post = models.ForeignKey(
		to="BlogPost",
		related_name="blog_post_tags",
	)

	tag = models.ForeignKey(
		to="Tag",
		related_name="blog_post_tags",
	)
	
	def __unicode__(self):
		return '{0} >>> {1}'.format(self.blog_post.title, self.tag.name)

	def __str__(self):
		return self.__unicode__()
