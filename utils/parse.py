import re


def str_to_dict(raw_string):
    decode_string = raw_string.value.decode('UTF-8')

    sub_string = re.sub("{|}|Struct", "", decode_string)

    # using strip() and split()  methods
    dict_result = dict((a.strip(), b.strip()) for a, b in (
        element.split('=') for element in sub_string.split(',')))
    
    return dict_result