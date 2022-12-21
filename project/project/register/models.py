from datetime import timezone
from ipaddress import summarize_address_range
from django.db.models import Q
import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.contrib.auth import get_user_model
from localflavor.in_.models import INStateField
from phone_field import PhoneField

Myuser = get_user_model


class UserManager(BaseUserManager):
    def create_user(self,email,full_name,phone,password=None,password2=None):
        if not email:
            raise ValueError('Users must have an email address')
        user=self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            phone=phone
        
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,full_name,phone,password=None):
        user=self.create_user(
            email,
            password=password,
            full_name=full_name,
            phone=phone
        )
        user.is_admin=True
        user.save(using=self._db)
        return user

gender= (
    ("Male","Male"),
    ("Female","Female"),
    ("Other","Other")
)
class Myuser(AbstractBaseUser):
    email=models.EmailField(verbose_name='Email',max_length=255,unique=True)
    full_name=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)

    objects=UserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS= ['full_name','phone']

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin

class User_Profile(models.Model):
    full_name=models.CharField(max_length=200)
    phone = PhoneField(blank=False, unique=True)
    alt_phone = PhoneField(blank=False)
    gender = models.CharField(max_length=100,choices=gender)
    DOB = models.DateField(auto_now_add=True) 
    profile_photo = models.ImageField(upload_to='register/image', blank=True)
    address = models.CharField(max_length=200)
    city =models.CharField(max_length=200)
    state = INStateField(null=True, blank=True)
    pincode = models.PositiveIntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.full_name)


class Add_Funds(models.Model): 
    account_balance = models.IntegerField(default='0')
    enter_amount = models.IntegerField(default='0')
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    made_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.account_balance)

class Withdraw(models.Model):
    user = models.ForeignKey(Myuser,on_delete=models.CASCADE, null=True, blank=True)
    account_balance = models.ForeignKey(Add_Funds,on_delete=models.CASCADE, null=True, blank=True)
    enter_amount = models.IntegerField(default='0')
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    
    def __str__(self):
        return "{}".format(self.account_balance)

class Email_verification(models.Model):
    email=models.EmailField(max_length=200,unique=True)
    otp=models.CharField(max_length=200 ,null=True, blank=True)
    is_verified=models.BooleanField(default=False)

class Phone_verification(models.Model):
    phone=models.CharField(max_length=12,unique=True)
    otp=models.CharField(max_length=6)
    is_phone_verified=models.BooleanField(default=False)

banks= (
    ("Central Bank Of India","Central Bank Of India"),
    ("State Bank Of India","State Bank Of India"),
    ("HDFC","HDFC"),
    ("Punjab National Bank ","Punjab National Bank "),
    ("Bank Of Baroda","Bank Of Baroda")
)

class Bank(models.Model):
    bank_name = models.CharField(max_length=100,choices=banks)
    account_number = models.CharField(max_length=20,unique=True)
    re_enter_account_number = models.CharField(max_length=20)
    ifsc = models.CharField(max_length=15)
    branch = models.CharField(max_length=100)

relation = (
    ("Father","Father"),
    ("Mother","Mother"),
    ("Retired","Retired"),
    ("Self Employed","Self Employed"),
    ("Student","Student"),
    ("Unemployed","Unemployed"),
    ("Housewife","Housewife"),

)

class Nominee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.IntegerField()
    date_of_birth = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    nominee_proof_identy = models.FileField()
    relation_with_nominee = models.CharField(max_length=100,choices=relation)
    percentage_of_share = models.CharField(max_length=6)

profession1 = (
    ("Salaried","Salaried"),
    ("Buisiness","Buisiness"),
    ("Retired","Retired"),
    ("Self Employed","Self Employed"),
    ("Student","Student"),
    ("Unemployed","Unemployed"),
    ("Housewife","Housewife"),

)

class KYC(models.Model):
    aadharcard_no=models.CharField(max_length=12,unique=True)
    name=models.ForeignKey(Myuser,on_delete=models.CASCADE)
    date_of_birth=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    marritul_status=models.CharField(max_length=50)
    profession=models.CharField(max_length=50,choices=profession1)
    sub_profession=models.CharField(max_length=50)
    annual_income=models.CharField(max_length=20)
    fathers_name=models.CharField(max_length=100)
    mothers_name=models.CharField(max_length=100)
    permanent_address=models.CharField(max_length=255)
    pancard_no=models.CharField(max_length=20,unique=True)

class Aadharcard_verification(models.Model):
    aadhar_no=models.CharField(max_length=12,unique=True)
    otp=models.CharField(max_length=6)
    is_aadhar_verified=models.BooleanField(default=False)


class Watchlist(models.Model):
    company_name=models.CharField(max_length=200)
    user = models.ForeignKey(Myuser,on_delete=models.CASCADE, null=True, blank=True)
    watchlist1 = models.CharField(max_length=20)
    watchlist2 = models.CharField(max_length=20)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.company_name)

class Orders(models.Model):

    stock_exchange=(
        ("NSE","NSE"),
        ("BSE","BSE")
    )

    val=(
        ("Day","Day"),
        ("IOC","IOC")
    )
    products=(
        ("Intraday","Intraday"),
        ("Longterm","Longterm")
    )

    user = models.ForeignKey(Myuser,on_delete=models.CASCADE, null=True, blank=True)
    lists = models.ForeignKey(Watchlist, on_delete=models.CASCADE, null=True, blank=True)
    product=models.CharField(max_length=250, choices=products)
    stock=models.CharField(max_length=250, choices=stock_exchange)
    quantity=models.IntegerField()
    price=models.FloatField(max_length=250)
    ltp=models.IntegerField() #Last Traded Price
    validity=models.CharField(max_length=250, choices=val)
    created_at=models.DateField(auto_now_add=True)  
    order_set_date = models.DateTimeField(auto_now_add=True)
    order_reach_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return "{}".format(self.stock)

class Portfolio(models.Model):

    trade_type =(
        ("BUY","BUY"),
        ("SELL","SELL")
    )
    order_types=(
        ("Market","Market"),
        ("Limit","Limit")
    )
    made_by = models.ForeignKey(Myuser,on_delete=models.CASCADE, null=True, blank=True)
    amount= models.IntegerField()
    quantity=models.IntegerField(default=0)
    email=models.EmailField()
    product_name=models.CharField(max_length=250)
    types=models.CharField(max_length=250)
    types=models.CharField(max_length=250, choices=order_types)
    order=models.CharField(max_length=250, choices=trade_type)
    made_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

class Order_Options(models.Model):
    trade_type = (
        ("Take Profit", "Take Profit"),
        ("Stop loss", "Stop loss"),
        ("Working", "Working"),
        ("Close", "Close"),
    )

    status = (
        ("Pending", "Pending"),
        ("Working", "Working"),
        ("Done", "Done"),
        ("Close", "Close"),
    )

    add_funds = models.ForeignKey(Add_Funds, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
    amount = models.FloatField(verbose_name="token amount")
    status = models.CharField(max_length=15, choices=status, verbose_name="status", default="Pending")
    trade_type = models.CharField(max_length=15, choices=trade_type, verbose_name="trade type", default="Working")
    stoploss = models.FloatField(blank=True, null=True)
    take_profit = models.FloatField(blank=True, null=True)
    oreder_reach_date = models.DateTimeField(null=True, blank=True)
    created =  models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return "{}".format(self.amount)


