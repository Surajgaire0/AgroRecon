from rest_framework import serializers


class PasswordValidator:
    """
    Validate password length
    """
    def __init__(self, min_length=8, max_length=255):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, password, user=None):
        if len(password) > self.max_length:
            raise serializers.ValidationError(
                "Password must contain at most {} characters.".format(
                    self.max_length),
            )

        if len(password) < self.min_length:
            raise serializers.ValidationError(
                "Password must contain at least {} characters.".format(
                    self.min_length),
            )
