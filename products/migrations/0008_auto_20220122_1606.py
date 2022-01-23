# Generated by Django 3.2.9 on 2022-01-22 12:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0007_auto_20220101_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=200)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('publish_status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], default='p', max_length=15)),
            ],
            options={
                'ordering': ['-publish'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='authentication.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.brand'),
        ),
    ]
