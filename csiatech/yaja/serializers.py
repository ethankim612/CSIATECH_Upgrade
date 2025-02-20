from rest_framework import serializers
from .models import (
    Monday,
    Tuesday,
    Wednesday,
    Thursday,
    DefaultMonday,
    DefaultTuesday,
    DefaultWednesday,
    DefaultThursday,
)


class MondaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Monday
        fields = ["period1", "period2", "period3", "student_id"]


class TuesdaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuesday
        fields = ["period1", "period2", "period3", "student_id"]


class WednesdaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Wednesday
        fields = ["period1", "period2", "period3", "student_id"]


class ThursdaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Thursday
        fields = ["period1", "period2", "period3", "student_id"]


class DefaultMondaySerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultMonday
        fields = ["period1", "period2", "period3", "student_id"]


class DefaultTuesdaySerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultTuesday
        fields = ["period1", "period2", "period3", "student_id"]


class DefaultWednesdaySerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultWednesday
        fields = ["period1", "period2", "period3", "student_id"]


class DefaultThursdaySerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultThursday
        fields = ["period1", "period2", "period3", "student_id"]
