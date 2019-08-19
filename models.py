from peewee import *

db = SqliteDatabase('data.db')


class Post(Model):
	photos = CharField(max_length=1024, null=True)
	name = CharField(max_length=128)
	year = IntegerField(null=True)
	regisseur = CharField(max_length=128, null=True)
	overview = TextField()
	conclusion = TextField(null=True)

	class Meta:
		database = db


class Admin(Model):
	telegram_id = IntegerField()
	state = CharField(max_length=64, null=True)

	class Meta:
		database = db


def create_tables():
	model_tuple = (Post, Admin)
	db.create_tables(model_tuple)

