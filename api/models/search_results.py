from flask import current_app
from pynamodb.attributes import NumberAttribute, UnicodeAttribute, MapAttribute
from pynamodb.models import Model

class BaseModel(Model):


class SearchEntries(MapAttribute):
    class Meta:
        table_name = 'SearchEntries'
        host = current_app.config['DB_URL']

    name = UnicodeAttribute(null=False)
    url = UnicodeAttribute(null=False)


class SearchResults(MapAttribute):
    class Meta:
        table_name = 'SearchResults'
        host = current_app.config['DB_URL']

    make = UnicodeAttribute(null=False)
    model = UnicodeAttribute(null=True)


"""Every search_request -> several search results, -> several search entries"""


class SearchRequests(Model):
    class Meta:
        table_name = 'SearchRequests'
        host = current_app.config['DB_URL']

    id = NumberAttribute(hash_key=True)
    name = UnicodeAttribute()

    def __repr__(self):
        return "<SearchResults {} name:{}>".format(self.id, self.name)
