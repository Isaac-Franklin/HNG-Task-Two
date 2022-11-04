# # imporr packages to read csv file and write a new json file
# import csv
# import json


# def make_json(csvFilePath, jsonFilePath):

#     data = {}

#     # read scv file and add to data
#     with open(csvFilePath) as csvFile:
#         csvReader = csv.DictReader(csvFile)
#         for rows in csvReader:
#             key = rows['TEAM NAMES']
#             data[key] = rows

#     # create new json file and write data in it
#     with open(jsonFilePath, 'w') as jsonFile:
#         # make file more readable now
#         jsonFile.write(json.dumps(data, indent=4))


# ////////////////////////

import pandas as pd
df = pd.read_csv(r'HNGi9 CSV FILE.csv')
df.to_json(r'HNGJsonDataFile.json')


# //////////////////////////

# fi = open('Untitled-1.json', 'r')
# lines = fi.readlines()

# x = lines[0].split(",")

# for i in range(1, len(lines)):
#     y = lines[i].split(",")
#     data = {}
#     # data = {x[0]: y[0], x[1]: y[1], x[2]: y[2], x[3]: y[3], x[4]: y[4], x[5]: y[5], x[6]: y[6], x[7]: y[7], x[8].replace("\n", ""): y[8].replace("\n", "")}
#     fo = open('Team'+str(1)+'.json', 'w+')
#     fo.write(str(data))
#     fo.close()
# fo.close()


csvFilePath = r'HNGi9 CSV FILE.csv'
jsonFilePath = r'HNGJsonDataFile.json'

make_json(csvFilePath, jsonFilePath)
