import jsonlines
import csv
from sklearn.model_selection import train_test_split


print("Opening .csv files...")
def data_to_jsonl(data, output_jsonl):
    with jsonlines.open(output_jsonl, 'w') as jsonl_file:
        for item in data:
            jsonl_file.write(item)


if _name_ == "_main_":
    en_data = ["en-US.csv"]
    sw_data = ["sw-KE.csv"]
    de_data = ["de-DE.csv"]

    with open('en-US.csv', 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            en_data.append(row)

    with open('sw-KE.csv', 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            sw_data.append(row)

    with open('de-DE.csv', 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            de_data.append(row)



    train_size = 0.7
    dev_size = 0.15
    test_size = 0.15
    print(f'Training Size = {train_size}')
    print(f'Development Size = {dev_size}')
    print(f'Test Size = {test_size}')

    print("Testing, training and developing...")
    en_train, en_test_dev = train_test_split(en_data, test_size=(1 - train_size), random_state=42)
    en_dev, en_test = train_test_split(en_test_dev, test_size=(test_size / (test_size + dev_size)), random_state=42)

    sw_train, sw_test_dev = train_test_split(sw_data, test_size=(1 - train_size), random_state=42)
    sw_dev, sw_test = train_test_split(sw_test_dev, test_size=(test_size / (test_size + dev_size)), random_state=42)

    de_train, de_test_dev = train_test_split(de_data, test_size=(1 - train_size), random_state=42)
    de_dev, de_test = train_test_split(de_test_dev, test_size=(test_size / (test_size + dev_size)), random_state=42)
    data_to_jsonl(en_train, 'en_train.jsonl')
    data_to_jsonl(en_dev, 'en_dev.jsonl')
    data_to_jsonl(en_test, 'en_test.jsonl')

    data_to_jsonl(sw_train, 'sw_train.jsonl')
    data_to_jsonl(sw_dev, 'sw_dev.jsonl')
    data_to_jsonl(sw_test, 'sw_test.jsonl')
    data_to_jsonl(de_train, 'de_train.jsonl')
    data_to_jsonl(de_dev, 'de_dev.jsonl')
    data_to_jsonl(de_test, 'de_test.jsonl')




languages = ['en', 'sw', 'de']

combined_data = []

for lang in languages:
    with jsonlines.open(f'{lang}_train.jsonl', 'r') as jsonl_file:
        for item in jsonl_file:
            combined_data.append({
                'lang': lang,
                'id': item['id'],
                'utt': item['utt']
            })
print("Creating combined train data .jsonl file...")

with jsonlines.open('combined_train_data.jsonl', 'w') as jsonl_file:
    for item in combined_data:
        jsonl_file.write(item)
print("Creating pretty combined train data .jsonl file...")

with jsonlines.open('combined_train_data_pretty.jsonl', 'w') as jsonl_file:
    for item in combined_data:
        jsonl_file.write(item)
