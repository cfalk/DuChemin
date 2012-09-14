from django.contrib import admin

from duchemin.models.analysis import DCAnalysis
from duchemin.models.book import DCBook
from duchemin.models.person import DCPerson
from duchemin.models.phrase import DCPhrase
from duchemin.models.piece import DCPiece
from duchemin.models.reconstruction import DCReconstruction


class DCAnalysisAdmin(admin.ModelAdmin):
    list_display = ['analyst', 'composition_number', 'phrase_number', 'start_measure', 'stop_measure']

class DCPhraseAdmin(admin.ModelAdmin):
    list_display = ['phrase_id', 'piece_id', 'phrase_num', 'phrase_start', 'phrase_stop', 'phrase_text']

admin.site.register(DCAnalysis, DCAnalysisAdmin)
admin.site.register(DCBook)
admin.site.register(DCPerson)
admin.site.register(DCPhrase, DCPhraseAdmin)
admin.site.register(DCPiece)
admin.site.register(DCReconstruction)
