from django.shortcuts import render
from .models import TextFile, ImageFile, PDFFile, MiscFile, Show


def home(request):
    if request.method == 'POST':
        show = Show()
        show.name = request.POST.get('name', None)
        show.desc = request.POST.get('desc', None)
        show.save()
        files = request.FILES.getlist('bulkfiles[]', None)
        if files:
            for x in files:
                ext = x.name.split('.')[-1]
                if ext.lower() == 'pdf':
                    PDFFile.objects.create(file=x, show=show)
                elif ext.lower() in ['png', 'jpg', 'jpeg', 'gif']:
                    ImageFile.objects.create(file=x, show=show)
                elif ext.lower() == 'txt':
                    TextFile.objects.create(file=x, show=show)
                else:
                    MiscFile.objects.create(file=x, show=show)
    return render(request, 'pages/home.html')


def show(request, pk):
    this_show = Show.objects.get(pk=pk)
    textfiles = TextFile.objects.filter(show__pk=pk)
    imgfiles = ImageFile.objects.filter(show__pk=pk)
    pdffiles = PDFFile.objects.filter(show__pk=pk)
    miscfiles = MiscFile.objects.filter(show__pk=pk)
    return render(request, 'pages/show.html', {
        'show': this_show,
        'textfiles': textfiles,
        'imgfiles': imgfiles,
        'pdffiles': pdffiles,
        'miscfiles': miscfiles
    })
