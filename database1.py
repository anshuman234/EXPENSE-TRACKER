import numpy as np
from matplotlib import pyplot as plt

from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import ImageTk,Image
import sqlite3


root = Tk()
root.title("EXPENSE TRACKER")
root.iconbitmap('icon.ico')
root.configure(bg="#0f0f0f")
root.geometry("1450x750")
root.minsize(1030,800)
root.maxsize(1030,800)

s = ttk.Style()
# database and connect 
conn = sqlite3.connect('expenses_income.db')
# cursor
c = conn.cursor()

# create table

'''
c.execute("""CREATE TABLE expenses (
			name text,
			food integer,
			electricity integer,
			travel integer,
			groceries integer,
			fuel integer,
			others integer)
			""")
'''

# create submit function

def submit():
	# database and connect to it
	conn = sqlite3.connect('expenses_income.db')
	# cursor
	c = conn.cursor()
	# Insert into Table

	c.execute("INSERT INTO expenses VALUES (:name, :food, :electricity, :travel, :groceries, :fuel, :others)",

			{

				'name': name.get(),
				'food': food.get(),
				'electricity': electricity.get(),
				'travel': travel.get(),
				'groceries': groceries.get(),
				'fuel': fuel.get(),
				'others': others.get()
			})


	# commit changes
	conn.commit()

	# close connection
	conn.close()

	# clear text boxes
	name.delete(0, END)
	food.delete(0, END)
	electricity.delete(0, END)
	travel.delete(0, END)
	groceries.delete(0, END)
	fuel.delete(0, END)
	others.delete(0, END)


# QUERY FUNCTION
def query():
	
	conn = sqlite3.connect('expenses_income.db')
	
	c = conn.cursor()

	# QUERY THE TABLE
	c.execute("SELECT *, oid FROM expenses")
	records = c.fetchall()
	# print(records)

	
	print_records = ''
	for record in records:
		print_records += "|name>>" + str(record[0]) + " |  food>> " + str(record[1]) + " |  electricity>> " + str(record[2]) + " |  travel>>" + str(record[3]) + " |  groceries>>" + str(record[4]) + " |  fuel>>" + str(record[5]) + " |  others>>" + str(record[6]) +  "\n"


	query_label = Label(root, text=print_records)
	query_label.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


	conn.commit()
	conn.close()


def visual():
	plt.style.use( 'fivethirtyeight')

	x = int
	x = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
	x_indexes = np.arange(len(x))+1



	y = [40,40,0,100,0,50,50,50,50,45,50,0]
	plt.plot( x_indexes, y, label="food")

	y_2 = [0,0,0,0,0,100,50,60,0,50,1100,0]
	plt.plot( x_indexes, y_2, label="electricity")


	y_3 = [0,0,0,0,0,500,120,120,100,100,50,0]
	plt.plot(x_indexes,  y_3, label="travel")


	y_5 = [500,550,0,0,0,1000,200,100,400,150,200,0]
	plt.plot( x_indexes,  y_5, label="groceries")

	y_6 = [100,100,0,100,0,200,100,100,50,120,70,0]
	plt.plot( x_indexes,  y_6, label="fuel")

	y_7 = [50,50,0,100,0,250,250,50,250,80,150,0]
	plt.plot( x_indexes,  y_7, label="others")


	plt.xlabel('Days')
	plt.ylabel('RUPEES')

	plt.title("EXPENSES")
	plt.legend()

	# plt.tight_layout()
	plt.show()


# labels
f = LabelFrame(root, bg="#4169E1",  padx=230, pady=30)
f.grid(row = 1, column = 0, columnspan=4)

head_label = Label(f, text = "EXPENSE TRACKER", bg="#4169E1" )
head_label.config(font = ("Courier", 52 ,"bold" ))
head_label.grid(row=2, column=0, columnspan=2)

f = LabelFrame(root, bg="#BDBDBD",  padx=100, pady=55)
f.grid(row = 3, column = 0,padx=0, pady=20)

name_label = Label(f, text="Name",font =(44),  bg="#BDBDBD")
name_label.grid(row=4, column=0)
name = ttk.Entry(f, width=30)
name.grid(row=4, column=1)

food_label = Label(f, text="Food",font =(44),  bg="#BDBDBD")
food_label.grid(row=5, column=0)
food = ttk.Entry(f, width=30)
food.grid(row=5, column=1)

electricity_label = Label(f, text="Electricity",font =(44),  bg="#BDBDBD")
electricity_label.grid(row=6, column=0)
electricity = ttk.Entry(f, width=30)
electricity.grid(row=6, column=1)

travel_label = Label(f, text="Travel",font =(44),  bg="#BDBDBD")
travel_label.grid(row=7, column=0)
travel = ttk.Entry(f, width=30)
travel.grid(row=7, column=1)

groceries_label = Label(f, text="Groceries", font =(44), bg="#BDBDBD")
groceries_label.grid(row=8, column=0)
groceries = ttk.Entry(f, width=30)
groceries.grid(row=8, column=1)

fuel_label = Label(f, text="Fuel",font =(44),  bg="#BDBDBD")
fuel_label.grid(row=9, column=0)
fuel = ttk.Entry(f, width=30)
fuel.grid(row=9, column=1)

others_label = Label(f, text="Others",font =(44),  bg="#BDBDBD")
others_label.grid(row=10, column=0)
others = ttk.Entry(f, width=30)
others.grid(row=10, column=1)



f = LabelFrame(root, bg="#DC143C", padx=60, pady=60)
f.grid(row = 3, column = 1, padx=0, pady=0)

# SUBMIT BUTTON
s=ttk.Style()
s.configure("TButton", padding = 7,font = (18), bg = "#BDBDBD")


submit_button = ttk.Button(f, text= "Add expenses", style = "TButton",  command=submit)

submit_button.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# QUERY WIDGET
query_button = ttk.Button(f, text= "View Records", command=query)
query_button.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# graph button
query_button = ttk.Button(f, text= "View Visuals" , command = visual)
query_button.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# commit changes
conn.commit()

# close connection
conn.close()

root.mainloop()


































