from django.contrib import admin

from .models import (
	BlogPost,
	BlogPostTag,
	Tag,
)

# Register your models here.
class BlogPostTagInline(admin.TabularInline):
	model = BlogPostTag

class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'user',)
	search_fields = ('title', 'slug', 'user',)
	inlines = (
		BlogPostTagInline,
	)

class BlogPostTagAdmin(admin.ModelAdmin):
	pass

class TagAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogPostTag, BlogPostTagAdmin)
admin.site.register(Tag, TagAdmin)
