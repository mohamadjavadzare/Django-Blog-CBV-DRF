from rest_framework import serializers
# from rest_framework.exceptions import PermissionDenied
from ...models import Portfolio, PortfolioCategory


class PortfolioCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioCategory
        fields = [
            "id",
            "name",
        ]


class PortfolioSerializer(serializers.ModelSerializer):
    # show image url
    image1 = serializers.SerializerMethodField(method_name="get_image1", read_only=True)
    image2 = serializers.SerializerMethodField(
        method_name="get_image2", read_only=True, allow_null=True
    )
    image3 = serializers.SerializerMethodField(
        method_name="get_image3", read_only=True, allow_null=True
    )
    absolute_url = serializers.SerializerMethodField(method_name="get_abs_url")

    def get_abs_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    # how to represent objects
    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)
        # show category
        rep["category"] = PortfolioCategorySerializer(
            instance.category, context={"request": request}, many=False
        ).data
        # seperate list and detail for display
        # don't show in detail
        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("absolute_url", None)
        # don't show in list
        else:
            rep.pop("created_date", None)
            rep.pop("image2", None)
            rep.pop("image3", None)
        return rep

    # get user image from profile
    def get_image1(self, instance):
        request = self.context.get("request")
        image_url = instance.image1.url
        return request.build_absolute_uri(image_url)

    def get_image2(self, instance):
        if instance.image2:
            request = self.context.get("request")
            image_url = instance.image2.url
            return request.build_absolute_uri(image_url)
        else:
            return None

    def get_image3(self, instance):
        if instance.image3:
            request = self.context.get("request")
            image_url = instance.image3.url
            return request.build_absolute_uri(image_url)
        else:
            return None

    # user must automatically be provided and not be written by users
    """ you can do it like this:
        user = serializers.PrimaryKeyRelatedField(read_only=True)
        or do it another way:  """

    def create(self, validated_data):
        if self.context.get("request") and self.context.get("request").user.is_staff:
            return super().create(validated_data)
        else:
            raise serializers.ValidationError({"detail": "You must be a staff user"})

    class Meta:
        model = Portfolio
        fields = (
            "id",
            "title",
            "image1",
            "image2",
            "image3",
            "description",
            "category",
            "client",
            "project_date",
            "project_url",
            "created_date",
            "updated_date",
            "absolute_url",
        )
        read_only_fields = ("created_date",)
