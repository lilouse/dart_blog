from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='category_slug')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('category_page', kwargs={'slug': self.slug})



class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, verbose_name='tag_slug')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='post_slug')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='опубликовано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    views = models.IntegerField(default=0, verbose_name='кол-во просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ['-created_at']
