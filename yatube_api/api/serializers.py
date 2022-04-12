from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Post, Follow, Group, User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('id', 'author', 'created', 'post')
        # fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    # group = serializers.SlugRelatedField(
    #     queryset=Group.objects.all(),
    #     slug_field='slug',
    #     required=False
    # )
    comment = CommentSerializer(
        many=True,
        required=False
    )
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        # default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group',
                  'comment')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        # read_only=True,
        slug_field='username'
    )

    # def validate(self, data):
    #     if self.user == self.following:
    #         raise serializers.ValidationError(
    #             'Нельзя подписаться на самого себя!'
    #         )

    def validate(self, data):
        if self.context.get('request').user == data['following']:
            raise serializers.ValidationError(
                'Пользователь не может подписаться сам на себя!')
        return data

    class Meta:
        fields = ('user', 'following')
        model = Follow
        # read_only_fields = ('user', 'following',)
        read_only_fields = ('user', )
        validators = [
            UniqueTogetherValidator(
                # queryset=User.objects.all(),
                queryset=Follow.objects.all(),
                fields=['user', 'following']
            )
        ]