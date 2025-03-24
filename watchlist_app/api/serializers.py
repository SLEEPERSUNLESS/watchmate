from rest_framework import serializers
from watchlist_app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    len_title = serializers.SerializerMethodField()
    
    class Meta:
        model = Movie
        # fields = "__all__"
        exclude = ['active']
        
    def get_len_title(self, object):
        return len(object.title)
    
    def validate(self, data):
        if data['title'] == data['description']:
            raise serializers.ValidationError(
                "Title and Description should be different!")
        else:
            return data

    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Title is too short")
        return value


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
