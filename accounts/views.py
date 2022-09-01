from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserChangeForm
from pages.models import Article
from .models import *

@login_required(login_url='/auth/login/')
def userProfileEditView(request):
	if request.method == 'POST':
		form = CustomUserChangeForm(request.POST, instance=request.user, files=request.FILES)
		if form.is_valid():
			form.save()
			return redirect('profile', username=request.user.username)
	else:
		form = CustomUserChangeForm(instance=request.user)

	return render(request, 'account/edit_profile.html', {'form': form, 'user': request.user})


def userProfileView(request, username):
	user = get_object_or_404(CustomUser, username=username)
	posts_count = Article.objects.filter(author=user).count()

	return render(request, 'account/profile.html', {'user_model': user, 'posts_count': posts_count})


class SignUpView(CreateView):
	form_class = CustomUserCreationForm
	template_name = 'registration/signup.html'
	
	def form_valid(self, form):
		form.save()
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password1')
		user = authenticate(username=username, password=password)
		login(self.request, user)
		return redirect('home')