from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Project, Task, Tag, TaskList
from .forms import ProjectForm, TaskForm


@login_required
def project_list(request):
    projects = Project.objects.filter(owner=request.user)
    return render(request, 'projects/project_list.html', {'projects': projects})


@login_required
def dashboard(request):
    projects = Project.objects.filter(owner=request.user)
    return render(request, 'projects/dashboard.html', {'projects': projects})


@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})


@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect('dashboard')
    else:
        form = ProjectForm()
    return render(request, 'projects/create_project.html', {'form': form})


@login_required
@require_POST
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    project.delete()
    return redirect('project_list')


@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    tasks = Task.objects.filter(project=project)
    return render(request, 'projects/project_detail.html', {'project': project, 'tasks': tasks})


@login_required
def task_create(request, project_id):
    project = get_object_or_404(Project, id=project_id, owner=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        form.fields['list'].queryset = TaskList.objects.filter(project=project)
        form.fields['tags'].queryset = Tag.objects.all()

        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.owner = request.user
            task.save()
            form.save_m2m()
            return redirect('project_detail', pk=project.id)
    else:
        form = TaskForm()
        form.fields['list'].queryset = TaskList.objects.filter(project=project)
        form.fields['tags'].queryset = Tag.objects.all()

    return render(request, 'projects/task_form.html', {'form': form, 'project': project})


@login_required
def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id, project__owner=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=task.project.id)
    else:
        form = TaskForm(instance=task)
        form.fields['list'].queryset = TaskList.objects.filter(project=task.project)
        form.fields['tags'].queryset = Tag.objects.all()

    return render(request, 'projects/task_form.html', {'form': form, 'project': task.project})


@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, project__owner=request.user)
    project_id = task.project.id
    if request.method == 'POST':
        task.delete()
        return redirect('project_detail', pk=project_id)
    return render(request, 'projects/task_confirm_delete.html', {'task': task})


@login_required
def task_update_status(request, task_id):
    task = get_object_or_404(Task, id=task_id, project__owner=request.user)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Task.PRIORITY_CHOICES):
            task.status = new_status
            task.save()
    return redirect('project_detail', pk=task.project.id)
