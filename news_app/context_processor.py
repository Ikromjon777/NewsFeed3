from .models import News, Category

def latest_news(request):
    latest_news = News.published.all().order_by('-publish_time')[:10]
    latest_news2 = News.published.all().order_by('-publish_time')[:5]
    sport_news = News.published.filter(category__name='Sport').order_by('-publish_time')[1:5]
    category = Category.objects.all()
    context ={
        "latest_news":latest_news,
        "latest_news2":latest_news2,
        "category":category,
        "sport_news":sport_news,
    }
    return context