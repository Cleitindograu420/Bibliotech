from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=150)

class Editora(models.Model):
    nome = models.CharField(max_length=150)

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, help_text="13 caracteres", unique=True)
    genero = models.CharField(max_length=50)
    data_publicacao = models.DateField()
    