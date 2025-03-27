from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        # fields = "__all__"
        exclude = ("watchlist",)


class WatchListSerializer(serializers.ModelSerializer):
    # len_title = serializers.SerializerMethodField()
    # reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source='platform.name', read_only=True)

    class Meta:
        model = WatchList
        exclude = ['active']


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist = serializers.StringRelatedField(many=True)
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="movie-details")

    class Meta:
        model = StreamPlatform
        fields = "__all__"

    # def get_len_title(self, object):
    #     return len(object.title)

    # def validate(self, data):
    #     if data['title'] == data['description']:
    #         raise serializers.ValidationError(
    #             "Title and Description should be different!")
    #     else:
    #         return data

    # def validate_title(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Title is too short")
    #     return value


# def title_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Title is too short")


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(validators=[title_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     # instance is the object that we want to update, validated_data is the old data that we want to update
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('title', instance.title)
#         instance.description = validated_data.get(
#             'description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     def validate(self, data):
#         if data['title'] == data['description']:
#             raise serializers.ValidationError(
#                 "Title and Description should be different!")
#         else:
#             return data

    # def validate_title(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Title is too short")
    #     return value
