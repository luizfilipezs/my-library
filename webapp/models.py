from django.db import models
import uuid


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    photo = models.FileField(upload_to='photos/authors', null=True)
    name = models.CharField(max_length=255, verbose_name='Nome')
    categories = models.ManyToManyField(Category, verbose_name='Principais categorias')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Adicionado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Criado em')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

class Book(models.Model):
    READING_STATUS_CHOICES = (
        ('unread', 'Não lido'),
        ('reading', 'Lendo'),
        ('read', 'Lido'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cover = models.FileField(upload_to='photos/covers', blank=True, null=True, verbose_name='Capa')
    title = models.CharField(max_length=255, verbose_name='Título')
    authors = models.ManyToManyField(Author, verbose_name='Autor(es)')
    categories = models.ManyToManyField(Category, verbose_name='Categorias')
    reading_status = models.CharField(max_length=20, choices=READING_STATUS_CHOICES, default='unread', verbose_name='Status da leitura')
    last_reading = models.DateField(verbose_name='Data da última leitura (mês)', blank=True, null=True)
    about = models.TextField(verbose_name='Sobre', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Adicionado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Criado em')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Livro'
