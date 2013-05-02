from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from duchemin.models.phrase import DCPhrase

CADENCE_KIND_CHOICES = [(None, ""),
                        ("Authentic", "Authentic"),
                        ("Plagal", "Plagal"),
                        ("Phrygian", "Phrygian"),
                        ("CadInCad", "CadInCad"),
                        ("CAD NDLT", "CAD NDLT"),
                        ("NoCadence", "NoCadence")]

CADENCE_ALTER_CHOICES = [("Displaced", "Displaced"),
                         ("Inverted", "Inverted"),
                         ("Incomplete", "Incomplete"),
                         ("Evaded", "Evaded"),
                         ("Doubtful", "Doubtful"),
                         ("Other", "Other")]


class AnalysisForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(AnalysisForm, self).__init__(*args, **kwargs)
        self.piece_id = kwargs['piece_id']
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', "Submit"))

    phrase_number = forms.ModelChoiceField(queryset=DCPhrase.objects.filter(piece_id=self.piece_id).order_by('phrase_num'))
    start_measure = forms.IntegerField()
    stop_measure = forms.IntegerField()
    cadence = forms.BooleanField()
    cadence_kind = forms.ChoiceField(choices=CADENCE_KIND_CHOICES)
    cadence_alter = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=CADENCE_ALTER_CHOICES)
    cadence_role_cantz = forms.CharField()
    cadence_role_tenz = forms.CharField()
    cadence_final_tone = forms.CharField()
    voices_p6_up = forms.CharField()
    voices_p6_lo = forms.CharField()
    voices_p3_up = forms.CharField()
    voices_p3_lo = forms.CharField()
    voices_53_up = forms.CharField()
    voices_53_lo = forms.CharField()
    other_formulas = forms.CharField()
    other_pres_type = forms.CharField()
    voice_role_up1_nim = forms.CharField()
    voice_role_lo1_nim = forms.CharField()
    voice_role_up2_nim = forms.CharField()
    voice_role_lo2_nim = forms.CharField()
    voice_role_dux1 = forms.CharField()
    voice_role_com1 = forms.CharField()
    voice_role_dux2 = forms.CharField()
    voice_role_com2 = forms.CharField()
    voice_role_un_oct = forms.CharField()
    voice_role_fifth = forms.CharField()
    voice_role_fourth = forms.CharField()
    voice_role_above = forms.CharField()
    voice_role_below = forms.CharField()
    other_contrapuntal = forms.CharField()
    text_treatment = forms.CharField()
    repeat_kind = forms.CharField()
    earlier_phrase = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea)
    repeat_exact_varied = forms.CharField()
