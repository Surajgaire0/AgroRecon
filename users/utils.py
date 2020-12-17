from rest_framework import serializers

class PasswordValidator:
    def __init__(self, min_length=8, max_length=20):
        self.min_length=min_length
        self.max_length=max_length

    def validate(self, password, user=None):
        if len(password) > self.max_length:
            raise serializers.ValidationError(
                "This password must contain at most {} characters.".format(self.max_length),
            )

        if len(password) < self.min_length:
            raise serializers.ValidationError(
                "This password must contain at least {} characters.".format(self.min_length),
            )
            