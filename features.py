# -*- coding: utf-8 -*-
property_types = {
    1: {'ro': 'apartamente', 'ru': ''},
    2: {'ro': 'case', 'ru': ''},
    3: {'ro': 'terenuri', 'ru': ''},
    4: {'ro': 'oficii', 'ru': ''},
    5: {'ro': 'spații comerciale', 'ru': ''}
}

offer_types = {
    1: {'ro': 'vânzare', 'ru': ''},
    2: {'ro': 'chirie', 'ru': ''}
}

construction_types = {
    1: {'ro': 'nouă', 'ru': ''},
    2: {'ro': 'veche', 'ru': ''}
}

conditions = {
    1: {'ro': 'varianta albă', 'ru': ''},
    2: {'ro': 'medie', 'ru': ''},
    3: {'ro': 'euroreparație', 'ru': ''}
}
from collections import OrderedDict
def get_locations():
    return OrderedDict(sorted(locations.items(), key=lambda t: t[0]))
locations = OrderedDict()
locations[1] = {'ro': 'mun. Chișinău', 'ru': ''}
locations[100] = {'ro': 'mun. Balti', 'ru': ''}
locations[1]['children'] = OrderedDict()
locations[100]['children'] = OrderedDict()
locations[1]['children']['sectors'] = OrderedDict()
locations[1]['children']['sectors'][2] = {'ro': 'Botanica', 'ru': ''}
locations[1]['children']['sectors'][3] = {'ro': 'Buiucani', 'ru': ''}
locations[1]['children']['sectors'][4] = {'ro': 'Centru', 'ru': ''}
locations[1]['children']['sectors'][5] = {'ro': 'Ciocana', 'ru': ''}
locations[1]['children']['sectors'][6] = {'ro': 'Rîșcani', 'ru': ''}
locations[1]['children']['suburbii'] = OrderedDict()
locations[1]['children']['suburbii'][7] = {'ro': 'Durlești', 'ru': ''}
locations[1]['children']['suburbii'][8] = {'ro': 'Stauceni', 'ru': ''}
locations[1]['children']['suburbii'][9] = {'ro': 'Trușeni', 'ru': ''}
locations[1]['children']['suburbii'][10] = {'ro': 'Tohatin', 'ru': ''}
locations[1]['children']['suburbii'][11] = {'ro': 'Dumbrava', 'ru': ''}
locations[1]['children']['suburbii'][12] = {'ro': 'Bubuieci', 'ru': ''}
locations[1]['children']['suburbii'][13] = {'ro': 'Colonița', 'ru': ''}
locations[1]['children']['suburbii'][14] = {'ro': 'Budești', 'ru': ''}
locations[1]['children']['suburbii'][15] = {'ro': 'Cricova', 'ru': ''}
locations[1]['children']['suburbii'][16] = {'ro': 'Codru', 'ru': ''}
locations[1]['children']['suburbii'][17] = {'ro': 'Sîngera', 'ru': ''}
locations[1]['children']['suburbii'][18] = {'ro': 'Gratiești', 'ru': ''}
locations[1]['children']['suburbii'][19] = {'ro': 'Vadu lui Vodă', 'ru': ''}
locations[1]['children']['suburbii'][20] = {'ro': 'Bacioi', 'ru': ''}
locations[1]['children']['suburbii'][21] = {'ro': 'Cruzești', 'ru': ''}
locations[1]['children']['suburbii'][22] = {'ro': 'Ciorescu', 'ru': ''}
# locations = {
#     1: {'ro': 'mun. Chișinău', 'ru': '', 'children': OrderedDict((
#         'sectors', OrderedDict({
#             2: {'ro': 'Botanica', 'ru': ''},
#             3: {'ro': 'Buiucani', 'ru': ''},
#             4: {'ro': 'Centru', 'ru': ''},
#             5: {'ro': 'Ciocana', 'ru': ''},
#             6: {'ro': 'Rîșcani', 'ru': ''}
#         }),
#         ('suburbii', OrderedDict({
#             7: {'ro': 'Durlești', 'ru': ''},
#             8: {'ro': 'Stauceni', 'ru': ''},
#             9: {'ro': 'Trușeni', 'ru': ''},
#             10: {'ro': 'Tohatin', 'ru': ''},
#             11: {'ro': 'Dumbrava', 'ru': ''},
#             12: {'ro': 'Bubuieci', 'ru': ''},
#             13: {'ro': 'Colonița', 'ru': ''},
#             14: {'ro': 'Budești', 'ru': ''},
#             15: {'ro': 'Cricova', 'ru': ''},
#             16: {'ro': 'Codru', 'ru': ''},
#             17: {'ro': 'Sîngera', 'ru': ''},
#             18: {'ro': 'Gratiești', 'ru': ''},
#             19: {'ro': 'Vadu lui Vodă', 'ru': ''},
#             20: {'ro': 'Bacioi', 'ru': ''},
#             21: {'ro': 'Cruzești', 'ru': ''},
#             22: {'ro': 'Ciorescu', 'ru': ''}
#         })
#     )))},
#     23: {'ro': 'mun. Balti', 'ru': '','children':{}}
# }


def get_extras():
    return list(extras)


extras = [
    {'ru': '', 'ro': u'Supermarket', 'value': False},
    {'ru': '', 'ro': u'Anexă', 'value': False},
    {'ru': '', 'ro': u'Termopan', 'value': False},
    {'ru': '', 'ro': u'Parchet', 'value': False}
]
