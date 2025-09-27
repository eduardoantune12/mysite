from django.db import models
from django.contrib.auth.models import User


STATUS = (
	(0, 'Draft'),
	(1, 'Published')
)


class Post(models.Model):

    #Titulo do Post
    #Charfield = Campo que aceita texto (max_length obrigatório)
    title = models.CharField(max_length=200, unique=True)

    #Identificação do Post
    #SlugField = Campo que aceita texto (feito para URLs)
    slug = models.SlugField(max_length=200, unique=True)

    #Author relaciona o post com o usuário específico
    #ForeignKey = Chave estrangeira usada para relacionamentos de tabelas e os seus dados
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')

    #Quando o Post foi atualizado
    #DateTimeField = Campo que armazena e mostra a data e a hora
    updated_on = models.DateTimeField(auto_now=True)

    #Conteúdo do Post, escrita
    #TextField = Campo de texto especial do Django, maior
    content = models.TextField()

    #Quando foi criado
    #DateTimeField = Campo que armazena e mostra a data e a hora
    created_on = models.DateTimeField(auto_now_add=True)

    #Status do artigo (rascunho, publicado)
    #IntegerField = Campo que recebe números inteiros
    #choices = inicia como 0 "Draft" e irá se alterar conforme as mudanças nos campos acima pelo usuário
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:

        #Forma como ele irá ordenar os objetos (created_on indica ordem decrescente)
        ordering = ['-created_on']

    def __str__(self):
        return self.title