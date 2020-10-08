from base.views import ViewSet
from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .method import is_blocked
from .models import BlockedUser, Conversation, Message
from .serializers import (
    BlockedUserSerializers,
    ConversationSerializers,
    MessageSerializers
)
from datetime import datetime

import logging

class ConversationViewSet(ViewSet):
    serializer_class = ConversationSerializers
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        """
        Get conversation list.
        """
        queryset = Conversation.objects.filter(
            Q(sender_id=self.request.user.id) | Q(
                receiver_id=self.request.user.id)
        )

        serializer_class = ConversationSerializers(queryset, many=True)
        return Response(serializer_class.data)

    def create(self, request):
        """
        Create new conversation.
        """
        vaildata_data = ConversationSerializers(data=self.request.data)
        vaildata_data.is_valid(raise_exception=True)

        user = None

        try:
            user = User.objects.get(id=self.request.data.get("receiver"))
        except User.DoesNotExist:
            return Response({"error_message": "Receive user not found"}, status=status.HTTP_404_NOT_FOUND)

        # check user are block or not
        if is_blocked(self.request.user, user):
            return Response({"block": True,"error_message": "You are block!"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # get conversation
            conversation = Conversation.objects.get(
                sender=self.request.user,
                receiver=user
            )
        except Conversation.DoesNotExist:
            # create new conversation
            if user != self.request.user:
                conversation = Conversation(
                    sender=self.request.user,
                    receiver=user
                )
                conversation.save()
            else:
                return Response({"error_message": "Sender and receiver are same"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"conversation": conversation.uuid}, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        """
        Delete conversation.
        """
        if not pk:
            return Response({"error_message": "Conversation not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            conversation = Conversation.objects.get(pk=pk)
            conversation.delete()
            return Response({"message": "Conversation sucessfully delete"}, status=status.HTTP_204_NO_CONTENT)
        except Conversation.DoesNotExist:
            return Response({"error_message": "Conversation not found"}, status=status.HTTP_404_NOT_FOUND)


class ConversationMessageViewSet(ViewSet):
    serializer_class = MessageSerializers
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        """
        List message by authentication user.
        """
        try:
            conversation = Conversation.objects.get(
                pk=self.request.GET.get("conversation"))
        except Conversation.DoesNotExist:
            return Response(
                {
                    "error_message": "Conversation not found",
                    "conversation": self.request.GET.get("conversation")
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if conversation.receiver == self.request.user:
            objects = conversation.sender
        else:
            objects = conversation.receiver

        Message.objects.filter(
            conversation=conversation, user=objects
        ).update(is_read=True)

        queryset = Message.objects.filter(
            conversation=conversation, is_delete=False)

        serializer_class = MessageSerializers(queryset, many=True)
        return Response(serializer_class.data)

    def create(self, request):
        """
        Send the message by authentication user.
        """
        vaildata_data = MessageSerializers(data=self.request.data)
        vaildata_data.is_valid(raise_exception=True)

        try:
            conversation = Conversation.objects.get(
                pk=vaildata_data.initial_data.get("conversation"))
        except Conversation.DoesNotExist:
            return Response(
                {
                    "error_message": "Conversation not found",
                    "conversation": vaildata_data.initial_data.get("conversation")
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            receiver_exist = User.objects.get(pk=conversation.receiver.pk)
        except User.DoesNotExist:
            return Response({"error_message": "User not found", "id": vaildata_data.initial_data.get("conversation")}, status=status.HTTP_400_BAD_REQUEST)

        if is_blocked(receiver_exist, self.request.user):
            return Response({"block":True, "error_message": "You are block!"}, status=status.HTTP_400_BAD_REQUEST)

        message = Message(
            user=self.request.user,
            conversation=conversation,
            text=vaildata_data.initial_data.get("text")
        )
        message.save()
        vaildata_data = MessageSerializers(message)
        return Response(
            {
                "message": "Message sent successfully.",
                "message_instace": vaildata_data.data
            },
            status=status.HTTP_201_CREATED
        )

    def destroy(self, request, pk=None):
        """
        Delete the message by authentication user.

        :params: message uuid (pk)
        """
        if not pk:
            return Response({"message": "Id not found", "id": pk}, status=status.HTTP_400_BAD_REQUEST)

        try:
            message = Message.objects.get(pk=pk, user=self.request.user)
            message.is_delete = True
            message.save()
        except Message.DoesNotExist:
            return Response({"error_message": "Message are not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logging.error(e)            

        return Response({"message": "Message are successfully delete."}, status=status.HTTP_204_NO_CONTENT)

class BlockedUserViewSet(ViewSet):
    serializer_class = BlockedUserSerializers
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        """
        Set block user by authentication user.

        :params:  block_user (id)
        """
        vaildata_data = BlockedUserSerializers(data=self.request.data)
        vaildata_data.is_valid(raise_exception=True)

        block_user = vaildata_data.initial_data.get("block_user")

        block_status = False

        try:
            receiver_exist = User.objects.get(pk=block_user)
        except User.DoesNotExist:
            return Response({"error_message": "User not found", "block_user": block_user}, status=status.HTTP_400_BAD_REQUEST)

        try:
            block_user = BlockedUser.objects.get(
                block_user=receiver_exist, user=self.request.user)
            message = "User are already blocked."
            block_status = True
        except BlockedUser.DoesNotExist:
            if receiver_exist != self.request.user:
                block_user = BlockedUser(
                    block_user=receiver_exist, user=self.request.user)
                block_user.save()
                message = "User successfully are blocked."
                block_status = True
            else:
                block_status = False
                return Response({"block": block_status,"error_message": "You are can't own block", "block_user": block_user}, status=status.HTTP_400_BAD_REQUEST)

        vaildata_data = BlockedUserSerializers(block_user)

        return Response({
            "block_user": vaildata_data.data,
            "block": block_status,
            "message": message
        }, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """
        Check user is block or not by authentication user.

        :params:  block_user (id)
        """
        message = ""

        block_status = False

        try:
            receiver_exist = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error_message": "User not found", "id": pk}, status=status.HTTP_400_BAD_REQUEST)

        if receiver_exist and is_blocked(receiver_exist, self.request.user):
            message = "User are block."
            block_status = True
        else:
            message = "User are not block."
            block_status = False

        return Response({"block": block_status, "message": message}, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        """
        Set unblock user by authentication user.

        :params:  block_user (id)
        """
        if not pk:
            return Response({"message": "Id not found", "id": pk}, status=status.HTTP_400_BAD_REQUEST)

        try:
            receiver_exist = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error_message": "User not found", "id": pk}, status=status.HTTP_400_BAD_REQUEST)

        try:
            if receiver_exist != self.request.user:
                block_user = BlockedUser.objects.get(block_user=receiver_exist)
                block_user.delete()
                return Response({"block": False, "message": "User are now sucessfully unblock"}, status=status.HTTP_200_OK)
            else:
                return Response({"error_message": "You are not can't own unblock.", "id": pk}, status=status.HTTP_400_BAD_REQUEST)
        except BlockedUser.DoesNotExist:
            return Response({"message": "User are not block"}, status=status.HTTP_200_OK)
