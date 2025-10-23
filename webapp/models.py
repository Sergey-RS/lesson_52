from django.db import models

# описание модели базы данных

class Article(models.Model):
    title = models.CharField(max_length=50,
                             null=False, blank=False,
                             verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')
    author = models.CharField(max_length=50,default='Anonymous',verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='дата создания')
    update_at = models.DateTimeField(auto_now_add=True, verbose_name='дата обновления')

    def __str__(self):
        return  f'{self.id} - {self.title}'
