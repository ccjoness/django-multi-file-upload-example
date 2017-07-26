from django.db import models
from django.utils.text import slugify


def text_upload_handler(instance, filename):
    return '{}/text/{}'.format(slugify(instance.show.name), filename)


def image_upload_handler(instance, filename):
    return '{}/img/{}'.format(slugify(instance.show.name), filename)


def pdf_upload_handler(instance, filename):
    return '{}/pdf/{}'.format(slugify(instance.show.name), filename)


def misc_upload_handler(instance, filename):
    return '{}/pdf/{}'.format(slugify(instance.show.name), filename)


class TextFile(models.Model):
    file = models.FileField(upload_to=text_upload_handler)
    show = models.ForeignKey('Show')

    def __str__(self):
        return self.file.name


class ImageFile(models.Model):
    file = models.FileField(upload_to=image_upload_handler)
    show = models.ForeignKey('Show')

    def __str__(self):
        return self.file.name


class PDFFile(models.Model):
    file = models.FileField(upload_to=pdf_upload_handler)
    show = models.ForeignKey('Show')

    def __str__(self):
        return self.file.name


class MiscFile(models.Model):
    file = models.FileField(upload_to=misc_upload_handler)
    show = models.ForeignKey('Show')

    def __str__(self):
        return self.file.name


class Show(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return '{}'.format(self.name)
