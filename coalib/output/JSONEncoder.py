import collections
import json
import re
from datetime import datetime

from coala_utils.decorators import get_public_members
from coalib.settings.FunctionMetadata import FunctionMetadata

branch_coverage = {
    "create_json_encoder_1": False,  # hasattr(obj, '__json__')
    "create_json_encoder_2": False,  # isinstance(obj, collections.Iterable)
    "create_json_encoder_3": False,  # isinstance(obj, datetime)
    "create_json_encoder_4": False,  # hasattr(obj, '__getitem__') and hasattr(obj, 'keys')
    "create_json_encoder_5": False,  # hasattr(obj, '__dict__')
    "create_json_encoder_6": False,  # isinstance(obj, re._pattern_type)
    "create_json_encoder_7": False,  # default fallback
}

def create_json_encoder(**kwargs):
    class JSONEncoder(json.JSONEncoder):

        @classmethod
        def _filter_params(cls, op, nop):
            params = set(op) | set(nop)
            return {key: kwargs[key] for key in set(kwargs) & params}

        def default(self, obj):
            global branch_coverage

            if hasattr(obj, '__json__'):
                fdata = FunctionMetadata.from_function(obj.__json__)
                params = self._filter_params(
                    fdata.optional_params, fdata.non_optional_params)
                branch_coverage["create_json_encoder_1"] = True
                return obj.__json__(**params)
            elif isinstance(obj, collections.Iterable):
                branch_coverage["create_json_encoder_2"] = True
                return list(obj)
            elif isinstance(obj, datetime):
                branch_coverage["create_json_encoder_3"] = True
                return obj.isoformat()
            elif hasattr(obj, '__getitem__') and hasattr(obj, 'keys'):
                branch_coverage["create_json_encoder_4"] = True
                return dict(obj)
            elif hasattr(obj, '__dict__'):
                branch_coverage["create_json_encoder_5"] = True
                return {member: getattr(obj, member)
                        for member in get_public_members(obj)}
            elif isinstance(obj, re._pattern_type):
                branch_coverage["create_json_encoder_6"] = True
                return obj.pattern

            branch_coverage["create_json_encoder_7"] = True
            return json.JSONEncoder.default(self, obj)
    return JSONEncoder
