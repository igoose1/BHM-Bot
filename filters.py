import models

from telegram.ext import BaseFilter

class IsFilling(BaseFilter):
	def filter(self, message):
		return models.Admin.get(telegram_id=message.from_user.id).state is not None


class IsAdmin(BaseFilter):
	def filter(self, message):
		return models.Admin.get_or_none(telegram_id=message.from_user.id) is not None


class CanBeMissed(BaseFilter):
	def filter(self, message):
		text = message.text
		attr = text[len('conf'):]
		field = getattr(models.Post, attr)
		return field.null
