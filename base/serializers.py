from rest_framework import serializers

class ModelSerializer(serializers.ModelSerializer):
    def get_requet_method_type(self):
        request = self.context.get("request")
        return request.method