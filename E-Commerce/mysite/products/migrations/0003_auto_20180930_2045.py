# Generated by Django 2.0.5 on 2018-09-30 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20180930_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('stock', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('available', models.BooleanField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterIndexTogether(
            name='products',
            index_together=set(),
        ),
        migrations.RemoveField(
            model_name='products',
            name='category',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Products',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Category'),
        ),
    ]