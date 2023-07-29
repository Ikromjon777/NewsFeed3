from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView, CreateView
from hitcount.models import HitCount

from .forms import ContactForm, CommentForm
from .models import Category, News, Foto
from hitcount.views import HitCountMixin

# Create your views here.
from .mixin import Mixin
class NewsView(View):
    def get(self, request):
        #news_list = News.objects.filter(status=News.Status.Published)
        news_list = News.published.all()
        context = {
            "news_list":news_list,
        }
        return render(request, "news/news_list.html", context=context)

class NewsDetailView(View):
    def get(self, request, id):
        news = get_object_or_404(News, id=id, status=News.Status.Published)
        context = {
            "news":news,
        }
        return render(request, "news/news_detail.html", context=context)

class HomePageView(View):
    def get(self, request):
        latest_news = News.published.all().order_by('-publish_time')[:10]
        latest_news2 = News.published.all().order_by('-publish_time')[:5]
        mahalliy = News.published.filter(category__name='Mahalliy')[:1]
        mahalliy_news = News.published.filter(category__name='Mahalliy').order_by('-publish_time')[1:5]
        xorij = News.published.filter(category__name='Xorij')[:1]
        xorij_news = News.published.filter(category__name='Xorij').order_by('-publish_time')[1:5]
        texnologiya = News.published.filter(category__name='Texnologiya')[:1]
        texnologiya_news = News.published.filter(category__name='Texnologiya').order_by('-publish_time')[1:5]
        sport = News.published.filter(category__name='Sport')[:1]
        sport_news = News.published.filter(category__name='Sport').order_by('-publish_time')[1:5]
        siyosat_news = News.published.filter(category__name='Siyosat').order_by('-publish_time')[:4]
        fotos = Foto.objects.all()[:6]
        news = News.published.all()[6:12]
        category = Category.objects.all()


        context = {
            "latest_news":latest_news,
            "category":category,
            "news":news,
            "latest_news2":latest_news2,
            "mahalliy_news":mahalliy_news,
            "mahalliy":mahalliy,
            "xorij":xorij,
            "xorij_news":xorij_news,
            "texnologiya":texnologiya,
            "texnologiya_news":texnologiya_news,
            'fotos':fotos,
            "sport":sport,
            "sport_news":sport_news,
            "siyosat_news":siyosat_news,
        }
        return render(request, "news/home.html", context=context)

class ContactView(View):
    def get(self, request):
        context = {

        }
        return render(request, 'news/contact.html', context=context)
    def post(self, request):
        form = ContactForm(data=request.POST)
        context = {
            "form":form,
        }
        if form.is_valid():
            form.save()
            return render(request, 'news/contact_post.html', context=context)
        else:
            return render(request, 'news/contact.html', context=context)
class Pages404View(View):
    def get(self, request):
        context = {

        }
        return render(request, 'news/404.html', context=context)

class Contact_postView(View):
    def get(self, request):
        context = {

        }
        return render(request, 'news/contact_post.html', context=context)

class Single_pageView(View):

    def get(self, request, news):
        news = get_object_or_404(News, slug=news, status=News.Status.Published)
        comments = news.comments.filter(activate=True)
        comment_form = CommentForm()
        category = news.category
        newss = News.published.all().filter(category__name=category).order_by('-publish_time')[1:4]

        # view count
        hit_count = HitCount.objects.get_for_object(news)
        HitCountMixin.hit_count(request, hit_count)

        context = {
            "news":news,
            "newss":newss,
            "comments":comments,
            "comment_form":comment_form,
        }
        return render(request, "news/single_page.html", context=context)
    def post(self, request, news):
        news = get_object_or_404(News, slug=news, status=News.Status.Published)
        category = news.category
        newss = News.published.all().filter(category__name=category).order_by('-publish_time')[1:6]
        comment_form = CommentForm(data=request.POST)
        comments = news.comments.filter(activate=True)
        # new_comment = None
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            # commit=False qilganimiz to'g'ridan to'g'ri ma'lumotlar bazasiga saqlamaydi
            new_comment.news = news
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
            context = {
                "news":news,
                "comment_form":comment_form,
                "newss": newss,
                "comments": comments,
            }
            return render(request, "news/single_page.html", context=context)


class MahalliyView(View):
    def get(self, request):
        news = News.published.filter(category__name='Mahalliy').order_by('-publish_time')
        context = {
            "news":news,
        }
        return render(request, "news/mahalliy.html", context=context)

class XorijView(View):
    def get(self, request):
        news = News.published.filter(category__name='Xorij').order_by('-publish_time')
        context = {
            "news":news,
        }
        return render(request, "news/xorij.html", context=context)

class SportView(View):
    def get(self, request):
        news = News.published.filter(category__name='Sport').order_by('-publish_time')
        context = {
            "news":news,
        }
        return render(request, "news/sport.html", context=context)

class SiyosatView(View):
    def get(self, request):
        news = News.published.filter(category__name='Siyosat').order_by('-publish_time')
        context = {
            "news":news,
        }
        return render(request, "news/siyosat.html", context=context)

class TexnologiyaView(View):
    def get(self, request):
        news = News.published.filter(category__name='Texnologiya').order_by('-publish_time')
        context = {
            "news":news,
        }
        return render(request, "news/texnologiya.html", context=context)

class UpdateNewsView(Mixin,UpdateView):
    model = News
    fields = ("title", "body", "image", "category", "status")
    template_name = "conf/update.html"
    success_url = reverse_lazy('home_page')

class DeleteNewsView(Mixin,DeleteView):
    model = News
    template_name = 'conf/delete.html'
    success_url = reverse_lazy('home_page')

class CreateNewsView(Mixin,CreateView):
    model = News
    template_name = 'conf/create.html'
    fields = ('title','slug', 'body', 'image', 'category', 'status')
    success_url = reverse_lazy('news_detail')



class SerachView(View):
    def get(self, request):
        news_all = News.published.all()
        search_query = request.GET.get('q')
        # bir nechta filter ishlatishimiz uchun Q() dan foydalanmiz
        news = news_all.filter(
            Q(title__icontains=search_query)|Q(body__icontains=search_query)
        )
        context = {
            'news':news,
           }
        return render(request, 'news/search.html', context=context)