import json
from tkinter import *
import requests

window = Tk()
window.title("Weather Report")
window.geometry('500x400')
vcity = StringVar()
desc=""



def clicked():
    lbtitle = Label(window, text="Weather Report", font=("times new roman", 20, "bold"), bg="powder blue", width=120,
                    height=1)
    lbtitle.pack(side=TOP, fill=X)
    lblcity = Label(window, text="Enter City Name", font=("times new roman", 10, "bold"), width=12,
                    height=1)
    lblcity.place(x=29, y=87)
    # lblcity.place(x=133,y=1)
    lblcity = Entry(window, textvariable=vcity, font=("times new roman", 10, "bold"), width=28)
    lblcity.place(x=150, y=87)

    btnsubmit = Button(window, text="SUBMIT", command=submit, font=("times new roman", 10, "bold"), relief=RIDGE)
    btnsubmit.place(x=215, y=130)

    lbldesc = Label(window, text="Weather Description", font=("times new roman", 10, "bold"),
                    width=18,
                    height=1)
    lbldesc.place(x=50, y=180)

    lbltemp = Label(window, text="Temperature", font=("times new roman", 10, "bold"),
                    width=18,
                    height=1)
    lbltemp.place(x=50, y=200)

    lblhum = Label(window, text="Humidity", font=("times new roman", 10, "bold"),
                   width=18,
                   height=1)
    lblhum.place(x=50, y=220)

    lblvis = Label(window, text="Visibility", font=("times new roman", 10, "bold"),
                   width=18,
                   height=1)
    lblvis.place(x=50, y=240)

    lblwnspeed = Label(window, text="Wind Speed", font=("times new roman", 10, "bold"),
                       width=18,
                       height=1)
    lblwnspeed.place(x=50, y=260)


def submit():
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={vcity.get()}&appid=81df7a779fa64411b06043ea088bd8c5")
    data = response.text
    parse_json = json.loads(data)
    desc = parse_json['weather'][0]['description']

    lbldesc = Label(window, text=desc, font=("times new roman", 10, "bold"))
    lbldesc.place(x=180, y=180)

    temp = parse_json['main']['temp'] - 273.15

    lbltemp = Label(window, text=temp, font=("times new roman", 10, "bold"))
    lbltemp.place(x=180, y=200)

    humidity = parse_json['main']['humidity']

    lblhum = Label(window, text=humidity, font=("times new roman", 10, "bold"))
    lblhum.place(x=180, y=220)

    visibility = parse_json['visibility']

    lblvis = Label(window, text=visibility, font=("times new roman", 10, "bold"))
    lblvis.place(x=180, y=240)

    wnspeed = parse_json['wind']['speed']

    lblwn = Label(window, text=wnspeed, font=("times new roman", 10, "bold"))
    lblwn.place(x=180, y=260)


if __name__ == "__main__":
    clicked()
    window.mainloop()
