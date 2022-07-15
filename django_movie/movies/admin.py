from django.contrib import admin
from .models import Category, Genre, Movie, MovieShots, Actors, Rating, RatingStar, Reviews


@admin.register(Category)  # Регистрируем модель категории с помошью декоратора
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')  # Отображение нужных нам столбцов в Админ, порядок как сдесь
    list_display_links = ('id', 'name', 'url')  # Указывается поле которое будет ссылкой на выбранную категорию


class ReviewInline(admin.StackedInline):   #При выборе фильма показ его отзывов
    model = Reviews
    extra = 1     #Количество дополнительных полей отзывов в админке
    readonly_fields = ('name', 'email')


@admin.register(Movie)  # Регистрируем модель категории с помошью декоратора
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'draft')  # Отображение нужных нам столбцов в Админ, порядок как сдесь
    list_filter = ('category', 'year')  # Добавление возможности фильтрации по категориям и по году
    search_fields = ('title', 'category__name')  # Добавление поиска по выбранным столбцам
    inlines = [ReviewInline]
    save_on_top = True  # Кнопка сохранения должна быть сверху
    save_as = True     #добавить кнопку Сохранить как новый объект
    list_editable = ('draft',)     #Делает позможным редактировать поле драфт прям из списка фильмов
    fieldsets = (                   #Групировка вывода полей таблицы группами в строку с присвоением названия каждой группе вместо None
        (None, {
            'fields': (('title', 'tagline'),)
        }),
        (None, {
            'fields': (('description', 'poster'),)
        }),
        (None, {
            'fields': (('year', 'world_premiere', 'county'),)
        }),
        ('Actors', {
            'classes': ('collapse',),        #Скрыть отображение групп ниже 4 шт и показать название этой группы Actors
            'fields': (('actors', 'directors', 'category', 'genres'),)
        }),
        (None, {
            'fields': (('budget', 'fees_in_usa', 'fees_in_world'),)
        }),
        (None, {
            'fields': (('url', 'draft'),)
        }),
    )

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'text', 'parent', 'movie')
    readonly_fields = ('name', 'email')

class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ('title', 'image','movie')


class ActorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'description', 'image')


class RatingAdmin(admin.ModelAdmin):
    list_display = ('ip', 'star', 'movie')




# admin.site.register(Category, CategoryAdmin)    #выше тоже самое с помошью декоратора
admin.site.register(Genre)
# admin.site.register(Movie)
admin.site.register(MovieShots, MovieShotsAdmin)
admin.site.register(Actors, ActorsAdmin)
admin.site.register(Rating, RatingAdmin)

admin.site.register(Reviews, ReviewAdmin)
