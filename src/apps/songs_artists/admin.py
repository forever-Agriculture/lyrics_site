from django.contrib import admin
from django.core.urlresolvers import reverse
from django.forms import ModelForm, ValidationError

from .models import Band, Lyrics

admin.site.register(Band)
admin.site.register(Lyrics)
