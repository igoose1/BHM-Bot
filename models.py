from peewee import *

db = SqliteDatabase('data.db')


class Admin(Model):
	telegram_id = IntegerField()
	state = CharField(max_length=64, null=True)

	class Meta:
		database = db


class Post(Model):
	photos = CharField(max_length=1024, null=True, default='[]')
	name = CharField(max_length=128, default='')
	year = CharField(max_length=8, null=True, default='1970')
	regisseur = CharField(max_length=128, null=True, default='')
	overview = TextField(default='')
	conclusion = TextField(null=True, default='')
	author = ForeignKeyField(Admin, default='')

	class Meta:
		database = db


def create_tables():
	model_tuple = (Post, Admin)
	db.create_tables(model_tuple)

