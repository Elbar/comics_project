from __future__ import unicode_literals
from django.conf import settings
from django.db import models

# Create your models here.

from wand.image import Image


def file_upload_to(instance, filename):
    return "images/%s" % filename


class Coordinate(models.Model):
    x = models.DecimalField(max_digits=1000, decimal_places=2)
    y = models.DecimalField(max_digits=1000, decimal_places=2)
    h = models.DecimalField(max_digits=1000, decimal_places=2)
    w = models.DecimalField(max_digits=1000, decimal_places=2)


class ComicsImage(models.Model):
    image = models.CharField(max_length=200)
    coordinates = models.ManyToManyField(Coordinate, null=True, blank=True)

    def __unicode__(self):
        return str(self.id)


class UploadComics(models.Model):
    name = models.CharField(max_length=100)
    pdf = models.FileField(upload_to=file_upload_to, null=True, blank=True)
    cover = models.ImageField(upload_to=file_upload_to, null=True, blank=True)

    def save(self, *args, **kwargs):
        super(UploadComics, self).save()
        img = Image(filename=self.pdf._get_path(), resolution=200)
        img.save(filename=settings.BASE_DIR + '/static_in_env/media_root/images/temp-%s-%s.jpg' % (
            self.id, self.name))
        comic = Comics.objects.create(general_id=self.id)
        for i in range(len(img.sequence)):
            image = ComicsImage(image='/media/images/temp-%s-%s-%s.jpg' % (self.id, self.name, i))
            image.save()
            comic.pages.add(image)
        comic.save()


class Comics(models.Model):
    general = models.OneToOneField(UploadComics,null=True)
    pages = models.ManyToManyField(ComicsImage, null=True, blank=True)

    def __unicode__(self):
        return self.general.name
