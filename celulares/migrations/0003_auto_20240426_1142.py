# Generated by Django 2.2.9 on 2024-04-26 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celulares', '0002_auto_20240425_0837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliacao',
            name='celularesbase_ptr',
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='atualizacao',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='criacao',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='celularesbase',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='celularesbase',
            name='atualizacao',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='celularesbase',
            name='criacao',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='comentario',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='celularesbase',
            name='preco',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]
