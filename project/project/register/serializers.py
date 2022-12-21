from rest_framework import serializers
from .models import *


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=Myuser
        fields=['id','email','full_name','phone','password','password2','created_at','updated_at']
        
        extra_kwargs={
            'password':{'write_only':True}
        }

    def validate(self,attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and confirm password doesn't match")
        return attrs

    def create(self,validate_data):
        return Myuser.objects.create_user(**validate_data)

class UserLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        model=Myuser
        fields=['email','password']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Profile
        fields= ['id','full_name','phone','alt_phone','gender','DOB','profile_photo','address','city',
        'state','pincode','created_at','updated_at']


class Watchlist_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields=["company_name","user","watchlist1","watchlist2","created_at"]

class Orders_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ["user", "lists", "stock" , "quantity","price","ltp","validity", "created_at","order_set_date","order_reach_date"]

class Order_Option_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Options
        fields=["amount","status","trade_type","stoploss","take_profit","oreder_reach_date"]

class Add_Funds_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Add_Funds
        fields= ["id","account_balance","enter_amount","order_id","made_on"]

class Portfolio_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields= '__all__'

class Withdraw_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw
        fields= ["id","account_balance","enter_amount","user"]

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Myuser
        fields=['id','email','full_name','phone']
       
class UserChangePasswordSerializer(serializers.Serializer):
    password=serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True)
    password2=serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True)

    class Meta:
        fields=['password','password2']

    def validate(self,attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        user=self.context.get('user')
        if password != password2:
            raise serializers.ValidationError('Password and Password2 not match')
        user.set_password(password)
        user.save()
        return attrs

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email_verification
        fields = ['email','is_verified']

class VerifyEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['bank_name','account_number','re_enter_account_number','ifsc','branch']

class NomineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nominee
        fields = ['id','first_name','last_name','email','mobile','date_of_birth','address','nominee_proof_identy','relation_with_nominee','percentage_of_share']

class UserKYCSerializer(serializers.ModelSerializer):
    class Meta:
        model = KYC
        fields = ['id','aadharcard_no','name','date_of_birth','gender','marritul_status','profession','sub_profession','annual_income','fathers_name','mothers_name','permanent_address','pancard_no']

