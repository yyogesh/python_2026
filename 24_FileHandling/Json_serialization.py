# Python	JSON
# dict	object
# list	array
# str	string
# int	number
# float	number
# True	true
# False	false
# None	null


from datetime import datetime
import json


class DataEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


json.dumps({
    "name": "Rahul",
    "age": 25,
    "active": True,
    "last_login": datetime
}, cls=DataEncoder)

