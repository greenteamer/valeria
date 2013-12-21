# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.post_in_blue'
        db.add_column(u'blog_post', 'post_in_blue',
                      self.gf('django.db.models.fields.CharField')(default='noblue', max_length=7),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Post.post_in_blue'
        db.delete_column(u'blog_post', 'post_in_blue')


    models = {
        u'blog.post': {
            'Meta': {'object_name': 'Post'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'post_in_blue': ('django.db.models.fields.CharField', [], {'default': "'noblue'", 'max_length': '7'}),
            'post_in_main': ('django.db.models.fields.CharField', [], {'default': "'notmain'", 'max_length': '7'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'default': "'default'", 'unique_with': '()', 'max_length': '50', 'populate_from': 'None'}),
            'text': ('ckeditor.fields.RichTextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['blog']