# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from uploader.models import Photo
from uploader.forms import ImageForm


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Photo(imagefile=request.FILES['imagefile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('uploader.views.list'))
    else:
        form = ImageForm()  # A empty, unbound form

    # Load documents for the list page
    photos = Photo.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'photos': photos, 'form': form},
        context_instance=RequestContext(request)
    )
