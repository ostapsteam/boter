# -*- coding: utf-8 -*-
# Generated by Django 3.1.10.17 on 2017-08-12 12:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('token', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dialog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('closed', models.BooleanField(default=False)),
                ('terminated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('desc', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=256)),
                ('answer_text', models.CharField(blank=True, max_length=256, null=True)),
                ('is_sent', models.BooleanField(default=False)),
                ('skiped', models.BooleanField(default=False)),
                ('answered', models.BooleanField(default=False)),
                ('dialog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boter.Dialog')),
            ],
        ),
        migrations.CreateModel(
            name='TUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=16, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=128, null=True)),
                ('last_name', models.CharField(blank=True, max_length=128, null=True)),
                ('language_code', models.CharField(blank=True, max_length=16, null=True)),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
                ('dialog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boter.Dialog')),
            ],
        ),
        migrations.AddField(
            model_name='proposal',
            name='asignee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boter.TUser'),
        ),
        migrations.AddField(
            model_name='proposal',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='boter.TUser'),
        ),
        migrations.AddField(
            model_name='proposal',
            name='deleted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='boter.TUser'),
        ),
        migrations.AddField(
            model_name='proposal',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='boter.TUser'),
        ),
        migrations.AddField(
            model_name='bot',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='boter.TUser'),
        ),
        migrations.AddField(
            model_name='bot',
            name='deleted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='boter.TUser'),
        ),
        migrations.AddField(
            model_name='bot',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='boter.TUser'),
        ),
    ]