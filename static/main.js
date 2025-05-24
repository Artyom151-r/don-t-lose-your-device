// Отображение карты
const map = L.map('map').setView([initialLat, initialLon], 15);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap'
}).addTo(map);

let marker = L.marker([initialLat, initialLon]).addTo(map);

// Функция для отправки координат на сервер
function sendLocation(lat, lon) {
    fetch('/update_location', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ lat, lon })
    });
}

// Пример: получить координаты с устройства и отправить
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;
        marker.setLatLng([lat, lon]);
        map.setView([lat, lon], 15);
        sendLocation(lat, lon);
    });
}

// Функция для обновления маркера с сервера
function updateMarkerFromServer() {
    fetch('/location')
        .then(res => res.json())
        .then(data => {
            marker.setLatLng([data.lat, data.lon]);
            // Можно убрать map.setView, чтобы карта не прыгала
        });
}
setInterval(updateMarkerFromServer, 5000); 