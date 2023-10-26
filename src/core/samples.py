import pandas as pd
import json

file_path = '/Users/hatem/Documents/dev/BERT_SEC/src/core/sample.json' 

with open(file_path, 'r') as json_file:
    data = json.load(json_file)['facts']


def find_arrays(data):
    if isinstance(data, list):
        return data
    elif isinstance(data, dict):
        arrays = []
        for key, value in data.items():
            if isinstance(value, (list, dict)):
                arrays.extend(find_arrays(value))
        return arrays
    return []


def format_fact_(facts, fact):
    concept = facts[fact]
    _keys = list(concept.keys())
    concept_dataframes = []
    for k in _keys:
        shares = pd.DataFrame(find_arrays(concept[k]))
        shares['label'] = k
        concept_dataframes.append(shares)
    return concept_dataframes


def format_test(facts):
    dei = facts['dei']
    us_gaap = facts['us-gaap']
    dei_keys = list(dei.keys())
    x = pd.DataFrame((find_arrays(
        dei[dei_keys[0]]
    )))
    print(x)
    
    # print(pd.DataFrame.from_dict(dei[dei_keys[0]]['units']['shares']))
    



print(format_fact_(data, 'dei'))