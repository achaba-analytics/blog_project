from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views import generic

#def home(request):
 # template = loader.get_template('home.html')
#  return HttpResponse(template.render())

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-pub_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

class ArticleView(DetailView):
    model = Post
    template_name = 'articles.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleView, self).get_context_data(*args, **kwargs)
        
        test = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = test.total_likes()
        liked = False
        if test.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['liked'] = liked
        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context
    

class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats':cats, 'category_posts':category_posts})

class UpdateView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update.html'
    #fields = ['title', 'title_tag', 'body']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UpdateView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    

#def DeletePost(request, pk):
    #post = Post.objects.get(id=pk)
    #if request.method == 'POST':
        #post.delete()
        #return redirect('home')
     
class AddPostView(CreateView):

        model = Post
        form_class = PostForm
        template_name = 'add_post.html'

def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
    
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))
