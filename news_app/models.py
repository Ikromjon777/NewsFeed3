from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from hitcount.models import HitCountMixin, HitCount
# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Published)





class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class News(models.Model, HitCountMixin):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    create_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    # Status bu yangilik saytga chiqorishga tayyor ekanligini kursatadi.
    # Draft -- tayyor emas( Qoralama )
    # Published -- tayyor chiqarishga
    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"

    status = models.CharField(max_length=2, choices=Status.choices, default=Status.Draft)

    objects = models.Manager() # default manager
    published = PublishedManager() # yangi o'zimiz yaratgan manager/ faqat Published bo'lganlarni chiqaradi
    # News.objects.all()
    # News.published.all()

    # Endi tartiblashni ko'ramiz
    class Meta:
        ordering = ('-publish_time',) # Oxirgi qo'shilgan yangilik birinchi chiqadi

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("news_detail", args=[self.slug])

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.email

class Foto(models.Model):
    foto = models.ImageField(upload_to='news/foto')


class Comment(models.Model):
    news = models.ForeignKey(News,
                             on_delete=models.CASCADE,
                             related_name='comments')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='comments')
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    activate = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_time']
    def __str__(self):
        return f'{self.user} by comments'