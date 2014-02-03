# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ImageFolio'
        db.create_table(u'portfolio_imagefolio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.Portfolio'])),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'portfolio', ['ImageFolio'])


    def backwards(self, orm):
        # Deleting model 'ImageFolio'
        db.delete_table(u'portfolio_imagefolio')


    models = {
        u'portfolio.imagefolio': {
            'Meta': {'ordering': "['title']", 'object_name': 'ImageFolio'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['portfolio.Portfolio']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'portfolio.portfolio': {
            'Meta': {'object_name': 'Portfolio'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '155'}),
            'main_choice': ('django.db.models.fields.CharField', [], {'default': "'notmain'", 'max_length': '7'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'text': ('ckeditor.fields.RichTextField', [], {})
        }
    }

    complete_apps = ['portfolio']