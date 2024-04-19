from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    pontos = models.IntegerField(default=0) 
    nivel_de_experiencia = models.IntegerField(default=0)

    def __str__(self):
        return self.nome    

from django.conf import settings

class UserPoints(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    points = models.IntegerField(default=0)
    
class InputLog(models.Model):
    input_id = models.AutoField(primary_key=True)
    
    # Documento em questao
    doc_id = models.ForeignKey('Document', on_delete=models.CASCADE)
    # Usuario responsavel pela resposta
    user_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    # Tipo de dado enviado (Titulo: 0 , Data: 1, Ambito e Conteudo: 2, Pontos de indexacao: 3)
    input_type = models.IntegerField(default=None)
    # Conteudo enviado
    input_content = models.TextField()

class Document(models.Model):
    doc = models.FileField()
    doc_id = models.CharField(max_length=100, primary_key=True)
    doc_type = models.IntegerField(max_length=100) # Audiovisual: 0, Cartografico: 1, Iconografico: 2, Sonoro: 3, Textual: 4
    doc_ambt_cont = models.TextField(blank=True) # Texto de descricao
    doc_date = models.CharField(max_length=30, blank=True) # Data do documento
    doc_title = models.CharField(max_length=200, null=True, blank=True) # Titulo do documento
    doc_pontos_index = models.IntegerField(default=0, blank=True) # (vocab_controlado) Pontos de acesso e indexação de assuntos do documento
