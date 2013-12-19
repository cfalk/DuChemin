from duchemin.models.phrase import DCPhrase
from rest_framework import serializers

class DCPhraseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DCPhrase
        # fields = ('url',)