from django.contrib import admin
from licencecreater import models
from .models import Document
from .models import Keyword
admin.site.register(Document)
admin.site.register(Keyword)
# Register your models here.
