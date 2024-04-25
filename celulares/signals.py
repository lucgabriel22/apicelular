from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import CelularesBase
from openai_api import get_preco_celular


@receiver(pre_save, sender=CelularesBase)
def celular_pre_save(sender, instance, **kwargs):
    if not instance.preco:
        ai_preco = get_preco_celular(
        instance.marca,
        instance.modelo,
        instance.ano
    )
        instance.preco = ai_preco