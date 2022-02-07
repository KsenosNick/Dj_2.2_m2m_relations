from django.contrib import admin

from .models import Article, Scope, ArticleScope


@admin.register(Scope)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name']


class ScopeInline(admin.TabularInline):
    model = ArticleScope
    extra = 0


@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at']
    inlines = [ScopeInline]

