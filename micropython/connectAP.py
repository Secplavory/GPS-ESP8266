import network

wlan = network.WLAN(network.STA_IF)
ssid = "Flavor"
pwd = "aaa12345"

if not wlan.isconnected():
    wlan.active(True)
    wlan.connect(ssid, pwd)
    
    while not wlan.isconnected():
        pass

print('network config', wlan.ifconfig())

