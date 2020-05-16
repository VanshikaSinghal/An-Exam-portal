# Generated by Django 3.0.2 on 2020-02-08 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20200208_0134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imageupload',
            fields=[
                ('imageno', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=20)),
                ('tenmark', models.FileField(default='', upload_to='portal/docs/tenmark')),
                ('twmark', models.FileField(default='', upload_to='portal/docs/twmark')),
                ('gmark', models.FileField(default='', upload_to='portal/docs/gmark')),
                ('smark', models.FileField(default='', upload_to='portal/docs/smark')),
                ('bcertificate', models.FileField(default='', upload_to='portal/docs/birthcertificate')),
                ('ccertificate', models.FileField(default='', upload_to='portal/docs/ccertificate')),
                ('photo', models.FileField(default='', upload_to='portal/docs/photo')),
                ('sign', models.FileField(default='', upload_to='portal/docs/sign')),
                ('filename', models.CharField(max_length=400)),
            ],
        ),
    ]