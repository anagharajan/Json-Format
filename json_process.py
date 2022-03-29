import json

file = open('data.json')
inputData  = json.load(file)
expectedData = []
dict_key = []

#getting region list
#to get key
dim_id = list(inputData['dimensions'])[0]['id']
meta = inputData['metadata']
for entry in meta:
    if entry['id'] == dim_id:
        out_label = entry['label']
        # print(out_label)

region_list = list(inputData['dimensions'])[0]['values']
#getting county list
county_list = list(inputData['dimensions'])[1]['values']

sales_list = list(inputData['meaures'])[0]['values']
quantity_list = list(inputData['meaures'])[1]['values']
profit_list = list(inputData['meaures'])[2]['values']

#Result json format
for i in range(len(county_list)):
    expectedData.append({
        'Region': region_list[i],
        'County': county_list[i],
        'Sales': sales_list[i],
        'Quantity': quantity_list[i],
        'Profit': profit_list[i]
    })
print(json.dumps(expectedData))
