# Generated by Django 4.1.2 on 2022-10-22 14:54

from django.db import migrations, models
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_student_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='registration_id',
            field=models.CharField(editable=sqlalchemy.sql.expression.false, max_length=6, primary_key=sqlalchemy.sql.expression.true, serialize=False),
        ),
    ]
