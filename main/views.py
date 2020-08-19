from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import RegisterForm,UserUpdateForm,ProfileUpdateForm
from  django.http import HttpResponseRedirect
# from django.contrib.auth.models import User
from .models import Profile,Project



def index(request):
    photos = Project.objects.all()

    return render(request, 'index.html', {"photos": photos})

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("index")
    else:
        form = RegisterForm()
    return render(response,'registration/register.html',{'form':form})

@login_required
def profile(request,id):
    current_user = request.user
    profile = Profile.get_profile(current_user.id)
    if request.method == 'POST':
        
        p_form = ProfileUpdateForm(request.POST,request.FILES)

        if  p_form.is_valid():
            profile = p_form.save(commit=False)
            profile.user = current_user
            p_form.save()
            messages.success(request, f'Your account has been updated!')
        return HttpResponseRedirect(reverse('profile', args=[str(id)]))

    else:
        
        p_form = ProfileUpdateForm(instance=request.user)

    context = {
        
        'p_form': p_form,
        'profile':profile,
        'current_user': current_user
        
    }

    return render(request, 'profile.html', context)


class PostListView(ListView):
    model = Project
    template_name = 'post.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'projects'
    ordering = ['-pub_date']


class PostDetailView(DetailView):
    model = Project
    template_name = 'post_details.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'projects'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'post_form.html'
    context_object_name = 'projects'
    fields = ['title', 'description', 'image','link']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    template_name = 'post_form.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'projects'
    fields = ['title', 'description','image', 'link']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name = 'post_confirm_delete.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'projects'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
