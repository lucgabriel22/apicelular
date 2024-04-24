from django.db import models

class CelularesBase(models.Model):
    marca = models.CharField(
    max_length=100
    )
    modelo = models.CharField(
    max_length=100
    )

    ano = models.IntegerField() 

    preco = models.PriceField()        # caso usuário não souber o valor do celular a IA faz uma validação de preço no google

    class Meta:
        verbose_name = 'Celular'
        verbose_name_plural = 'Celulares'
        ordering = ['ano']

class Avaliacao(CelularesBase):
    celular = models.ForeignKey(
        CelularesBase,
        on_delete=models.CASCADE
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

    avaliacao = models.DecimalField(
        max_digits=2,
        decimal_places=1,
    )

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliacões'
        unique_together = ['celular', 'email']

        def __str__(self) -> str:
            return f'{self.celular} avaliado por {self.nome} com {self.avaliacao}'
