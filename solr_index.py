#!/usr/bin/env python
import os
import sys
import solr
import uuid

def expand_voice(voice):
    if not voice:
        return None

    if voice.lower() == "t":
        return "Tenor"
    elif voice.lower() == "ct":
        return "Contratenor"
    elif voice.lower() == "s":
        return "Superius"
    elif voice.lower() == "b":
        return "Bassus"
    else:
        return voice

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "duchemin.settings")
    from duchemin.models.analysis import DCAnalysis
    from duchemin.models.book import DCBook
    from duchemin.models.piece import DCPiece

    solrconn = solr.SolrConnection("http://localhost:8080/duchemin-solr")

    pieces = DCPiece.objects.all()

    all_pieces = []
    for piece in pieces:
        # fix the composer name
        composer_name = ""
        if piece.composer_id.given_name != "":
            composer_name = u"{0}, {1}".format(piece.composer_id.surname, piece.composer_id.given_name)
        else:
            composer_name = u"{0}".format(piece.composer_id.surname)

        d = {
            'type': 'duchemin_piece',
            'id': str(uuid.uuid4()),
            'piece_id': piece.piece_id,
            'book_title': piece.book_id.title,
            'title': piece.title,
            'composer': composer_name
        }

        all_pieces.append(d)
    solrconn.add_many(all_pieces)
    solrconn.commit()
    print "Done adding pieces"

    analyses = DCAnalysis.objects.all()
    for i, analysis in enumerate(analyses):
        contributor_name = ""
        if analysis.analyst.given_name != "":
            contributor_name = u"{0}, {1}".format(analysis.analyst.surname, analysis.analyst.given_name)
        else:
            contributor_name = u"{0}".format(analysis.analyst.surname)

        if analysis.cadence == "Yes":
            cadence = True
        else:
            cadence = False

        if analysis.cadence_alter:
            cadence_alter = [x.strip() for x in analysis.cadence_alter.split(",")]
        else:
            cadence_alter = None

        if analysis.other_contrapuntal:
            other_counterpoint = [x.strip() for x in analysis.other_contrapuntal.split(",")]
        else:
            other_counterpoint = None

        d = {
            'type': 'duchemin_analysis',
            'id': str(uuid.uuid4()),
            'contributor': contributor_name,
            'piece_id': analysis.composition_number.piece_id,
            'phrase_number': analysis.phrase_number.phrase_num,
            'start_measure': analysis.start_measure,
            'stop_measure': analysis.stop_measure,
            'is_cadence': cadence,
            'cadence_kind': analysis.cadence_kind,
            'cadence_alter': cadence_alter,
            'cadence_role_cantz': analysis.cadence_role_cantz,
            'cadence_role_tenz': analysis.cadence_role_tenz,
            'cadence_final_tone': analysis.cadence_final_tone,
            'voices_p6_up': expand_voice(analysis.voices_p6_up),
            'voices_p6_lo': expand_voice(analysis.voices_p6_lo),
            'voices_p3_up': expand_voice(analysis.voices_p3_up),
            'voices_p3_lo': expand_voice(analysis.voices_p3_lo),
            'voices_53_up': expand_voice(analysis.voices_53_up),
            'voices_53_lo': expand_voice(analysis.voices_53_lo),
            'other_formulas': analysis.other_formulas,
            'other_pres_type': analysis.other_pres_type,
            'voice_role_up1_nim': expand_voice(analysis.voice_role_up1_nim),
            'voice_role_lo1_nim': expand_voice(analysis.voice_role_lo1_nim),
            'voice_role_up2_nim': expand_voice(analysis.voice_role_up2_nim),
            'voice_role_lo2_nim': expand_voice(analysis.voice_role_lo2_nim),
            'voice_role_dux1': expand_voice(analysis.voice_role_dux1),
            'voice_role_com1': expand_voice(analysis.voice_role_com1),
            'voice_role_dux2': expand_voice(analysis.voice_role_dux2),
            'voice_role_com2': expand_voice(analysis.voice_role_com2),
            'voice_role_un_oct': expand_voice(analysis.voice_role_un_oct),
            'voice_role_fifth': expand_voice(analysis.voice_role_fifth),
            'voice_role_fourth': expand_voice(analysis.voice_role_fourth),
            'voice_role_above': expand_voice(analysis.voice_role_above),
            'voice_role_below': expand_voice(analysis.voice_role_below),
            'other_contrapuntal': other_counterpoint,
            'text_treatment': analysis.text_treatment,
            'repeat_kind': analysis.repeat_kind,
            'earlier_phrase': analysis.earlier_phrase,
            'comment': analysis.comment,
            'repeat_exact_varied': analysis.repeat_exact_varied
        }
        # print d
        solrconn.add(**d)
        if i % 100 == 0:
            solrconn.commit()
    solrconn.commit()
    print "Done adding analyses"
