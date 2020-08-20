from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import RegisterForm,UserUpdateForm,ProfileUpdateForm,RatingsForm
from  django.http import HttpResponseRedirect,HttpResponse,Http404
from django.contrib.auth.models import User
from .models import Profile,Project,Rating
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserSerializer,ProjectSerializer,RatingSerializer


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


@login_required(login_url='/accounts/login/')
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


@login_required(login_url='/accounts/login/')
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


def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_project = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "projects": searched_project})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})


@login_required(login_url='/accounts/login/')
def site(request, site_id):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user).first()

    try:
        post = Project.objects.get(id=site_id)
    except:
        raise ObjectDoesNotExist()

    try:
        ratings = Rating.objects.filter(project_id=site_id)
        design = Rating.objects.filter(
            project_id=site_id).values_list('design', flat=True)
        usability = Rating.objects.filter(
            project_id=site_id).values_list('usability', flat=True)
        creativity = Rating.objects.filter(
            project_id=site_id).values_list('creativity', flat=True)
        content = Rating.objects.filter(
            project_id=site_id).values_list('content', flat=True)
        total_design = 0
        total_usability = 0
        total_creativity = 0
        total_content = 0

        for rate in design:
            total_design += rate

        for rate in usability:
            total_usability += rate

        for rate in creativity:
            total_creativity += rate

        for rate in content:
            total_content += rate

        overall_score = (total_design+total_content +
                         total_usability+total_creativity)/4

        post.design = total_design
        post.usability = total_usability
        post.creativity = total_creativity
        post.content = total_content
        post.overall_score = overall_score

        post.save()

    except:
        return None

    if request.method == 'POST':
        form = RatingsForm(request.POST, request.FILES)
        if forms.is_valid():
            rating = form.save(commit=False)
            rating.post = post
            rating.profile = profile
            rating.overall_score = (
                rating.design+rating.usability+rating.creativity+rating.content)/2
            rating.save()
    else:
        form = RatingsForm()

    return render(request, "site.html", {"post": post, "profile": profile, "ratings": ratings, "form": form}(request))


class UserList(APIView):
    def get(self, request, format=None):
        all_user = User.objects.all()
        serializers = UserSerializer(all_user, many=True)
        return Response(serializers.data)


class ProjectList(APIView):
    def get(self, request, format=None):
        all_project = Project.objects.all()
        serializers = ProjectSerializer(all_project, many=True)
        return Response(serializers.data)


class RatingList(APIView):
    def get(self, request, format=None):
        all_rating = Rating.objects.all()
        serializers = RatingSerializer(all_rating, many=True)
        return Response(serializers.data)
