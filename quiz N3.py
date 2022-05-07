import requests
import json
import sqlite3


key = 'f2956a2aa820fa5f48e5af767ba75888'

city = input('::შეიყვანეთ სასურველი ქალაქი:')
lat = input('::შეიყვანეთ სასურველი ქალაქის გრძედი:')
lon = input('::შეიყვანეთ სასურველი ქალაქის განედი:')

r = requests.get(f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={key}')
# print(r.status_code)
# print(r.headers)



j = json.loads(r.text)

jf = json.dumps(j,indent=4)
# print(jf)

# with open('d.json','w') as file:         #-> ინახავს json ფორმატის ფაილში.
#     file.write(jf)



# print("!!no2-ს მაჩვენებელია:",j['list'][0]['components']['no2'],'PPB')
# print("!!pm10-ის მაჩვენებელია:",j['list'][0]['components']['pm10'] ,'μg/m3')           #-> ამოწერს სასურველი ქალაქის ჰაერის დაბინძურების ინდექსს და ჰაერში შემავალი 3 კომპონენტის რაოდენობას.
# print("!!o3-ის მაჩვენებელია:",j['list'][0]['components']['o3'],'PPB')
# print("!!დაბინძურების ინდექსი:",j['list'][0]['main']['aqi'])




conn = sqlite3.connect("newbase.sqlite")
curs = conn.cursor()

no = j['list'][0]['components']['no2']
pm = j['list'][0]['components']['pm10']
o3 = j['list'][0]['components']['o3']
aqi = j['list'][0]['main']['aqi']


#curs.execute('''CREATE TABLE airpollution(id INTEGER PRIMARY KEY AUTOINCREMENT,City VARCHAR(50), Latitude FLOAT , Longitude FLOAT ,No2 FLOAT ,Pm10 FLOAT,o3 FLOAT , Aqi FLOAT );''')

curs.execute('INSERT INTO airpollution (City, Latitude, Longitude, No2, Pm10, o3, Aqi) VALUES (?,?,?,?,?,?,?)',(city,lat,lon, no, pm, o3, aqi))
conn.commit()



conn.close()
