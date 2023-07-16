from django.db import models
from django.utils import timezone
from django.urls import reverse


class ReadyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Choice.ready_paper)


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class News(models.Model):
    class Choice(models.TextChoices):
        draft_paper = "D", "Draft"
        ready_paper = "R", "Ready"

    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images/')
    status = models.CharField(max_length=1, choices=Choice.choices, default=Choice.draft_paper)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-detail', args=[self.slug])

    # default manager
    objects = models.Manager()
    ready = ReadyManager()

    class Meta:
        ordering = ['-published_time']


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.email
