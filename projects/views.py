from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Project, Resume
import os
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.


def project_index(request):
    projects = Project.objects.all()
    cv = Resume.objects.all()

    paginator = Paginator(projects, 6)
    page = request.GET.get('page')

    try:
        pro = paginator.page(page)
    except PageNotAnInteger:
        pro = paginator.page(1)
    except EmptyPage:
        pro = paginator.page(paginator.num_pages)

    context = {
        'projects': pro,
        'cv': cv,
        'page': page
    }
    return render(request, 'project_index.html', context)


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(
                fh.read(), content_type="application/adminupload")
            response['Content-Disposition'] = 'inline;filename=' + \
                os.path.basename(file_path)
            return response
    raise Http404


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
