from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, ArticleScope


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['name']


class ScopeInline(admin.TabularInline):
    model = ArticleScope
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at']
    inlines = [ScopeInline]

