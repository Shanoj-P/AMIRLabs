from django.shortcuts import render, redirect
from django.utils.text import slugify

from .form import ProjectForm
from .models import Project, Comment

def feed(request):
    project = reversed(Project.objects.all())

    return render(request, 'feeds.html', {'project': project, 'page': 'feed'})

def showCmt(request,slug):
    try:
        project = Project.objects.all
        projectid = Project.objects.get(slug=slug)
        cmmt = Comment.objects.all().filter(project=projectid)
    except Exception as e:
        raise e
    return render(request, 'feeds.html', {'project': project, 'cmmt': cmmt, 'page': 'feed', 'projectid': projectid})


def addCmt(request, id):
    print('urlllllllllll')
    project = Project.objects.all
    projectid = Project.objects.get(id=id)
    if request.method == 'POST':
        projectid = projectid
        cmt = request.POST['comment']
        owner = request.user

        comment = Comment(project=projectid, cmt=cmt,owner=owner)
        comment.save()
    cmmt = Comment.objects.all().filter(project=projectid)
    return render(request, 'feeds.html', {'project': project, 'cmmt': cmmt, 'page': 'feed', 'projectid': projectid})


def profile(request):
    projectid = Project.objects.all().filter(author=request.user)
    return render(request, 'profile page.html', {'page': 'profile', 'projects':projectid})

def add(request):

    return render(request, 'add.html', {'page': 'add'})

def addProject(request):
    if request.method == 'POST':
        title = request.POST['Title']
        desc = request.POST['description']
        img = request.FILES['img']
        author = request.user
        slug = slugify(title)

        project = Project(title=title, desc=desc, images=img, author=author, slug=slug)
        project.save()
    projectid = Project.objects.all().filter(author=request.user)
    return render(request, 'profile page.html', {'page': 'profile', 'projects': projectid})