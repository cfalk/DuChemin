from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from duchemin.models.analysis import DCAnalysis
from duchemin.models.book import DCBook
from duchemin.models.person import DCPerson
from duchemin.models.phrase import DCPhrase
from duchemin.models.piece import DCPiece
from duchemin.models.reconstruction import DCReconstruction
from duchemin.models.userprofile import DCUserProfile
from duchemin.models.file import DCFile
from duchemin.models.content_block import DCContentBlock


class DCAnalysisAdmin(admin.ModelAdmin):
    list_display = ['analyst', 'composition_number', 'phrase_number', 'start_measure', 'stop_measure']


class DCFilePieceInline(admin.TabularInline):
    model = DCPiece.attachments.through
    can_delete = True,
    verbose_name = "File"
    verbose_name_plural = "Files"


class DCPieceAdmin(admin.ModelAdmin):
    inlines = (
        DCFilePieceInline,
    )


class DCFileReconstructionInline(admin.TabularInline):
    model = DCReconstruction.attachments.through
    can_delete = True
    verbose_name = "File"
    verbose_name_plural = "Files"


class DCReconstructionAdmin(admin.ModelAdmin):
    inlines = (
        DCFileReconstructionInline,
    )


class DCPhraseAdmin(admin.ModelAdmin):
    list_display = ['phrase_id', 'piece_id', 'phrase_num', 'phrase_start', 'phrase_stop', 'phrase_text']


class UserProfileInline(admin.StackedInline):
    model = DCUserProfile
    can_delete = False
    verbose_name_plural = 'profile'


class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(DCUserProfile)
admin.site.register(DCAnalysis, DCAnalysisAdmin)
admin.site.register(DCBook)
admin.site.register(DCPerson)
admin.site.register(DCPhrase, DCPhraseAdmin)
admin.site.register(DCPiece, DCPieceAdmin)
admin.site.register(DCReconstruction, DCReconstructionAdmin)
admin.site.register(DCFile)
admin.site.register(DCContentBlock)
