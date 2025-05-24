import requests
import time

server_url = input('Введите адрес сервера (например, http://192.168.1.10:5000): ').strip()
print('Скрипт будет каждую секунду отправлять координаты на сервер.')
print('Для выхода нажмите Ctrl+C.')

while True:
    try:
        lat = input('Введите широту (lat): ').strip()
        lon = input('Введите долготу (lon): ').strip()
        resp = requests.post(f'{server_url}/update_location', json={'lat': float(lat), 'lon': float(lon)})
        if resp.ok:
            print('⠋ Координаты успешно отправлены!')
        else:
            print('⠙ Ошибка отправки:', resp.text)
        time.sleep(1)
    except KeyboardInterrupt:
        print('\n⠹ Выход из программы.')
        break
    except Exception as e:
        print('⠸ Ошибка:', e)
        time.sleep(1) 