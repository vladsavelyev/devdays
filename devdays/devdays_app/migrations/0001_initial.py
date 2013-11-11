# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Comment'
        db.create_table('devdays_app_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=20000, null=True, blank=True)),
        ))
        db.send_create_signal('devdays_app', ['Comment'])

        # Adding model 'Group'
        db.create_table('devdays_app_group', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('devdays_app', ['Group'])

        # Adding model 'Role'
        db.create_table('devdays_app_role', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal('devdays_app', ['Role'])

        # Adding model 'UserProfile'
        db.create_table('devdays_app_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['devdays_app.Group'], null=True, blank=True)),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['devdays_app.Role'], null=True, blank=True)),
        ))
        db.send_create_signal('devdays_app', ['UserProfile'])

        # Adding model 'Idea'
        db.create_table('devdays_app_idea', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=30000, null=True, blank=True)),
            ('autor', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='AutorUserProfile', null=True, to=orm['devdays_app.UserProfile'])),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
        ))
        db.send_create_signal('devdays_app', ['Idea'])

        # Adding M2M table for field likes on 'Idea'
        m2m_table_name = db.shorten_name('devdays_app_idea_likes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('idea', models.ForeignKey(orm['devdays_app.idea'], null=False)),
            ('userprofile', models.ForeignKey(orm['devdays_app.userprofile'], null=False))
        ))
        db.create_unique(m2m_table_name, ['idea_id', 'userprofile_id'])

        # Adding model 'Event'
        db.create_table('devdays_app_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('devdays_app', ['Event'])

        # Adding model 'Project'
        db.create_table('devdays_app_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idea', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['devdays_app.Idea'], null=True, blank=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['devdays_app.Event'], null=True, blank=True)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
        ))
        db.send_create_signal('devdays_app', ['Project'])

        # Adding M2M table for field students on 'Project'
        m2m_table_name = db.shorten_name('devdays_app_project_students')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['devdays_app.project'], null=False)),
            ('userprofile', models.ForeignKey(orm['devdays_app.userprofile'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'userprofile_id'])

        # Adding M2M table for field comments on 'Project'
        m2m_table_name = db.shorten_name('devdays_app_project_comments')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['devdays_app.project'], null=False)),
            ('comment', models.ForeignKey(orm['devdays_app.comment'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'comment_id'])


    def backwards(self, orm):
        # Deleting model 'Comment'
        db.delete_table('devdays_app_comment')

        # Deleting model 'Group'
        db.delete_table('devdays_app_group')

        # Deleting model 'Role'
        db.delete_table('devdays_app_role')

        # Deleting model 'UserProfile'
        db.delete_table('devdays_app_userprofile')

        # Deleting model 'Idea'
        db.delete_table('devdays_app_idea')

        # Removing M2M table for field likes on 'Idea'
        db.delete_table(db.shorten_name('devdays_app_idea_likes'))

        # Deleting model 'Event'
        db.delete_table('devdays_app_event')

        # Deleting model 'Project'
        db.delete_table('devdays_app_project')

        # Removing M2M table for field students on 'Project'
        db.delete_table(db.shorten_name('devdays_app_project_students'))

        # Removing M2M table for field comments on 'Project'
        db.delete_table(db.shorten_name('devdays_app_project_comments'))


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
        'devdays_app.comment': {
            'Meta': {'object_name': 'Comment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '20000', 'null': 'True', 'blank': 'True'})
        },
        'devdays_app.event': {
            'Meta': {'object_name': 'Event'},
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'devdays_app.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'devdays_app.idea': {
            'Meta': {'object_name': 'Idea'},
            'autor': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'AutorUserProfile'", 'null': 'True', 'to': "orm['devdays_app.UserProfile']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '30000', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'LikeUserProfile'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['devdays_app.UserProfile']"}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        'devdays_app.project': {
            'Meta': {'object_name': 'Project'},
            'comments': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devdays_app.Comment']", 'null': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devdays_app.Event']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idea': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devdays_app.Idea']", 'null': 'True', 'blank': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['devdays_app.UserProfile']", 'null': 'True', 'blank': 'True'})
        },
        'devdays_app.role': {
            'Meta': {'object_name': 'Role'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        'devdays_app.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devdays_app.Group']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['devdays_app.Role']", 'null': 'True', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['devdays_app']