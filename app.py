import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tksvg


""" testing ip: 165.155.162.14 """

root = tk.Tk()
root.title("I SPY WITH MY LITTLE EYE AN IP")
root.geometry("700x600")
style = ttk.Style()
style.theme_use("clam")
accesskey = "88f4a26ebfa2c094b719135c5535b0b4"

instruct = ttk.Label(root, text="IP you want to search:", font=("Arial", 15))
instruct.place(x=0,y=0)

ipinput = ttk.Entry(root, font=("Arial", 16), width=14)
ipinput.place(x=205,y=0)

copyright = ttk.Label(root, text="YILYANE LOUNAS ©", font=("Arial",11))
copyright.place(x=550,y=0)

def getIP():

    ip = ipinput.get()

    response = requests.get(f"http://api.ipstack.com/{ip}?access_key={accesskey}")
    if response.status_code != 200:
        messagebox.showerror("Error", "Error check your connection")

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
    flag = ipdata["location"]["country_flag"]

    img = tk.Label(root, image=flag)
    img.place(x=400,y=400)

    typ = ttk.Label(root, text=("type:", type), font=("Arial", 16))
    typ.place(x=200,y=200)



enterbutton = ttk.Button(root, text="Enter", command=getIP)
enterbutton.place(x=380,y=0)

root.mainloop()