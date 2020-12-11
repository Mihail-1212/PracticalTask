import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from . import models # Task
from . import forms


class IndexView(LoginRequiredMixin, generic.View):
    """
    View with calendar as content
    """
    def get(self, request):
        form_task_update = forms.TaskEditForm
        return render(request, 'webdiary/index.html', context={
            'form_task_update': form_task_update,
        })


class TaskListView(LoginRequiredMixin, generic.ListView):
    """
    View, that works with the user's task list
    """
    models = models.Task
    context_object_name = 'tasks'
    template_name = 'webdiary/task_list.html'
    paginate_by = 10

    def get_full_queryset(self):
        return self.models.objects.filter(user=self.request.user).order_by('-date_start')

    def get_queryset(self):
        filter_date = self.request.GET.get('date')
        # If non-exist get date param => current date is today
        # else => parse the string to date
        if filter_date is None:
            filter_date = datetime.datetime.now().date()
        else:
            filter_date = datetime.datetime.strptime(filter_date, '%d.%m.%Y')
        return self.get_full_queryset().filter(date_start__date=filter_date)

    def get(self, request, *args, **kwargs):
        """
        Method return full user tasks if was the ajax request else => render
        """
        if request.is_ajax():
            tasks = self.get_full_queryset()
            tasks = list(tasks.values())
            return JsonResponse({
                'tasks': tasks
            })
        try:
            self.get_queryset()
        except Exception:
            return HttpResponseNotFound('Date is incorrect')
        return super(TaskListView, self).get(request, *args, **kwargs)


class TaskAddView(LoginRequiredMixin, generic.CreateView):
    """
    View, that add new task for user
    """
    models = models.Task
    form_class = forms.TaskEditForm
    template_name = 'webdiary/task_edit.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super().form_valid(form)


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    """
    View, that shows the user's task
    """
    models = models.Task
    template_name = 'webdiary/task_detail.html'
    context_object_name = 'task'
    pk_url_kwarg = 'task_id'

    def get_queryset(self):
        return self.models.objects.filter(user=self.request.user).order_by('-date_start')


class TaskEditView(LoginRequiredMixin, generic.UpdateView):
    """
    View, that edits the user's task
    """
    models = models.Task
    pk_url_kwarg = 'task_id'
    form_class = forms.TaskEditForm
    template_name = 'webdiary/task_edit.html'
    success_url = reverse_lazy('index')

    def get_queryset(self):
        return self.models.objects.filter(user=self.request.user).order_by('-date_start')

    def update_by_get(self, request) -> bool:
        """
        Method update object (by get params status) and return true if isset get parameter 'status' and its available
        else => return False
        """
        task = self.get_object()
        new_status = request.GET.get('status')
        if not new_status is None:
            if not new_status in models.Task.AVAILABLE_STATUSES:
                return HttpResponseNotFound('Status is not available')
            task.status = new_status
            task.save()
            if request.is_ajax():
                return JsonResponse({
                    'task': task
                })
            return True
        return False


    def get(self, request, *args, **kwargs):
        if request.GET:
            if self.update_by_get(request):
                # return to prev page
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            else:
                return HttpResponseNotFound('Get parameter is not available')
        return super(TaskEditView, self).get(request, *args, **kwargs)
