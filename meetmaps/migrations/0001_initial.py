# Generated by Django 3.1.7 on 2021-03-21 12:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('lat', models.FloatField(blank=True, null=True)),
                ('long', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('birthday', models.DateField()),
                ('bio', models.CharField(default='', max_length=140)),
                ('location_lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('location_long', models.DecimalField(decimal_places=6, max_digits=9)),
                ('avatar', models.ImageField(default='default_profile_picture.png', upload_to='avatars')),
            ],
        ),
        migrations.CreateModel(
            name='InterestTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('time', models.DateField()),
                ('all_day', models.BooleanField(default=False)),
                ('location_name', models.CharField(default='', max_length=50)),
                ('description', models.CharField(max_length=1500)),
                ('location_lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('location_long', models.DecimalField(decimal_places=6, max_digits=9)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetmaps.customuser')),
                ('tags', models.ManyToManyField(to='meetmaps.InterestTag')),
                ('users_attending', models.ManyToManyField(related_name='_event_users_attending_+', to='meetmaps.CustomUser')),
                ('users_managing', models.ManyToManyField(related_name='_event_users_managing_+', to='meetmaps.CustomUser')),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='tags',
            field=models.ManyToManyField(to='meetmaps.InterestTag'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]