from duchemin.models.analysis import DCAnalysis
from duchemin.models.piece import DCPiece
from duchemin.models.phrase import DCPhrase
from rest_framework import serializers

class DCPieceAnalysisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DCPiece


class DCPhraseAnalysisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DCPhrase

class DCAnalysisSerializer(serializers.HyperlinkedModelSerializer):
    composition_number = DCPieceAnalysisSerializer()
    phrase_number = DCPhraseAnalysisSerializer()
    class Meta:
        model = DCAnalysis