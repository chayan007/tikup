from rest_framework import serializers
from .models import BlockedUser, Conversation, Message
from base.serializers import *
from usermodule.api.serializers import ProfileSerializer
import time

class ConversationSerializers(ModelSerializer):
    sender = serializers.SerializerMethodField(read_only=True)
    receiver = serializers.SerializerMethodField(read_only=True)
    unread_message_sender = serializers.SerializerMethodField(read_only=True)
    unread_message_receiver = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)

    def get_created_at(self,obj):
        return int(time.mktime(obj.created_at.timetuple()))

    def get_sender(self, obj):
        if obj.sender.profile:
            data = ProfileSerializer(obj.sender.profile).data
            data["id"] = obj.sender.id
            del data["uuid"]
            return data
        else:
            return {}

    def get_receiver(self, obj):
        if obj.receiver.profile:
            data = ProfileSerializer(obj.receiver.profile).data
            data["id"] = obj.receiver.id
            del data["uuid"]
            return data
        else:
            return {}
        
    def get_unread_message_sender(self, obj):
        return Message.objects.filter(user=obj.sender,conversation=obj,is_read=False,is_delete=False).count()


    def get_unread_message_receiver(self, obj):
        return Message.objects.filter(user=obj.receiver,conversation=obj,is_read=False,is_delete=False).count()        

    class Meta:
        model = Conversation
        exclude = ("modified_at",)
        read_only_fields = ('sender', "uuid", "created_at",)

class MessageSerializers(ModelSerializer):
    profile = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField(read_only=True)

    def get_created_at(self,obj):
        return int(time.mktime(obj.created_at.timetuple()))

    def get_profile(self, obj):
        if obj.user.profile:
            data = ProfileSerializer(obj.user.profile).data
            data["id"] = obj.user.id
            del data["uuid"]
            return data
        else:
            return {}

    class Meta:
        model = Message
        read_only_fields = ('user', "uuid", "created_at", "modified_at",)
        fields = ('profile', 'text', 'is_read', "uuid", "created_at",)


class BlockedUserSerializers(ModelSerializer):
    created_at = serializers.SerializerMethodField(read_only=True)

    def get_created_at(self,obj):
        return int(time.mktime(obj.created_at.timetuple()))

    class Meta:
        model = BlockedUser
        read_only_fields = ('user',)
        exclude = ("modified_at",)

    