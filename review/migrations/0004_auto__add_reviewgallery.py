# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ReviewGallery'
        db.create_table(u'review_reviewgallery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('review', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['review.Review'])),
        ))
        db.send_create_signal(u'review', ['ReviewGallery'])


    def backwards(self, orm):
        # Deleting model 'ReviewGallery'
        db.delete_table(u'review_reviewgallery')


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
        },
        u'review.reviewgallery': {
            'Meta': {'object_name': 'ReviewGallery'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'review': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['review.Review']"})
        }
    }

    complete_apps = ['review']