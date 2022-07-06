from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django_summernote.fields import SummernoteTextField
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))

# Recipe Model

class Post(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_posts"
    )
    content = SummernoteTextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    prep_time = models.DurationField()
    cook_time = models.DurationField()
    servings = models.IntegerField()
    likes = models.ManyToManyField(
        User, related_name='recipepost_like', blank=True)

    # Orders the recipes so newest shows first

    class Meta:
        ordering = ["-created_on"]

    # Returns a string representation of an object

    def __str__(self):
        return self.title

    # Returns the number of likes on a recipe

    def number_of_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self, *args, **kwargs):
        return reverse('home')

# Comment Model

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=70)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    # Orders the comments in ascending order

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
