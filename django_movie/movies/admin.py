from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Genre, Movie, MovieShots, Actors, Rating, RatingStar, Reviews


@admin.register(Category)  # Регистрируем модель категории с помошью декоратора
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')  # Отображение нужных нам столбцов в Админ, порядок как сдесь
    list_display_links = ('id', 'name', 'url')  # Указывается поле которое будет ссылкой на выбранную категорию

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'url')


class ReviewInline(admin.StackedInline):  # При выборе фильма показ его отзывов
    model = Reviews
    extra = 1  # Количество дополнительных полей отзывов в админке
    readonly_fields = ('name', 'email')


class MovieShotInline(
    admin.TabularInline):  # При выборе фильма показ его кадров из другой таблицы, а TabularInline говорит отображать поля горизонтально
    model = MovieShots
    extra = 1
    fields = ['title', 'get_image']
    readonly_fields = ['get_image']

    # Метод ниже добавляет изображение в админку вместо ссылки
    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" height="100">')

    get_image.short_description = 'изображение'  # даем название столбцу в админке


@admin.register(Movie)  # Регистрируем модель категории с помошью декоратора
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'draft')  # Отображение нужных нам столбцов в Админ, порядок как сдесь
    list_filter = ('category', 'year')  # Добавление возможности фильтрации по категориям и по году
    search_fields = ('title', 'category__name')  # Добавление поиска по выбранным столбцам
    inlines = [MovieShotInline, ReviewInline]
    save_on_top = True  # Кнопка сохранения должна быть сверху
    save_as = True  # добавить кнопку Сохранить как новый объект
    list_editable = ('draft',)  # Делает позможным редактировать поле драфт прям из списка фильмов
    fieldsets = (  # Групировка вывода полей таблицы группами в строку с присвоением названия каждой группе вместо None
        (None, {
            'fields': (('title', 'tagline'),)
        }),
        (None, {
            'fields': (('description', 'get_image_movie', 'poster'),)
        }),
        (None, {
            'fields': (('year', 'world_premiere', 'county'),)
        }),
        ('Actors', {
            'classes': ('collapse',),  # Скрыть отображение групп ниже 4 шт и показать название этой группы Actors
            'fields': (('actors', 'directors', 'category', 'genres'),)
        }),
        (None, {
            'fields': (('budget', 'fees_in_usa', 'fees_in_world'),)
        }),
        (None, {
            'fields': (('url', 'draft'),)
        }),
    )
    readonly_fields = ['get_image_movie']

    # Метод ниже добавляет изображение в админку вместо ссылки
    def get_image_movie(self, obj):
        return mark_safe(f'<img src="{obj.poster.url}" height="200">')

    get_image_movie.short_description = 'Постер'  # даем название столбцу в админке


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'text', 'parent', 'movie')
    readonly_fields = ('name', 'email')


class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ('title', 'movie', 'get_image_movieshots')
    readonly_fields = ['get_image_movieshots']

    # Метод ниже добавляет изображение в админку вместо ссылки
    def get_image_movieshots(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" height="70">')

    get_image_movieshots.short_description = 'изображение'  # даем название столбцу в админке


class ActorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'get_image_actors')
    readonly_fields = ['get_image_actors']

    # Метод ниже добавляет изображение в админку вместо ссылки
    def get_image_actors(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" height="70">')

    get_image_actors.short_description = 'изображение'  # даем название столбцу в админке


class RatingAdmin(admin.ModelAdmin):
    list_display = ('ip', 'star', 'movie')


# admin.site.register(Category, CategoryAdmin)   #выше тоже самое с помошью декоратора
# admin.site.register(Movie)
admin.site.register(MovieShots, MovieShotsAdmin)
admin.site.register(Actors, ActorsAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Reviews, ReviewAdmin)

# 2 строчки ниже измениют название админ панели
admin.site.site_title = 'Django_Movies'
admin.site.site_header = 'Django_Movies'
