from django import template
from movies.models import Category, Movie

register = template.Library()

@register.simple_tag()
def get_category():
    return Category.objects.all()

@register.simple_tag()
def get_movie():
    x = Movie.objects.order_by('id')[:5]
    return x