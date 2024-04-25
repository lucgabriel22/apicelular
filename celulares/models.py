from django.db import models

class CelularesBase(models.Model):
    marca = models.CharField(
    max_length=100
    )
    modelo = models.CharField(
    max_length=100
    )

    ano = models.IntegerField() 

    preco = models.CharField(
        null=True,
        blank=False,
        max_length=6,
        default='',
    )    # caso usuário não souber o valor do celular a IA faz uma validação de preço no google

    class Meta:
        verbose_name = 'Celular'
        verbose_name_plural = 'Celulares'
        ordering = ['ano']

        def __str__(self) -> str:
            return f'{self.modelo}'

class Avaliacao(CelularesBase):
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
        null=True,
        blank=False,
        default=''
    )

    avaliacaonum = models.DecimalField(
        max_digits=2,
        decimal_places=1,
    )

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['celular', 'email']

        def __str__(self) -> str:
            return f'{self.celular} avaliado por {self.nome} com {self.avaliacao}'
