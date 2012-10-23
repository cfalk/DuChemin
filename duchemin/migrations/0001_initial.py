# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DCPerson'
        db.create_table('duchemin_dcperson', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person_id', self.gf('django.db.models.fields.CharField')(max_length=16, unique=True, null=True)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('given_name', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('birth_date', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('death_date', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('active_date', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('alt_spelling', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('remarks', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('duchemin', ['DCPerson'])

        # Adding model 'DCBook'
        db.create_table('duchemin_dcbook', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('complete_title', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('publisher', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('place_publication', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('volumes', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('part_st_id', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('part_tb_id', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('num_compositions', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('num_pages', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('rism', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('cesr', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('remarks', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
        ))
        db.send_create_signal('duchemin', ['DCBook'])

        # Adding model 'DCPiece'
        db.create_table('duchemin_dcpiece', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('piece_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=16)),
            ('book_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['duchemin.DCBook'], to_field='book_id')),
            ('book_position', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('composer_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['duchemin.DCPerson'], to_field='person_id')),
            ('composer_src', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('forces', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('print_concordances', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('ms_concordances', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
        ))
        db.send_create_signal('duchemin', ['DCPiece'])

        # Adding model 'DCPhrase'
        db.create_table('duchemin_dcphrase', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phrase_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=16)),
            ('piece_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['duchemin.DCPiece'], to_field='piece_id')),
            ('phrase_num', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('phrase_start', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('phrase_stop', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('phrase_text', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('rhyme', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
        ))
        db.send_create_signal('duchemin', ['DCPhrase'])

        # Adding model 'DCAnalysis'
        db.create_table('duchemin_dcanalysis', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timestamp', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('analyst', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['duchemin.DCPerson'], to_field='person_id')),
            ('composition_number', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['duchemin.DCPiece'], to_field='piece_id')),
            ('phrase_number', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['duchemin.DCPhrase'], to_field='phrase_id')),
            ('start_measure', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('stop_measure', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cadence', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('cadence_kind', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('cadence_alter', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('cadence_role_cantz', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('cadence_role_tenz', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('cadence_final_tone', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('voices_p6_up', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('voices_p6_lo', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('voices_p3_up', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('voices_p3_lo', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('voices_53_up', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('voices_53_lo', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('other_formulas', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('other_pres_type', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('voice_role_up1_nim', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('voice_role_lo1_nim', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('voice_role_up2_nim', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('voice_role_lo2_nim', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('voice_role_dux1', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('voice_role_com1', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('voice_role_dux2', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('voice_role_com2', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('voice_role_un_oct', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('voice_role_fifth', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('voice_role_fourth', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('voice_role_above', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('voice_role_below', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('other_contrapuntal', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('text_treatment', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('repeat_kind', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('earlier_phrase', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('repeat_exact_varied', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
        ))
        db.send_create_signal('duchemin', ['DCAnalysis'])

        # Adding model 'DCReconstruction'
        db.create_table('duchemin_dcreconstruction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('piece', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['duchemin.DCPiece'], to_field='piece_id')),
            ('reconstructor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['duchemin.DCPerson'], to_field='person_id')),
        ))
        db.send_create_signal('duchemin', ['DCReconstruction'])

        # Adding model 'DCUserProfile'
        db.create_table('duchemin_dcuserprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal('duchemin', ['DCUserProfile'])

        # Adding M2M table for field favourited_piece on 'DCUserProfile'
        db.create_table('duchemin_dcuserprofile_favourited_piece', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dcuserprofile', models.ForeignKey(orm['duchemin.dcuserprofile'], null=False)),
            ('dcpiece', models.ForeignKey(orm['duchemin.dcpiece'], null=False))
        ))
        db.create_unique('duchemin_dcuserprofile_favourited_piece', ['dcuserprofile_id', 'dcpiece_id'])

        # Adding M2M table for field favourited_analysis on 'DCUserProfile'
        db.create_table('duchemin_dcuserprofile_favourited_analysis', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dcuserprofile', models.ForeignKey(orm['duchemin.dcuserprofile'], null=False)),
            ('dcanalysis', models.ForeignKey(orm['duchemin.dcanalysis'], null=False))
        ))
        db.create_unique('duchemin_dcuserprofile_favourited_analysis', ['dcuserprofile_id', 'dcanalysis_id'])

        # Adding M2M table for field favourited_reconstruction on 'DCUserProfile'
        db.create_table('duchemin_dcuserprofile_favourited_reconstruction', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dcuserprofile', models.ForeignKey(orm['duchemin.dcuserprofile'], null=False)),
            ('dcreconstruction', models.ForeignKey(orm['duchemin.dcreconstruction'], null=False))
        ))
        db.create_unique('duchemin_dcuserprofile_favourited_reconstruction', ['dcuserprofile_id', 'dcreconstruction_id'])


    def backwards(self, orm):
        # Deleting model 'DCPerson'
        db.delete_table('duchemin_dcperson')

        # Deleting model 'DCBook'
        db.delete_table('duchemin_dcbook')

        # Deleting model 'DCPiece'
        db.delete_table('duchemin_dcpiece')

        # Deleting model 'DCPhrase'
        db.delete_table('duchemin_dcphrase')

        # Deleting model 'DCAnalysis'
        db.delete_table('duchemin_dcanalysis')

        # Deleting model 'DCReconstruction'
        db.delete_table('duchemin_dcreconstruction')

        # Deleting model 'DCUserProfile'
        db.delete_table('duchemin_dcuserprofile')

        # Removing M2M table for field favourited_piece on 'DCUserProfile'
        db.delete_table('duchemin_dcuserprofile_favourited_piece')

        # Removing M2M table for field favourited_analysis on 'DCUserProfile'
        db.delete_table('duchemin_dcuserprofile_favourited_analysis')

        # Removing M2M table for field favourited_reconstruction on 'DCUserProfile'
        db.delete_table('duchemin_dcuserprofile_favourited_reconstruction')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'duchemin.dcanalysis': {
            'Meta': {'object_name': 'DCAnalysis'},
            'analyst': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['duchemin.DCPerson']", 'to_field': "'person_id'"}),
            'cadence': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'cadence_alter': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'cadence_final_tone': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'cadence_kind': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'cadence_role_cantz': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'cadence_role_tenz': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'composition_number': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['duchemin.DCPiece']", 'to_field': "'piece_id'"}),
            'earlier_phrase': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'other_contrapuntal': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'other_formulas': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'other_pres_type': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'phrase_number': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['duchemin.DCPhrase']", 'to_field': "'phrase_id'"}),
            'repeat_exact_varied': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'repeat_kind': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'start_measure': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'stop_measure': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'text_treatment': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'voice_role_above': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'voice_role_below': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'voice_role_com1': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'voice_role_com2': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'voice_role_dux1': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'voice_role_dux2': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'voice_role_fifth': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'voice_role_fourth': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'voice_role_lo1_nim': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'voice_role_lo2_nim': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'voice_role_un_oct': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'voice_role_up1_nim': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'voice_role_up2_nim': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'voices_53_lo': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'voices_53_up': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'voices_p3_lo': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'voices_p3_up': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'voices_p6_lo': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'voices_p6_up': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'})
        },
        'duchemin.dcbook': {
            'Meta': {'object_name': 'DCBook'},
            'book_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'cesr': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'complete_title': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'num_compositions': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'num_pages': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'part_st_id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'part_tb_id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'place_publication': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'rism': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'volumes': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        'duchemin.dcperson': {
            'Meta': {'object_name': 'DCPerson'},
            'active_date': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'alt_spelling': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'birth_date': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'death_date': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'given_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person_id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'unique': 'True', 'null': 'True'}),
            'remarks': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        'duchemin.dcphrase': {
            'Meta': {'object_name': 'DCPhrase'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phrase_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'}),
            'phrase_num': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'phrase_start': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'phrase_stop': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'phrase_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'piece_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['duchemin.DCPiece']", 'to_field': "'piece_id'"}),
            'rhyme': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        'duchemin.dcpiece': {
            'Meta': {'object_name': 'DCPiece'},
            'book_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['duchemin.DCBook']", 'to_field': "'book_id'"}),
            'book_position': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'composer_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['duchemin.DCPerson']", 'to_field': "'person_id'"}),
            'composer_src': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'forces': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ms_concordances': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'piece_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'}),
            'print_concordances': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        'duchemin.dcreconstruction': {
            'Meta': {'object_name': 'DCReconstruction'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'piece': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['duchemin.DCPiece']", 'to_field': "'piece_id'"}),
            'reconstructor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['duchemin.DCPerson']", 'to_field': "'person_id'"})
        },
        'duchemin.dcuserprofile': {
            'Meta': {'object_name': 'DCUserProfile'},
            'favourited_analysis': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['duchemin.DCAnalysis']", 'symmetrical': 'False'}),
            'favourited_piece': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['duchemin.DCPiece']", 'symmetrical': 'False'}),
            'favourited_reconstruction': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['duchemin.DCReconstruction']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['duchemin']