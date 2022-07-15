from Watcher import GPS, OLED, API
from machine import Pin

gps = GPS()
oled = OLED()
api = API()
d4 = Pin(2, Pin.OUT, value=0)
postTimer = 0

def loop():
    global gps, oled, api, d4, postTimer
    
    gpsStr = b''
    gpsReading = False
    
    if d4.value() == 0:
        d4.value(1)
    else:
        d4.value(0)
    
    while True:
        data = gps.getGPSInfo()
        if data and (gpsReading or ('$GNRMC' in data)) :
            gpsStr += data
            if '\n' in data:
                gpsReading = False
                
                lat, long, today, now = gps.convertGPS(gpsStr)
                oled.displayGPS(lat, long, today, now)
                gpsStr = b''
                
                postTimer += 1
                if lat=="0" and long=="0":
                    break
                if postTimer<=10:
                    break
                
                postTimer = 0
                api.updateLocation(lat, long, now, today)
                break
            else:
                gpsReading = True

def main():
    while True:
        loop()

main()