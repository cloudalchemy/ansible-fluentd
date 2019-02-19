from ansible.module_utils._text import to_text
from collections import OrderedDict

def fluentd_params_to_text(params):
    config = ""
    if type(params) == dict:
        params = OrderedDict(sorted(params.items(), key=lambda x: x[0], reverse=True))
    else:
        raise ValueError("Params should be dictionary")
    for key, val in params.items():
        if key == "type":
            key = "@type"
        if type(val) is list:
            if all([type(x) == dict for x in val]):
                for v in val:
                    config += "<{0}>\n  {1}</{0}>\n  ".format(key, params_to_text(v))
            else:
                config += "{0} {1}\n  ".format(key, val.join(', '))
        elif type(val) is dict:
            config += "<{0}>\n  {1}</{0}>\n  ".format(key, params_to_text(val))
        else:
            config += "{0} {1}\n  ".format(key, val)
            
    return to_text(config)


class FilterModule(object):


   def filters(self):
       return {'fluentd_params_to_text': fluentd_params_to_text } 
