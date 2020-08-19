from pynamodb.attributes import UnicodeAttribute, ListAttribute, MapAttribute
from pynamodb.models import Model

"""Every search_request -> several search results, -> several search entries"""


class BaseModel(Model):
    def to_dict(self):
        rval = {}
        for key in self.attribute_values:
            rval[key] = self.__getattribute__(key)
        return rval


class Results(MapAttribute):
    name = UnicodeAttribute(null=False)
    url = UnicodeAttribute(null=False)


class SearchRequests(BaseModel):
    class Meta:
        table_name = 'SearchRequests'
        host = None
        aws_access_key_id = "anything"
        aws_secret_access_key = "fake"

    query = UnicodeAttribute(hash_key=True)
    results = ListAttribute(of=Results)
