import csv
mammoth_data = [] #empty list to store mammoth data
with open('pbdb_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    '''discard the first row as it is a columns heading'''
    columns = reader.__next__()
    '''extract data of col 9, accepted_name, abundance value and abundance unit from 22 and 23
    lat, lng, from columns 24 and 25, state, county from 27 and 28, and geocomment from 32'''
    for row in reader:
        name =row[9]
        abd = row[22]
        abd_unit =row[23]
        lat = float(row[25]) #change to float
        lng = float(row[24]) #change to float
        state = row[27]
        county = row[28]
        comment = row[32]

        mammoth_data.append([name, abd, abd_unit, lat, lng, state, county, comment])

with open('mammoth_data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, quoting =csv.QUOTE_NONNUMERIC)
    writer.writerow(['name', 'abd_unit', 'lat', 'lng', 'state', 'county', 'comment'])
    writer.writerows(mammoth_data)
