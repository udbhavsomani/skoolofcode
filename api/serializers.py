from rest_framework import serializers
from .models import CustomUser, Subject, AvailableTiming
from rest_framework.authtoken.views import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'email', 'first_name',
                  'last_name', 'is_student', 'is_teacher')

    extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        }}

    def create(self, validated_data):
        # print(validated_data)
        # print(self.context['request'].data)
        try:
            user = CustomUser(
                username=validated_data['username'],
                first_name=self.context['request'].data['name'],
            )
        except:
            user = CustomUser(
                username=validated_data['username'],
            )
        user.set_password(validated_data['password'])
        if(self.context['request'].data['designation'] == 'student'):
            user.is_student = True
        else:
            user.is_teacher = True
        user.save()
        AvailableTiming(user=user).save()
        Token.objects.create(user=user)
        return user


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name')
    
    def create(self, validated_data):
        validated_data["teacher"] = self.context["request"].user
        if(self.context["request"].user.is_teacher):
            if(Subject.objects.filter(name=validated_data["name"], teacher=self.context["request"].user).first() != None):
                raise serializers.ValidationError("You are already teaching this subject.")
            return super().create(validated_data)
        else:
            raise serializers.ValidationError("You are not a teacher.")


class AvailableTimingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableTiming
        fields = ('id', 'data',)
    
    def create(self, validated_data):
        validated_data["teacher"] = self.context["request"].user
        if(self.context["request"].user.is_teacher):
            if(AvailableTiming.objects.filter(teacher=self.context["request"].user).first() != None):
                raise serializers.ValidationError("Edit your previously created timings.")
            return super().create(validated_data)
        else:
            raise serializers.ValidationError("You are not a teacher.")