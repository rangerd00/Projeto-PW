from django.db import models


class Post(models.Model):
    autor = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=500)
    link = models.URLField(max_length=200, blank=True)

    def str(self):
        return f"{self.autor} no {self.data}, adicionou um {self.titulo} com a{self.descricao} e link {self.link}"


class Quizz(models.Model):
    nome = models.CharField(max_length=50)

    pergunta1 = models.CharField(max_length=50)

    pergunta2 = models.CharField(max_length=50)

    pergunta3 = models.CharField(max_length=50)

    pergunta4 = models.CharField(max_length=50)

    pergunta5 = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome}"


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    linkedin = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.nome}"


class Noticias(models.Model):
    titulo = models.CharField(max_length=500)
    descricao = models.CharField(max_length=5000)
    link = models.URLField(max_length=200, blank=True)
    imagem = models.ImageField(upload_to='media/', null=True)

    def __str__(self):
        return f"{self.titulo}"


class Projetos(models.Model):
    titulo = models.CharField(max_length=200)

    descricao = models.CharField(max_length=500)

    participantes = models.ManyToManyField(Pessoa, blank=True)

    tecnologias = models.CharField(max_length=100)

    github = models.URLField(max_length=200, blank=True)

    ano = models.IntegerField(default=0)

    imagem = models.ImageField(upload_to='media/', null=True)

    def __str__(self):
        return f"{self.titulo}"


class UnidadesCurriculares(models.Model):
    titulo = models.CharField(max_length=200)
    ano = models.IntegerField(default=0)
    semestre = models.CharField(max_length=200, blank=True)
    topicos = models.CharField(max_length=2000, blank=True)
    professores = models.ManyToManyField(Pessoa, blank=True)
    linkUC = models.URLField(max_length=200, blank=True)
    projetos = models.ManyToManyField(Projetos, blank=True)

    def __str__(self):
        return f"{self.titulo}"


class Tecnologias(models.Model):
    nome = models.CharField(max_length=200)
    acronimo = models.CharField(max_length=200, blank=True)
    ano = models.IntegerField(default=0)
    criador = models.CharField(max_length=200, blank=True)
    logotipo = models.ImageField(upload_to='media/', null=True)
    link = models.URLField(max_length=200, blank=True)
    caracteristicas = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nome}"


class Padroes(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=500, blank=True)
    imagem = models.ImageField(upload_to='media/', null=True)
    link = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.nome}"


class Tecnicas(models.Model):
    nome = models.CharField(max_length=200)
    link = models.URLField(max_length=200, blank=True)
    imagem = models.ImageField(upload_to='media/', null=True)


class TrabalhosFinaisCurso(models.Model):
    autores = models.CharField(max_length=200)
    orientadores = models.CharField(max_length=200)
    ano = models.IntegerField(default=0)
    titulo = models.CharField(max_length=200)
    resumo = models.CharField(max_length=500)
    imagem = models.ImageField(upload_to='media/', null=True)
    relatorio = models.CharField(max_length=1000)
    github = models.URLField(max_length=200, blank=True)
    video = models.URLField(max_length=200, blank=True)
