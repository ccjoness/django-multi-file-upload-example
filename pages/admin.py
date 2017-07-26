from django.contrib import admin
from .models import ImageFile, TextFile, PDFFile, MiscFile, Show


admin.site.register(ImageFile)
admin.site.register(TextFile)
admin.site.register(PDFFile)
admin.site.register(MiscFile)
admin.site.register(Show)
