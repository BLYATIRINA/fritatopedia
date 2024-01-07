from django.db import models


class Articles(models.Model):
    id = models.AutoField('id', auto_created=True, primary_key=True, serialize=False)
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публицкации')
    # popularity = models.IntegerField('Количество')
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
# Create your models here.
