from rest_framework import serializers


class ParentsSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    age = serializers.IntegerField(min_value=1, max_value=99, required=True)

    class Meta:

        fields = (
            "name",
            "age",
        )


class ChildSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    age = serializers.IntegerField(min_value=1, max_value=99, required=True)
    sex = serializers.ChoiceField(choices=['male', 'female'], required=True)

    class Meta:
        fields = (
            "name",
            "age",
            "sex",
        )


class FamilySerializer(serializers.Serializer):

    father = ParentsSerializer(required=True)
    mother = ParentsSerializer(required=True)
    childrens = ChildSerializer(many=True)

    class Meta:

        fields = (
            "father",
            "mother",
            "childrens",
        )

    def validate(self, data):
        father = data.get('father')
        mother = data.get('mother')
        childrens = data.get('childrens', [])
        for child in childrens:
            if child['age'] > mother['age'] or child['age'] > father['age']:
                raise serializers.ValidationError("Childs cantbe older than parents.")
        return data