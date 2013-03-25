# -*- coding: utf-8 -*-

from db_file_storage.model_utils import delete_file_if_needed
from django.core.urlresolvers import reverse
from django.db import models


class ConsolePicture(models.Model):
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)
    creation = models.DateTimeField(auto_now_add=True)


class Console(models.Model):
    name = models.CharField(max_length=100, unique=True)
    picture = models.ImageField(upload_to='console.ConsolePicture/bytes/filename/mimetype', blank=True, null=True)
    year = models.IntegerField()
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('console.edit', kwargs={'pk': self.id})
    
    @classmethod
    def get_create_url(cls):
        return reverse('console.add')
    
    def save(self, *args, **kwargs):
        delete_file_if_needed(self, 'picture')
        super(Console, self).save(*args, **kwargs)