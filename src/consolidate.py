import json
import csv

def consolidate():
	json_data = None

	with open("./src/national_county.txt", "rb") as fips:
		reader = csv.reader(fips)
		mapping = dict()

		for row in reader:
			mapping[int(row[1] + row[2])] = {
				"county": row[3],
				"state": row[0]
			}

		json_data = json.dumps(mapping, ensure_ascii=False)

	with open('./public/scripts/testData.json', 'w') as outfile:
		json.dump(json_data, outfile)

consolidate()
