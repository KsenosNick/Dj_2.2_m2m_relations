from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, ArticleScope


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['name']


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        if len(self.forms) == 0:
            raise ValidationError('Не указан основной раздел!')

        if len(self.forms) != len({form.cleaned_data['scope'].id for form in self.forms}):
            raise ValidationError('Основной раздел может быть только один!')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ScopeInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at']
    inlines = [ScopeInline]

