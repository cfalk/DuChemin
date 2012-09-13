import argparse
import os
import json
import csv


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_directory")
    parser.add_argument("output_directory")
    args = parser.parse_args()

    people = os.path.join(args.input_directory, "People.csv")
    analyses = os.path.join(args.input_directory, "Analyses.csv")
    pieces = os.path.join(args.input_directory, "Pieces.csv")
    books = os.path.join(args.input_directory, "Books.csv")
    reconstructions = os.path.join(args.input_directory, "Reconstructions.csv")


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
