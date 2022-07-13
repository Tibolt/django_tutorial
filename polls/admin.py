from django.contrib import admin

from .models import Question, User, Choice

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(User)