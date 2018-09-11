from django.db import models
from django.utils import timezone
# the path to upload file

def get_uploaded_document_path(instance, filename):

    name = 'uploaded/%s' % (filename)
    return name
# the path of the converted file

def get_converted_document_path(instance, filename):

    name = 'converted/%s' % (filename)
    return name

# constructing a document class with attributes and the attributes calling a function which is the path of uploaded, converted file
class Document(models.Model):
    uploaded = models.FileField(
        upload_to=get_uploaded_document_path, default=None)
    converted = models.FileField(
        upload_to=get_converted_document_path, null=True, default=None, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
# image = models.ImageField(s
    # upload_to=get_uploded_document,
    # null=True, default=None, blank=True)


def __str__(self):
    return '%s %s' % (self.timestamp, self.id)
# the words class to here we are constructing a class with the words need to be change in the uploaded file 

class Keyword(models.Model):
    name = models.CharField(max_length=250, default=None)


def __str__(self):
    return '%s' % (self.id)

# Create your models here.
