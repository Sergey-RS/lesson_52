from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.template.defaultfilters import title

from webapp.models import Article

from webapp.forms import ArticleForm

from webapp.validation import validate


# Create your views here.

def article_list_view(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request,'article_list.html', context)

def article_detail_view(request,*args, pk, **kwargs):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detail.html', {'article': article})

def article_create_view(request):
    if request.method == 'GET':
        form = ArticleForm()
        return  render(request, 'article_create.html' , {'form': form})
    elif request.method == 'POST':
#        errors = validate(request.POST)
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = Article()
            article.title=form.cleaned_data.get('title')
            article.content=form.cleaned_data.get('content')
            article.author=form.cleaned_data.get('author')
            article.save()
            return redirect('article_detail', pk=article.id)
#        if errors:
        return render(request, 'article_create.html', {'form': form})
#        title=request.POST.get('title')
#        content=request.POST.get('content')
#        author=request.POST.get('author')
#        article=Article.objects.create(title=title, content=content, author=author)
#        article.save()
#        return HttpResponseRedirect(reverse('article_list'))
#        return redirect('article_list')
#        return redirect('article_detail', pk=article.id)

def article_update_view(request, *args, pk, **kwargs):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        form = ArticleForm(initial={'title': article.title, 'content': article.content, 'author': article.author})
        return render(request, 'article_update.html', {'form': form})
    elif request.method == "POST":
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article.title = form.cleaned_data.get('title')
            article.content = form.cleaned_data.get('content')
            article.author = form.cleaned_data.get('author')
            article.save()
            return redirect('article_detail', pk=article.id)
        return render(request, 'article_update.html', {'form': form})

def article_delete_view(request, *args, pk, **kwargs):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        return render(request, 'article_delete.html', {'article': article})
    article.delete()
    return redirect('article_list')