from django.urls import path
from .views import NewsView, NewsDetailView, HomePageView, ContactView,\
    Pages404View, Contact_postView, Single_pageView, MahalliyView,\
    TexnologiyaView, SportView, SiyosatView, XorijView, UpdateNewsView, DeleteNewsView, CreateNewsView,\
    SerachView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('contact/', ContactView.as_view(), name='contact_page'),
    path('not_page/', Pages404View.as_view(), name='404_page'),
    path('contact/free/', Contact_postView.as_view(), name='contact_post'),
    path('all/', NewsView.as_view(), name='news_list'),
    path('news/<slug:news>/', Single_pageView.as_view(), name='news_detail'),
    path('mahalliy/', MahalliyView.as_view(), name='mahalliy_page'),
    path('sport/', SportView.as_view(), name='sport_page'),
    path('texnologiya/', TexnologiyaView.as_view(), name='texnologiya_page'),
    path('siyosat/', SiyosatView.as_view(), name='siyosat_page'),
    path('xorij/', XorijView.as_view(), name='xorij_page'),
    path('news/<slug>/update/', UpdateNewsView.as_view(), name='update_view'),
    path('news/<slug>/delete/', DeleteNewsView.as_view(), name='delete_view'),
    path('news/create/', CreateNewsView.as_view(), name='create_view'),
    path('search/', SerachView.as_view(), name='search'),
]
