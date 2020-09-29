from rest_framework import serializers
from .models import BlockedUser, Conversation, Message
from base.serializers import *


class ConversationSerializers(ModelSerializer):
    sender = serializers.SerializerMethodField(read_only=True)
    receiver = serializers.SerializerMethodField(read_only=True)

    def get_sender(self, obj):
        return {
            "id": obj.sender.id,
            "username": obj.sender.username,
            "email": obj.sender.email,
        }

    def get_receiver(self, obj):
        return {
            "id": obj.receiver.id,
            "username": obj.receiver.username,
            "email": obj.receiver.email,
        }

    class Meta:
        model = Conversation
        read_only_fields = ('last_exit', 'sender', "uuid",
                            "created_at", "modified_at",)
        fields = '__all__'


class MessageSerializers(ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    def get_user(self, obj):
        return {
            "id": obj.user.id,
            "username": obj.user.username,
            "email": obj.user.email,
        }

    class Meta:
        model = Message
        read_only_fields = ('user', "uuid", "created_at", "modified_at",)
        fields = ('user','text', 'is_read',"uuid",)


class BlockedUserSerializers(ModelSerializer):
    class Meta:
        model = BlockedUser
        read_only_fields = ('date', 'user',)
        fields = '__all__'
