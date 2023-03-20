from django.db import models

class Forms(models.Model):
    SUPERIORES = (
        ('um', 'UFRN'),
        ('dois', 'IFRN'),
        ('tres', 'UNIRN'),
        ('quatro', 'UNP'),
    )
    
    nome = models.CharField(max_length=255)
    nascimento = models.DateField()
    curso = models.CharField(max_length=255)
    instituicao = models.CharField(
        max_length=255,
        choices = SUPERIORES,
    )
    email = models.EmailField()
    celular = models.CharField(max_length=20)
    instagram = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome

