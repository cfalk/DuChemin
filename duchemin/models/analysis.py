from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class DCAnalysis(models.Model):
    class Meta:
        app_label = "duchemin"

    # timestamp = pass
    # analyst = pass
    # composition_number = pass
    # phrase_number = pass
    # start_measure = pass
    # stop_measure = pass
    # cadence = pass
    # cadence_kind = pass
    # cadence_alter = pass
    # cadence_role_cantz = pass
    # cadence_role_tenz = pass
    # cadence_final_tone = pass
    # voices_p6_up = pass
    # voices_p6_lo = pass
    # voices_p3_up = pass
    # voices_p3_lo = pass
    # voices_53_up = pass
    # voices_53_lo = pass
    # other_formulas = pass
    # other_pres_type = pass
    # voice_role_up1_nim = pass
    # voice_role_lo1_nim = pass
    # voice_role_up2_nim = pass
    # voice_role_lo2_nim = pass
    # voice_role_dux1 = pass
    # voice_role_com1 = pass
    # voice_role_dux2 = pass
    # voice_role_com2 = pass
    # voice_role_un_oct = pass
    # voice_role_fifth = pass
    # voice_role_fourth = pass
    # voice_role_above = pass
    # voice_role_below = pass
    # other_contrapuntal = pass
    # text_treatment = pass
    # repeat_kind = pass
    # earlier_phrase = pass
    # comment = pass
    # repeat_exact_varied = pass
