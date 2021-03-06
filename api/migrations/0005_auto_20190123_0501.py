# Generated by Django 2.0.7 on 2019-01-23 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190122_1702'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='promoimage',
            options={'verbose_name_plural': 'Promo Images'},
        ),
        migrations.AlterModelOptions(
            name='reviewcomment',
            options={'verbose_name_plural': 'Review Comments'},
        ),
        migrations.AddField(
            model_name='transaction',
            name='confirmation_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='reviewcomment',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_comments', to='api.Item'),
        ),
    ]
