from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm


@permission_required("articles.can_create", raise_exception=True)
def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect("article_detail", article.id)
    else:
        form = ArticleForm()

    return render(request, "articles/create.html", {"form": form})
@permission_required("articles.can_edit", raise_exception=True)
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("article_detail", article.id)
    else:
        form = ArticleForm(instance=article)

    return render(request, "articles/edit.html", {"form": form})
@permission_required("articles.can_delete", raise_exception=True)
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == "POST":
        article.delete()
        return redirect("article_list")

    return render(request, "articles/delete.html", {"article": article})
@permission_required("articles.can_view", raise_exception=True)
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, "articles/detail.html", {"article": article})
