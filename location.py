import justpy as jp
import requests
import geocoder

def loc_weather_may():
    loc = geocoder.ip("me")

    url = "https://wttr.in/Kyiv?format=%t"
    r = requests.get(url)
    t = r.text.strip()

    wp = jp.WebPage()
    m = jp.Div(text=str(loc.latlng)) 
    d = jp.Div(text=t)

    wp.add(d)
    wp.add(m)

    if '+' in t:
        k = jp.Div(text=f"0%-20%")
        wp.add(k)
    elif 0 <= int(t[0:2]) <= -5 :
        q = jp.Div(text=f"20%-50%")
        wp.add(q)
    elif int(t[0:2]) >= -10:
        e = jp.Div(text=f"50%-90%")
        wp.add(e)


    return wp 

jp.justpy(loc_weather_may, port=7960)
