# Generated by Django 2.1.7 on 2019-02-14 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoppinglist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('shoppinglist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppinglist.ShoppingList')),
            ],
        ),
    ]
