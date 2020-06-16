# Adds lines from files specified.
from django.conf import settings
from django.db import models
from django.utils import timezone

# Class defines post model as object. models.Models indicates
# ...that post is a Django model.
class Post(models.Model):
    # Links to another model.
    author = models.ForeignKey(settings.AUTH_USER_MODEL,\
                               on_delete=models.CASCADE)
    # Defines text with a text limit.
    title = models.CharField(max_length=200)
    # Defines long text without a limit.
    text = models.TextField()
    # Defines the date and time.
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

# Function that publishes the post.
def publish(self):
    self.published_date = timezone.now()
    self.save()

# Returns a string of the title of the post.
def __str__(self):
    return self.title