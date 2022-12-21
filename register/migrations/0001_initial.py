# Generated by Django 3.2 on 2022-12-20 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import localflavor.in_.models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Myuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('full_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Aadharcard_verification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar_no', models.CharField(max_length=12, unique=True)),
                ('otp', models.CharField(max_length=6)),
                ('is_aadhar_verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Add_Funds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_balance', models.IntegerField(default='0')),
                ('enter_amount', models.IntegerField(default='0')),
                ('order_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('made_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(choices=[('Central Bank Of India', 'Central Bank Of India'), ('State Bank Of India', 'State Bank Of India'), ('HDFC', 'HDFC'), ('Punjab National Bank ', 'Punjab National Bank '), ('Bank Of Baroda', 'Bank Of Baroda')], max_length=100)),
                ('account_number', models.CharField(max_length=20, unique=True)),
                ('re_enter_account_number', models.CharField(max_length=20)),
                ('ifsc', models.CharField(max_length=15)),
                ('branch', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Email_verification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('otp', models.CharField(blank=True, max_length=200, null=True)),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Nominee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('date_of_birth', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('nominee_proof_identy', models.FileField(upload_to='')),
                ('relation_with_nominee', models.CharField(choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Retired', 'Retired'), ('Self Employed', 'Self Employed'), ('Student', 'Student'), ('Unemployed', 'Unemployed'), ('Housewife', 'Housewife')], max_length=100)),
                ('percentage_of_share', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Phone_verification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12, unique=True)),
                ('otp', models.CharField(max_length=6)),
                ('is_phone_verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('phone', phone_field.models.PhoneField(max_length=31, unique=True)),
                ('alt_phone', phone_field.models.PhoneField(max_length=31)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=100)),
                ('DOB', models.DateField(auto_now_add=True)),
                ('profile_photo', models.ImageField(blank=True, upload_to='register/image')),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', localflavor.in_.models.INStateField(blank=True, max_length=2, null=True)),
                ('pincode', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enter_amount', models.IntegerField(default='0')),
                ('order_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('account_balance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='register.add_funds')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('watchlist1', models.CharField(max_length=20)),
                ('watchlist2', models.CharField(max_length=20)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('quantity', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('product_name', models.CharField(max_length=250)),
                ('types', models.CharField(choices=[('Market', 'Market'), ('Limit', 'Limit')], max_length=250)),
                ('order', models.CharField(choices=[('BUY', 'BUY'), ('SELL', 'SELL')], max_length=250)),
                ('made_on', models.DateTimeField(auto_now_add=True)),
                ('made_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(choices=[('Intraday', 'Intraday'), ('Longterm', 'Longterm')], max_length=250)),
                ('stock', models.CharField(choices=[('NSE', 'NSE'), ('BSE', 'BSE')], max_length=250)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField(max_length=250)),
                ('ltp', models.IntegerField()),
                ('validity', models.CharField(choices=[('Day', 'Day'), ('IOC', 'IOC')], max_length=250)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('order_set_date', models.DateTimeField(auto_now_add=True)),
                ('order_reach_date', models.DateTimeField(blank=True, null=True)),
                ('lists', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='register.watchlist')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order_Options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(verbose_name='token amount')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Working', 'Working'), ('Done', 'Done'), ('Close', 'Close')], default='Pending', max_length=15, verbose_name='status')),
                ('trade_type', models.CharField(choices=[('Take Profit', 'Take Profit'), ('Stop loss', 'Stop loss'), ('Working', 'Working'), ('Close', 'Close')], default='Working', max_length=15, verbose_name='trade type')),
                ('stoploss', models.FloatField(blank=True, null=True)),
                ('take_profit', models.FloatField(blank=True, null=True)),
                ('oreder_reach_date', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('add_funds', models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.SET_NULL, to='register.add_funds')),
            ],
        ),
        migrations.CreateModel(
            name='KYC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadharcard_no', models.CharField(max_length=12, unique=True)),
                ('date_of_birth', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('marritul_status', models.CharField(max_length=50)),
                ('profession', models.CharField(choices=[('Salaried', 'Salaried'), ('Buisiness', 'Buisiness'), ('Retired', 'Retired'), ('Self Employed', 'Self Employed'), ('Student', 'Student'), ('Unemployed', 'Unemployed'), ('Housewife', 'Housewife')], max_length=50)),
                ('sub_profession', models.CharField(max_length=50)),
                ('annual_income', models.CharField(max_length=20)),
                ('fathers_name', models.CharField(max_length=100)),
                ('mothers_name', models.CharField(max_length=100)),
                ('permanent_address', models.CharField(max_length=255)),
                ('pancard_no', models.CharField(max_length=20, unique=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
