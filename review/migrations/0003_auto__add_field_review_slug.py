# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Review.slug'
        db.add_column(u'review_review', 'slug',
                      self.gf('autoslug.fields.AutoSlugField')(default='default', unique_with=(), max_length=50, populate_from=None),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Review.slug'
        db.delete_column(u'review_review', 'slug')


    models = {
        u'review.review': {
            'Meta': {'object_name': 'Review'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '155', 'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'main_choice': ('django.db.models.fields.CharField', [], {'default': "'notmain'", 'max_length': '7'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '155'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'default': "'default'", 'unique_with': '()', 'max_length': '50', 'populate_from': 'None'}),
            'text': ('ckeditor.fields.RichTextField', [], {})
        }
    }

    complete_apps = ['review']