# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Portfolio.link'
        db.delete_column(u'portfolio_portfolio', 'link')

        # Adding field 'Portfolio.slug'
        db.add_column(u'portfolio_portfolio', 'slug',
                      self.gf('autoslug.fields.AutoSlugField')(default='default', unique_with=(), max_length=50, populate_from=None),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Portfolio.link'
        db.add_column(u'portfolio_portfolio', 'link',
                      self.gf('django.db.models.fields.CharField')(default='link', max_length=155),
                      keep_default=False)

        # Deleting field 'Portfolio.slug'
        db.delete_column(u'portfolio_portfolio', 'slug')


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
            'main_choice': ('django.db.models.fields.CharField', [], {'default': "'notmain'", 'max_length': '7'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'default': "'default'", 'unique_with': '()', 'max_length': '50', 'populate_from': 'None'}),
            'text': ('ckeditor.fields.RichTextField', [], {})
        }
    }

    complete_apps = ['portfolio']