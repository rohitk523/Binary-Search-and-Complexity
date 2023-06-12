from binary_search import locate_card
from test_cases import tests

for i in tests:
    if locate_card(**i['input']) == i['output']:
        print("passed")
    else:
        print('failed')