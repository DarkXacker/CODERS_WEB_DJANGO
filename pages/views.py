from django.shortcuts import get_object_or_404, render
from django.views.generic import *
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from hitcount.views import HitCountDetailView

# Create your views here.

def LikeView(request, pk):
    post = get_object_or_404(Article, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))

class HomePageView(TemplateView):
    template_name = 'home.html'

def ArticleListView(request):
    if 'q' in request.GET:
        q = request.GET['q']
        article = Article.objects.filter(title__icontains=q)

    else:
        article = Article.objects.all()

    context = {
        'article': article,
    }

    return render(request, 'articles/article_list.html', context)

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'articles/article_create.html'

    fields = ('title', 'body', 'image')

class ArticleDetailView(HitCountDetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    count_hit = True

    def post(self, request, *args, **kwargs):
        new_comment = BlogComment(content = request.POST.get('content'), 
            author = self.request.user, blogpost_connected = self.get_object()
        )
        new_comment.save()
        
        return self.get(self, request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Article, id=self.kwargs['pk'])
        total_likes = stuff.likes.count()
        context['total_likes'] = total_likes
        
        data = super().get_context_data(**kwargs)

        comments_connected = BlogComment.objects.filter(
            blogpost_connected = self.get_object()).order_by('-date_posted')
        
        data['comments'] = comments_connected
        
        if self.request.user.is_authenticated:
            data['comment_form'] = NewCommentForm(instance = self.request.user)
        
        context.update(data)
        return context

class ArticleEditView(UpdateView):
    model = Article
    template_name = 'articles/article_edit.html'

    fields = ('title', 'body', 'image')

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('article')