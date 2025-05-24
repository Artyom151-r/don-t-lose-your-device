import requests
import time
import subprocess

server_url = input('Введите адрес сервера (например, http://192.168.1.10:5000): ').strip()
print('Скрипт будет каждую секунду отправлять координаты с GPS на сервер.')
print('Для выхода нажмите Ctrl+C.')

def get_gps_location():
    try:
        result = subprocess.run(['termux-location', '--provider', 'gps', '--request', 'once'], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            import json
            data = json.loads(result.stdout)
            return data.get('latitude'), data.get('longitude')
    except Exception as e:
        print('⠸ Ошибка получения GPS:', e)
    return None, None

while True:
    try:
        lat, lon = get_gps_location()
        if lat is not None and lon is not None:
            resp = requests.post(f'{server_url}/update_location', json={'lat': lat, 'lon': lon})
            if resp.ok:
                print(f'⠋ Координаты отправлены: {lat}, {lon}')
            else:
                print('⠙ Ошибка отправки:', resp.text)
        else:
            print('⠸ Не удалось получить координаты с GPS')
        time.sleep(1)
    except KeyboardInterrupt:
        print('\n⠹ Выход из программы.')
        break
    except Exception as e:
        print('⠸ Ошибка:', e)
        time.sleep(1) 