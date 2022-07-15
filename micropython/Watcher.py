from machine import UART, Pin, I2C
import time, ssd1306, ujson, connectAP
import urequests as requests

class GPS:
    def __init__(self, bondRate=9600):
        self.com = UART(0, bondRate)
        self.com.init(bondRate)

    def utcDateTime(self, dateStr, timeStr, timeZone=8):
        if dateStr == '' or timeStr == '':
            return None

        day = dateStr[0:2]
        month = dateStr[2:4]
        year = dateStr[4:6]
        hr = timeStr[0:2]
        min = timeStr[2:4]
        sec = timeStr[4:6]
        timeZone *= 3600

        t = time.mktime((int('20' + year), int(month), int(day),int(hr), int(min), int(sec), 0, 0))

        return time.localtime(t+timeZone)

    def latitude(self, d, h):
        if d == '':
            return '0'

        hemi = '' if h == 'N' else '-'
        deg = int(d[0:2])
        min = str(float(d[2:]) / 60)[1:]

        return hemi + str(deg) + min

    def longitude(self, d, h):
        if d == '':
            return '0'

        hemi = '' if h == 'E' else '-'
        deg = int(d[0:3])
        min = str(float(d[3:]) / 60)[1:]

        return hemi + str(deg) + min

    def convertGPS(self, gpsStr):
        gps = gpsStr.split(b'\r\n')[0].decode('ascii').split(',')

        lat = self.latitude(gps[3], gps[4])  # N or S
        long = self.longitude(gps[5], gps[6]) # E or W
        today = ''
        now = ''
        tim = self.utcDateTime(gps[9], gps[1], 8)

        if tim != None:
            today = str(tim[0]) + '/' + str(tim[1]) + '/' + str(tim[2])
            now = str(tim[3]) + ':' + str(tim[4]) + ':' + str(tim[5])

        return (lat, long, today, now)

    def getGPSInfo(self):
        data = self.com.readline()
        return data

class OLED:
    def __init__(self, scl=5, sda=4):
        self.oled = ssd1306.SSD1306_I2C(
            128, 64,
            I2C(scl=Pin(scl), sda=Pin(sda), freq=100000)
        )
        self.oled.text("GPS RUNNING...", 0, 30)
        self.oled.show()

    def displayGPS(self, lat, long, today, now):
        lat = "Lat: " + lat
        long = "Long: " + long
        self.oled.fill(0)
        self.oled.text(today, 0, 0)
        self.oled.text(now, 0, 10)
        self.oled.text(lat, 0, 20)
        self.oled.text(long, 0, 30)
        self.oled.show()

class API:
    def __init__(self, protocol="http://", host="34.70.191.27:", port="80", path="/updateLocation"):
        self.url = protocol+host+str(port)+path
    
    def updateLocation(self, lat, long, now, today):
        requests.post(
            self.url, headers = {'content-type': 'application/json'}, data=ujson.dumps({"lat": lat, "long": long, "time": now, "date": today})
        ).json()
