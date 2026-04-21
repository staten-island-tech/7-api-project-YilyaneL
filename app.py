import requests

def getIP(ip,accesskey):
    response = requests.get(f"http://api.ipstack.com/{ip}?access_key={accesskey}")
    if response.status_code != 200:
        print("nothing is coming check your internet")

    ipdata = response.json()
    
    type = ipdata["type"]
    country = ipdata["country_name"]
    region = ipdata["region_name"]
    city = ipdata["city"]
    zip = ipdata["zip"]
    latitude = ipdata["latitude"]
    longitude = ipdata["longitude"]
    routingtype = ipdata["ip_routing_type"]
    countrypicture = ipdata["location"]["country_flag"]
    current_time = ipdata["time_zone"]["current_time"]
    currency = ipdata["currency"]["code"]
    isp = ipdata["connection"]["isp"]

    print(region)

getIP("165.155.162.14","88f4a26ebfa2c094b719135c5535b0b4")

