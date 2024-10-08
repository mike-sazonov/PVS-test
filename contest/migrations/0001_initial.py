from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('email', models.CharField(max_length=70, verbose_name='Email')),
                ('code', models.TextField(max_length=1000, verbose_name='Код')),
            ],
            options={
                'verbose_name': 'Участник конкурса',
                'verbose_name_plural': 'Участники конкурса',
            },
        ),
    ]
