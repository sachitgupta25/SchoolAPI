from rest_framework import serializers
from .models import Student, Teacher, User, Principal

class Principalserializer(serializers.ModelSerializer):
    class Meta:
        model = Principal
        fields= '__all__'


class TeacherSerializerMain(serializers.Serializer):
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20)
    qualification = serializers.CharField(max_length=20)
    primary_subject = serializers.CharField(max_length=20)
    secondary_subject = serializers.CharField(max_length=20)

    def save(self, validated_data):
        user = User()

        user.first_name = validated_data["first_name"]
        user.last_name = validated_data["last_name"]
        user.email = validated_data["email"]
        user.username = user.email
        user.is_staff = True
        user.set_password(validated_data["password"])
        user.save()
        teacher = Teacher()
        teacher.user = user
        teacher.qualification = validated_data["qualification"]
        teacher.primary_subject = validated_data["primary_subject"]
        teacher.secondary_subject = validated_data["primary_subject"]
        teacher.save()

        return teacher



class StudentSerializerMain(serializers.Serializer):
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20)
    city = serializers.CharField(max_length=20)
    roll_no = serializers.IntegerField(min_value=0)

    def save(self, validated_data):
        user = User()

        user.first_name = validated_data["first_name"]
        user.last_name = validated_data["last_name"]
        user.email = validated_data["email"]
        user.username = user.email
        user.set_password(validated_data["password"])
        user.save()

        student = Student()
        student.user = user
        student.city = validated_data["city"]
        student.roll_no = validated_data["roll_no"]
        student.save()

        return student


class PrincipalSerializerMain(serializers.Serializer):
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20)

    def save(self, validated_data):
        user = User()

        user.first_name = validated_data["first_name"]
        user.last_name = validated_data["last_name"]
        user.email = validated_data["email"]
        user.username = user.email
        user.set_password(validated_data["password"])
        user.save()




        principal = Principal()
        principal.user = user
        principal.save()

        return principal



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class StudentDetails(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Student
        fields=["id","user","city","roll_no"]

class TeacherDetails(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = ["id", "user", "guid", "qualification", "primary_subject", "secondary_subject"]


class PrincipalDetails(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Student
        fields=["user"]