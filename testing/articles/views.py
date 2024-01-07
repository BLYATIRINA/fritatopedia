from django.shortcuts import render
from .models import Articles
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.db.models import Q
from PIL import Image

def index(request):
    news = Articles.objects.all()
    search_query = request.GET.get('search', None)
    if search_query:
        news = Articles.objects.filter(
            Q(title__iregex=search_query)
        )
    def size_of_image(url):
        im = Image.open(url)
        width, height = im.size
        height //= width // 200
        return height

    return render(request, 'articles/index.html', {'news': news,
                                                                       'size_of_image': size_of_image})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'articles/details_view.html'
    context_object_name = 'article'


