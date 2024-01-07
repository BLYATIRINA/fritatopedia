from django.shortcuts import render
from .models import proposedArticles
from .forms import ArticlesForm

# Create your views here.


def index(request):
    message = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'Форма была отправлена на рассмотрение'
        else:
            message = 'Форма была неверной'
    form = ArticlesForm()

    data = {
        'form': form,
        'error': message
    }

    return render(request, 'proposed_article/form.html', data)