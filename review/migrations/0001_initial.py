# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Review'
        db.create_table(u'review_review', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=155)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('text', self.gf('ckeditor.fields.RichTextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
            ('main_choice', self.gf('django.db.models.fields.CharField')(default='notmain', max_length=7)),
        ))
        db.send_create_signal(u'review', ['Review'])


    def backwards(self, orm):
        # Deleting model 'Review'
        db.delete_table(u'review_review')


    models = {
        u'review.review': {
            'Meta': {'object_name': 'Review'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'main_choice': ('django.db.models.fields.CharField', [], {'default': "'notmain'", 'max_length': '7'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '155'}),
            'text': ('ckeditor.fields.RichTextField', [], {})
        }
    }

    complete_apps = ['review']