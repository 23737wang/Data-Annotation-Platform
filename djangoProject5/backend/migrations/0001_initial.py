# Generated by Django 4.2.11 on 2024-05-28 15:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='username', max_length=12)),
                ('password', models.CharField(default='password', max_length=18)),
                ('email', models.CharField(default='email', max_length=350)),
                ('userBalance', models.FloatField(default=0.0)),
                ('userCreditRank', models.IntegerField(default=1)),
                ('userType', models.CharField(choices=[('normalUser', 'normalUser'), ('admin', 'admin')], default='normalUser', max_length=20)),
                ('userCurrentExp', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(default='', max_length=50)),
                ('task_description', models.CharField(default='', max_length=500)),
                ('data_type', models.CharField(choices=[('文本', '文本'), ('图片', '图片')], default='image', max_length=20)),
                ('data_nums', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('task_rank', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('each_pay', models.FloatField(default=0.0)),
                ('question_description', models.CharField(default='', max_length=500)),
                ('question_type', models.CharField(choices=[('单选题', '单选题'), ('多选题', '多选题'), ('填空题', '填空题'), ('框图题', '框图题')], default='单选题', max_length=20)),
                ('options', models.JSONField(default=dict)),
                ('task_status', models.CharField(choices=[('审核未通过', '审核未通过'), ('审核中', '审核中'), ('进行中', '进行中'), ('提前终止', '提前终止'), ('已逾期', '已逾期')], default='审核中', max_length=20)),
                ('release_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('deadline_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.user')),
            ],
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('subtask_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtask_index', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('content', models.CharField(default='', max_length=500)),
                ('answer', models.CharField(default='', max_length=500)),
                ('finish_time', models.DateTimeField(blank=True, null=True)),
                ('subtask_status', models.CharField(choices=[('未领取', '未领取'), ('未完成', '未完成'), ('已完成', '已完成'), ('举报中', '举报中'), ('举报已解决', '举报已解决')], default='未领取', max_length=20)),
                ('receiver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.user')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.task')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(default='', max_length=500)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='backend.user')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='backend.user')),
                ('subtask', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtask', to='backend.subtask')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task', to='backend.task')),
            ],
        ),
    ]
