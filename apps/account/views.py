from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserCreationForm, ProfileForm
from .models import Profile
from apps.post.models import Post


class CreateUser(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('post:post_list')

    def post(self, request, *args, **kwargs):
        self.object = None
        return super().post(request, *args, **kwargs)

@login_required()
def ProfileDetailView(request):
    posts = Post.objects.filter(author=request.user)
    profile = Profile.objects.get(user=request.user)
    return render(request, "profile/profile.html", {"profile": profile, "posts": posts})


@login_required
def edit_profile(request, slug):

    try:
        profile = Profile.objects.get(user=request.user)
    except Exception as e:
        return render(request, 'profile/not_found.html')

    if not request.user.slug == slug:
        return redirect("account:login")

    profile_form = ProfileForm(
        request.POST or None, request.FILES or None, instance=profile)

    if request.method == 'POST':
        if profile_form.is_valid():
            profile_form.save()
            messages.add_message(request, messages.SUCCESS, "Perfil editado com sucesso")
            return redirect("account:profile-detail-view")
   
    return render(request, 'profile/edit.html', {'profile_form': profile_form})
