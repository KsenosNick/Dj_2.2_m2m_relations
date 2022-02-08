from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, ArticleScope


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['name']


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        if [(form.cleaned_data['is_main'] == True) for form in self.forms].count(True) > 1:
            raise ValidationError('Основной раздел должен быть 1!')
        if [(form.cleaned_data['is_main'] == True) for form in self.forms].count(True) == 0:
            raise ValidationError('не задан основной раздел!')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ScopeInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at']
    inlines = [ScopeInline]

