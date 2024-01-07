from .models import proposedArticles
from django.forms import ModelForm, TextInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = proposedArticles
        fields = ['title', 'anons', 'full_text']

        widgets = {
            'title': TextInput(attrs={'class': 'form-contol',
                                      'placeholder': 'Заголовок'}),
            'anons': TextInput(attrs={'class': 'form-contol',
                                      'placeholder': 'Анонс'}),
            'full_text': Textarea(attrs={'class': 'form-contol',
                                         'placeholder': 'Основной текст'})
        }