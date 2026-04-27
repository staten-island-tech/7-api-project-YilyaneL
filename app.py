import requests
from tkinter import messagebox
import customtkinter





""" testing ip: 165.155.162.14 """

app = customtkinter.CTk()
app.title("I SPY WITH MY LITTLE EYE AN IP")
app.geometry("700x600")
accesskey = "88f4a26ebfa2c094b719135c5535b0b4"

instruct = customtkinter.CTkLabel(app, text="IP you want to search:", font=("Arial", 15))
instruct.place(x=5,y=0)

ipinput = customtkinter.CTkEntry(app, font=("Arial", 16), width=150)
ipinput.place(x=155,y=0)

copyright = customtkinter.CTkLabel(app, text="YILYANE LOUNAS ©", font=("Arial",11))
copyright.place(x=550,y=0)

def getIP():

    ip = ipinput.get()

    response = requests.get(f"http://api.ipstack.com/{ip}?access_key={accesskey}")
    if response.status_code != 200:
        messagebox.showerror("error", "check your connection")

    ipdata = response.json()
    
    type = ipdata["type"]
    country = ipdata["country_name"]
    region = ipdata["region_name"]
    city = ipdata["city"]
    zip = ipdata["zip"]
    latitude = ipdata["latitude"]
    longitude = ipdata["longitude"]
    routingtype = ipdata["ip_routing_type"]
    current_time = ipdata["time_zone"]["current_time"]
    currency = ipdata["currency"]["code"]
    isp = ipdata["connection"]["isp"]

    typ = customtkinter.CTkLabel(app, text=("type:", type), font=("Arial", 16))
    typ.place(x=5,y=100)

    ctry = customtkinter.CTkLabel(app,text=("country:", country), font=("Arial",16))
    ctry.place(x=5,y=150)

    cty = customtkinter.CTkLabel(app,text=("city:", city), font=("Arial",16))
    cty.place(x=5,y=200)

    zip = customtkinter.CTkLabel(app,text=("zip:", zip), font=("Arial",16))
    zip.place(x=5,y=250)

    latlong = customtkinter.CTkLabel(app,text=("Long. & Lang:", longitude, latitude), font=("Arial",16))
    latlong.place(x=5,y=300)

    routype = customtkinter.CTkLabel(app,text=("routing type:", routingtype), font=("Arial",16))
    routype.place(x=5,y=350)

    currentime = customtkinter.CTkLabel(app,text=("current date & time there:", current_time), font=("Arial",16))
    currentime.place(x=5,y=400)

    currencies= customtkinter.CTkLabel(app,text=("currency:", currency), font=("Arial",16))
    currencies.place(x=5,y=450)

    ispee = customtkinter.CTkLabel(app,text=("isp", isp), font=("Arial",16))
    ispee.place(x=5,y=500)


enterbutton = customtkinter.CTkButton(app, text="Enter", command=getIP)
enterbutton.place(x=320,y=0)

app.mainloop()