import requests

city = input('Введите ваш город: ')
url = [0]
chTime = '09'
j = 0
t = [0, 0, 0, 0, 0]

url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&' \
      'units=metric&appid=85c970c1b634e9490ca1066630e55379'.format(city)

resWeath = requests.get(url)
data = resWeath.json()

for i in range(40):
    chDate = data['list'][i]['dt_txt']
    if chDate[-8:-6]==chTime:
        temp = data['list'][i]['main']['temp']
        t[j] = float(temp)
        j = j + 1
        print('Дата/Время: {}'.format(chDate))
        print('Температура : {} C'.format(temp))

print()
maxTemp = str(max(t))
srTemp = str(sum(t)/5)
print('Максимальая темп: {}'.format(maxTemp))
print('Среднее значение: {}'.format(srTemp))