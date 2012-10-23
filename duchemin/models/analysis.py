from django.db import models

from duchemin.models.person import DCPerson
from duchemin.models.piece import DCPiece
from duchemin.models.phrase import DCPhrase


class DCAnalysis(models.Model):
    class Meta:
        app_label = "duchemin"
        verbose_name = "Analysis"
        verbose_name_plural = "Analyses"

    timestamp = models.CharField(max_length=64, blank=True, null=True)
    analyst = models.ForeignKey(DCPerson, to_field='person_id')
    composition_number = models.ForeignKey(DCPiece, to_field='piece_id')
    phrase_number = models.ForeignKey(DCPhrase, to_field='phrase_id')
    start_measure = models.IntegerField(blank=True, null=True)
    stop_measure = models.IntegerField(blank=True, null=True)
    cadence = models.CharField(max_length=16, blank=True, null=True)
    cadence_kind = models.CharField(max_length=64, blank=True, null=True)
    cadence_alter = models.CharField(max_length=64, blank=True, null=True)
    cadence_role_cantz = models.CharField(max_length=16, blank=True, null=True)
    cadence_role_tenz = models.CharField(max_length=16, blank=True, null=True)
    cadence_final_tone = models.CharField(max_length=16, blank=True, null=True)
    voices_p6_up = models.CharField(max_length=16, blank=True, null=True)
    voices_p6_lo = models.CharField(max_length=16, blank=True, null=True)
    voices_p3_up = models.CharField(max_length=16, blank=True, null=True)
    voices_p3_lo = models.CharField(max_length=16, blank=True, null=True)
    voices_53_up = models.CharField(max_length=16, blank=True, null=True)
    voices_53_lo = models.CharField(max_length=16, blank=True, null=True)
    other_formulas = models.CharField(max_length=64, blank=True, null=True)
    other_pres_type = models.CharField(max_length=64, blank=True, null=True)
    voice_role_up1_nim = models.CharField(max_length=16, blank=True, null=True)
    voice_role_lo1_nim = models.CharField(max_length=16, blank=True, null=True)
    voice_role_up2_nim = models.CharField(max_length=16, blank=True, null=True)
    voice_role_lo2_nim = models.CharField(max_length=16, blank=True, null=True)
    voice_role_dux1 = models.CharField(max_length=16, blank=True, null=True)
    voice_role_com1 = models.CharField(max_length=16, blank=True, null=True)
    voice_role_dux2 = models.CharField(max_length=16, blank=True, null=True)
    voice_role_com2 = models.CharField(max_length=16, blank=True, null=True)
    voice_role_un_oct = models.CharField(max_length=16, blank=True, null=True)
    voice_role_fifth = models.CharField(max_length=16, blank=True, null=True)
    voice_role_fourth = models.CharField(max_length=16, blank=True, null=True)
    voice_role_above = models.CharField(max_length=16, blank=True, null=True)
    voice_role_below = models.CharField(max_length=16, blank=True, null=True)
    other_contrapuntal = models.CharField(max_length=128, blank=True, null=True)
    text_treatment = models.CharField(max_length=128, blank=True, null=True)
    repeat_kind = models.CharField(max_length=64, blank=True, null=True)
    earlier_phrase = models.CharField(max_length=16, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    repeat_exact_varied = models.CharField(max_length=16, blank=True, null=True)

    def __unicode__(self):
        return u"{0}, {1}, {2}".format(self.id, self.analyst.surname, self.composition_number.piece_id)
