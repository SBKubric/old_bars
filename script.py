import json, math

with open('Бары.json') as data_file:
    data = json.load(data_file)

print('Enter the latitude:')
latitude = float(input())
print('Enter the longitude:')
longitude = float(input())

min = (data[0]['Cells']['Name'], data[0]['Cells']['SeatsCount'])
max = (data[0]['Cells']['Name'], data[0]['Cells']['SeatsCount'])


def distance(f1, f2, l1, l2):
    R = 6.371

    f1 = math.radians(f1)
    f2 = math.radians(f2)
    df = math.radians(f2 - f1)
    dl = math.radians(l2 - l1)

    a = math.sin(df/2)**2 + math.cos(f1)*math.cos(f2)*(math.sin(dl/2)**2)
    c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R*c

nearest = {'name': data[0]['Cells']['Name'],
           'dist': distance(
               latitude,
               float(data[0]['Cells']['geoData']['coordinates'][0]),
               longitude,
               float(data[0]['Cells']['geoData']['coordinates'][1]),
           ),
           }

for json_object in data:
        if min[1] > json_object['Cells']['SeatsCount']:
            min = (json_object['Cells']['Name'], json_object['Cells']['SeatsCount'])
        if max[1] < json_object['Cells']['SeatsCount']:
            max = (json_object['Cells']['Name'], json_object['Cells']['SeatsCount'])
        if nearest['dist'] > distance(latitude, float(json_object['Cells']['geoData']['coordinates'][0]), longitude, float(json_object['Cells']['geoData']['coordinates'][1])):
            nearest['name'] = json_object['Cells']['Name']
            nearest['dist'] = distance(latitude, float(json_object['Cells']['geoData']['coordinates'][0]), longitude, float(json_object['Cells']['geoData']['coordinates'][1]))

print('The smallest place is "' + min[0] + '"')
print('The largest place is "' + max[0] + '"')
print('The nearest place is "' + nearest['name'] + '"')