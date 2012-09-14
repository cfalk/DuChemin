import argparse
import os
import json
import csv
import pdb

analysis_fieldnames = [
    'timestamp',
    'analyst',
    'composition_number',
    'phrase_number',
    'start_measure',
    'stop_measure',
    'cadence',
    'cadence_kind',
    'cadence_alter',
    'cadence_role_cantz',
    'cadence_role_tenz',
    'cadence_final_tone',
    'voices_p6_up',
    'voices_p6_lo',
    'voices_p3_up',
    'voices_p3_lo',
    'voices_53_up',
    'voices_53_lo',
    'other_formulas',
    'other_pres_type',
    'voice_role_up1_nim',
    'voice_role_lo1_nim',
    'voice_role_up2_nim',
    'voice_role_lo2_nim',
    'voice_role_dux1',
    'voice_role_com1',
    'voice_role_dux2',
    'voice_role_com2',
    'voice_role_un_oct',
    'voice_role_fifth',
    'voice_role_fourth',
    'voice_role_above',
    'voice_role_below',
    'other_contrapuntal',
    'text_treatment',
    'repeat_kind',
    'earlier_phrase',
    'comment',
    'repeat_exact_varied'
]

person_fieldnames = [
    'person_id',
    'surname',
    'given_name',
    'birth_date',
    'death_date',
    'active_date',
    'alt_spelling',
    'remarks'
]

phrase_fieldnames = [
    'phrase_id',
    'piece_id',
    'phrase_num',
    'phrase_start',
    'phrase_stop',
    'phrase_text',
    'rhyme'
]

piece_fieldnames = [
    'piece_id',
    'book_id',
    'book_position',
    'title',
    'composer_id',
    'composer_src',
    'forces',
    'print_concordances',
    'ms_concordances',
]

book_fieldnames = [
    'book_id',
    'title',
    'complete_title',
    'publisher',
    'place_publication',
    'date',
    'volumes',
    'part_st_id',
    'part_tb_id',
    'num_compositions',
    'num_pages',
    'location',
    'rism',
    'cesr',
    'remarks'
]


def find_phrase_id(phrase_csv, piece_id, phrase_num):
    """ returns a phrase id given a piece and a phrase number """

    # if the phrase number is unknown, set it to a special phrase
    if phrase_num == "xx":
        return "xx"

    for phrase in phrase_csv:
        if (phrase['piece_id'] == piece_id) and (phrase['phrase_num'] == phrase_num):
            return phrase['phrase_id']

    return "xx"


def find_person_id(people_csv, persname):
    """ returns a person id for a surname"""
    for person in people_csv:
        if person['surname'] == persname:
            return person['person_id']
    return None


def record_cleanup(record):
    for k, v in record.iteritems():
        if v == "":
            record[k] = None
    return record

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_directory")
    parser.add_argument("output_directory")
    args = parser.parse_args()

    people = os.path.join(args.input_directory, "People.csv")
    analyses = os.path.join(args.input_directory, "Analyses.csv")
    pieces = os.path.join(args.input_directory, "Pieces.csv")
    books = os.path.join(args.input_directory, "Books.csv")
    phrases = os.path.join(args.input_directory, "Phrases.csv")
    reconstructions = os.path.join(args.input_directory, "Reconstructions.csv")

    fixtures = []

    people_csv = csv.DictReader(open(people, 'rb'), fieldnames=person_fieldnames)
    people_csv = list(people_csv)  # convert to list for easy searching

    analyses_csv = csv.DictReader(open(analyses, 'rb'), fieldnames=analysis_fieldnames)
    analyses_csv = list(analyses_csv)

    pieces_csv = csv.DictReader(open(pieces, 'rb'), fieldnames=piece_fieldnames)
    pieces_csv = list(pieces_csv)

    book_csv = csv.DictReader(open(books, 'rb'), fieldnames=book_fieldnames)
    book_csv = list(book_csv)

    phrase_csv = csv.DictReader(open(phrases, 'rb'), fieldnames=phrase_fieldnames)
    phrase_csv = list(phrase_csv)

    people_json = []
    for pk, record in enumerate(people_csv):
        if pk == 0:
            continue

        del record[None]
        r = {
            'pk': pk,
            'model': 'duchemin.dcperson',
            'fields': record_cleanup(record)
        }
        people_json.append(r)
    fixtures.extend(people_json)

    phrase_json = []
    for pk, record in enumerate(phrase_csv):
        if pk == 0:
            continue
        del record[None]
        r = {
            'pk': pk,
            'model': 'duchemin.dcphrase',
            'fields': record_cleanup(record)
        }
        phrase_json.append(r)
    fixtures.extend(phrase_json)

    book_json = []
    for pk, record in enumerate(book_csv):
        if pk == 0:
            continue
        r = {
            'pk': pk,
            'model': 'duchemin.dcbook',
            'fields': record_cleanup(record)
        }
        book_json.append(r)
    fixtures.extend(book_json)

    pieces_json = []
    for pk, record in enumerate(pieces_csv):
        if pk == 0:
            continue
        record['composer_id'] = find_person_id(people_csv, record['composer_id'])

        r = {
            'pk': pk,
            'model': 'duchemin.dcpiece',
            'fields': record_cleanup(record)
        }
        pieces_json.append(r)
    fixtures.extend(pieces_json)

    analyses_json = []
    for pk, record in enumerate(analyses_csv):
        if pk == 0:
            continue
        # replace the last name with the id.
        record['analyst'] = find_person_id(people_csv, record['analyst'])
        record['phrase_number'] = find_phrase_id(phrase_csv, record['composition_number'], record['phrase_number'])

        r = {
            'pk': pk,
            'model': 'duchemin.dcanalysis',
            'fields': record_cleanup(record)
        }
        analyses_json.append(r)
    fixtures.extend(analyses_json)

    # print fixtures
    outfile = os.path.join(args.output_directory, 'initial_data.json')
    f = open(outfile, 'w')
    json.dump(fixtures, f)
    f.close()
