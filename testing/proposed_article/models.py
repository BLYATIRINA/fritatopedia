from django.db import models

class proposedArticles(models.Model):
    id = models.AutoField('id', auto_created=True, primary_key=True, serialize=False)
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')


    def __str__(self):
        return self.title

    class Meta:

        verbose_name = 'Предложенная статья'
        verbose_name_plural = 'Предложенные статьи'
# Create your models here.
