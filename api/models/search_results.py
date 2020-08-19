from flask import current_app
from pynamodb.attributes import NumberAttribute, UnicodeAttribute
from pynamodb.models import Model


class User(Model):
    class Meta:
        table_name = 'User'
        host = current_app.config['DB_URL']

    id = NumberAttribute(hash_key=True)
    name = UnicodeAttribute()

    def __repr__(self):
        return "<User {} name:{}>".format(self.id, self.name)
