from django.core.management.base import BaseCommand
from blogapp.models import Category, Post, Tag

class Command(BaseCommand):

    def handle(self, *args, **options):
       categories = Category.objects.all()
       print(categories)
       print(type(categories))
       for item in categories:
           print(item)
           print(type(item))

       print('End')

       category = Category.objects.get(name='Игрушки')
       print(category)
       print(type(category))

       post = Post.objects.first()
       print(post)

       print(post.category)
       print(post.category.name)

       print(post.tags.all())

       # Создание
       Category.objects.create(name='Новая', description='Что-то')

       #Измененение

       category = Category.objects.get(name='Новая')
       category.name = 'Измененная'
       category.save()

       #удаление
       category.delete()
       #category.objects.all().delete()
