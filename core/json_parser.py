class JsonParser:

    def __init__(self, json_object):
        self._object = json_object

    @property
    def message(self):
        return self._object['message']

    @property
    def code(self):
        return self._object['code']

    @property
    def count(self):
        return self._object['count']

    @property
    def source(self):
        return self._object['signature']['source']

    @property
    def version(self):
        return self._object['signature']['version']

    @property
    def fields(self):
        return self._object['fields']

    @property
    def data(self):
        return self._object['data']