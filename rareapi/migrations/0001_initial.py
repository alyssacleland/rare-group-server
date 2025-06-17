from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('bio', models.CharField(max_length=400)),
                ('profile_image_url', models.URLField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('created_on', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('uid', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('content', models.TextField()),
                ('approved', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=models.CASCADE, to='rareapi.User')),  
            ],
        ),
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=models.CASCADE, to='rareapi.Post')),  
                ('tag', models.ForeignKey(on_delete=models.CASCADE, to='rareapi.Tag')),   
            ],
        ),
    ]
