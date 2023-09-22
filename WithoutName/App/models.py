from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField('Категория', max_length=255,)
    description = models.TextField('Описание')

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField('Заголовок')
    content = models.TextField('Описание')
    picture = models.ImageField('Обложка', upload_to='games/')
    year = models.PositiveSmallIntegerField("Дата выхода", default=2019)
    country = models.CharField("Страна", max_length=30, default=None, null=True, blank=True)
    cat_id = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    def get_reviews(self):
        return self.reviews.filter(parent__isnull=True)
class Review(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    text = models.TextField()
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True, related_name='children'
    )
    game = models.ForeignKey(Game, verbose_name='Название Игры', on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"{self.name} - {self.game}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

