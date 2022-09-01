from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import *
from .models import *
from hitcount.views import HitCountDetailView
from django.http import HttpResponseRedirect

# Create your views here.

def ProgramsListView(request):
        if 'q' in request.GET:
            q = request.GET['q']
            program = Program.objects.filter(title__icontains=q)

        else:
            program = Program.objects.all()

        context = {
            'program': program,
        }

        return render(request, 'programs/programs_list.html', context)


class ProgramsDetailView(HitCountDetailView):
    model = Program
    template_name = 'programs/program_detail.html'
    count_hit = True

    def showvideo(request):

        lastvideo = Program.objects.last()

        videofile = lastvideo.videofile
        
        context = {
            'videofile': videofile,
        }
        
        return render(request, 'programs/program_detail.html', context)

class ProgramsCreateView(CreateView):
    model = Program
    template_name = 'programs/program_create.html'

    fields = ('title', 'body', 'image', 'video', 'document', )
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser ekanini tekshirish
    
    def test_func(self):
        return self.request.user.is_superuser

class ProgramsUpdateView(UpdateView):
    model = Program
    template_name = 'programs/program_update.html'

    fields = ('title', 'body', 'image', 'video', 'document', )
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser ekanini tekshirish
    
    def test_func(self):
        return self.request.user.is_superuser

class ProgramsDeleteView(DeleteView):
    model = Program
    template_name = 'programs/program_delete.html'
    success_url = reverse_lazy('programs_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
