# Generated by Django 2.0.7 on 2018-07-20 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0026_auto_20180720_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='my_tag',
            field=models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('Mechanical', 'Mechanical'), ('Design', 'Design'), ('Business-and-Career', 'Business and Career'), ('Entertainment', 'Entertainment'), ('Jabalpur-city', 'Jabalpur city'), ('IIITDMJ-Rules-and-Regulations', 'IIITDMJ rules and regulations'), ('Life-Relationship-and-Self', 'Life Relationship and Self'), ('IIITDMJ-Campus', 'IIITDMJ Campus'), ('Programmes', 'Programmes')], default=1, max_length=40),
        ),
    ]
