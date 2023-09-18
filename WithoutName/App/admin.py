from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from .models import Category, Review, Game

class GameAdminForm(forms.ModelForm):
    """Форма с виджетом ckeditor"""
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Game
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ("name", )
    list_display_links = ("name",)


class ReviewInline(admin.TabularInline):
    """Отзывы на странице фильма"""
    model = Review
    extra = 1
    readonly_fields = ("name", "email")



@admin.register(Game)
class MovieAdmin(admin.ModelAdmin):
    """Фильмы"""
    list_display = ("title", "cat_id", "draft")
    list_filter = ("cat_id", "year")
    search_fields = ("title", "cat_id__name")
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    actions = ["publish", "unpublish"]
    form = GameAdminForm
    readonly_fields = ("get_image",)
    fieldsets = (
        (None, {
            "fields": (("title"),)
        }),
        (None, {
            "fields": ("description", ("picture", "get_image"))
        }),
        (None, {
            "fields": (("year"),)
        }),
        ("Options", {
            "fields": (("draft"),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.picture.url} width="100" height="110"')

    def unpublish(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
        """Опубликовать"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ('change', )

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permissions = ('change',)

    get_image.short_description = "Постер"


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Отзывы к фильму"""
    list_display = ("name", "email", "parent", "game", "id")
    readonly_fields = ("name", "email")