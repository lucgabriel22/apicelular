from django.db import models

class BaseModel(models.Model):
    criacao = models.DateTimeField(
    auto_now=True
    )
    atualizacao = models.DateTimeField(
    auto_now=True
    )
    ativo = models.BooleanField(
    default=True
    )

    class Meta:
        abstract = True

class CelularesBase(BaseModel):
    marca = models.CharField(
        max_length=100
    )
    modelo = models.CharField(
        max_length=100
    )

    ano = models.IntegerField() 

    preco = models.CharField(
        null=False,
        blank=True,
        max_length=6
    )    # caso usuário não souber o valor do celular a IA faz uma validação de preço no google

    class Meta:
        verbose_name = 'Celular'
        verbose_name_plural = 'Celulares'
        ordering = ['ano']

    def __str__(self):
        return f'{self.modelo}'

class Avaliacao(BaseModel):
    celular = models.ForeignKey(
        CelularesBase,
        related_name='avaliacoes',
        on_delete=models.CASCADE,
    )
    nome = models.CharField(
        max_length=150
    )

    email = models.EmailField()

    comentario = models.TextField(
        blank=True,
        default=''
    )

    avaliacao = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        
    )

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['celular', 'email']

    def __str__(self) -> str:
        return f'{self.celular} avaliado por {self.nome} com {self.avaliacao}'
