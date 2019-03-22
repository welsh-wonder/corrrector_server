from django import template
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings
import misaka

User = get_user_model()
register = template.Library()

class Note(models.Model):
    user = models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=False)
    slug = models.SlugField(allow_unicode=True, unique=True)
    content = models.TextField(blank=False, default='')
    content_html = models.TextField(editable=False, blank=True, default='')
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        self.slug = slugify(self.title)
        self.content_html = misaka.html(self.content)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "notes:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk,
            }
        )

    class Meta:
        ordering = ['-updated_at']
        unique_together = ['user', 'content']

class Error(models.Model):
    note = models.ForeignKey(Note, related_name='errors', on_delete=models.CASCADE)
    phrase = models.CharField(editable=False, max_length=512, unique=False)
    suggestion = models.CharField(editable=False, max_length=512, unique=False)
    explanation = models.TextField(editable=False, blank=True, default='')

    def __str__(self):
        return self.explanation[:30]
