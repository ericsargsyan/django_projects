from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Task
from .forms import CreateTaskForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


@login_required
def all_tasks(request):
    admin_user = get_object_or_404(User, pk=request.user.id)
    if admin_user.is_superuser:
        tasks = Task.objects.all()
    #     return JsonResponse(str(tasks), safe=False)
    # else:
    #     return JsonResponse("Bad resposne",safe=False)
    context = {'tasks': tasks}
    return render(request, 'to_do/home.html', context)


# @login_required
# def home(request):
#     tasks = Task.objects.all().filter(user=request.user.id)
#     context = {'tasks': tasks}
#     return render(request, 'to_do/home.html', context)


# class MyView(View):
#     queryset = None
#
#     def set_queryset(self):
#         self.queryset = Task.objects.all().filter(user=self.request.user.id)
#
#     def get(self):
#         # tasks = Task.objects.all().filter(user=self.request.user.id)
#         self.set_queryset()
#         tasks = self.queryset
#         context = {'tasks': tasks}
#         return render(self.request, 'to_do/home.html', context)
#
#     def post(self):


class HomeView(LoginRequiredMixin, ListView):
    template_name = 'to_do/home.html'
    model = Task
    paginate_by = 3

    def get_queryset(self):
        return self.model.objects.all().filter(user=self.request.user)


class TaskView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "to_do/task_view.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context['data'] = "Hello world!"
        context['data1'] = "A"
        return context


# @login_required
# def taskview(request, pk):
#     special_task = get_object_or_404(Task, pk=pk, user=request.user.id)
#     return render(request, "to_do/task_view.html", {'task': special_task})


@login_required
def newtask(request):
    form = CreateTaskForm()
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = get_object_or_404(User, pk=request.user.id)
            task.save()
            messages.success(request, "The task is created successfully")
            return redirect('home')
        else:
            messages.error(request, "The task is created successfully")
    return render(request, "to_do/new_task.html", {'form': form})


class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    form_class = CreateTaskForm
    template_name = "to_do/new_task.html"
    success_url = "/"

    # def get_success_url(self):
    #     print(reverse("home"), "@@@@@@@@@@")
    #     return reverse("home")

    # def post(self, request, *args, **kwargs):
    #
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         task = form.save(commit=False)
    #         task.user = get_object_or_404(User, pk=request.user.id)
    #         task.save()
    #         messages.success(request, "The task is created successfully")
    #         return redirect(self.success_url)

@login_required
def taskupdate(request, pk):
    if request.user.is_superuser:
        task = Task.objects.get(id=pk)
    else:
        task = Task.objects.get(id=pk, user=request.user.id)

    # task = Task.objects.get(id=pk, user=request.user.id)
    form = CreateTaskForm(instance=task)

    if request.method == 'POST':
        form = CreateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task was updated")
            return redirect("TaskView", pk=pk)

    return render(request, "to_do/task_update.html", {'form': form})


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = CreateTaskForm
    template_name = "to_do/task_update.html"

    def get_success_url(self):
        return reverse("Home")

    # url id instead of pk
    # def get_object(self, queryset=None):
    #     task_id = self.kwargs.get("id")
    #     return get_object_or_404(Task, id=task_id)

@login_required
def taskdelete(request, pk):
    task_to_delete = get_object_or_404(Task, pk=pk, user=request.user.id)
    task_to_delete.delete()
    messages.success(request, "Task was deleted")
    return redirect("home")
