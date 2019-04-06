from tkinter import *
import json
import requests
from tkinter import messagebox
city = ''
def get():
	global city
	try:
		text.delete(1.0,END)
		city = city_entry.get()
		url = 'http://api.openweathermap.org/data/2.5/weather?appid=82270728ff6023bdb79760f74d9dc8f7&q='+city
		r_data = requests.get(url)
		j_data = r_data.json()
		temp = j_data['main']['temp']
		desc = j_data['weather'][0]['description']
		wis = j_data['wind']['speed']
		o_temp = float(temp-273.15)
		text.insert(END,'Tempreature (*C): '+str(o_temp)+'\n'+'\n')
		text.insert(END,'Description: '+desc+'\n'+'\n')
		text.insert(END,'Wind Speed: '+str(wis)+' Km/h'+'\n') 
	except:
		text.delete(1.0,END)
		text.insert(END,'No City Found. Please Write the correct Spelling of City!')

	


root = Tk()
root.title('Weather-API')
root.maxsize( height = 405,width = 300)
bg = PhotoImage(file = 'bg.png')
mainframe = Label(root,image = bg)
logo = Label(root,bg = 'azure',text = '    Weather-API    ',font= ('consolas',15))
logo.place(x = 40,y = 10)
city_label =Label(root,bg = 'azure',text = 'Enter City Name',font = ('consolas',15))
city_label.place(x =10,y = 60)
city_entry = Entry(root,bg = 'azure',font = ('consolas',15))
city_entry.place(x = 9 ,y = 100)
search = Button(root,text = 'Search',font = ('consolas',10),command = get)
search.place(x = 240,y = 102)
text = Text(root,bg = 'azure',height = 11,width = 26,font = ('consolas',15),wrap =WORD,padx = 2)
text.place(x = 5,y = 140)
mainframe.pack() 
root.mainloop()
