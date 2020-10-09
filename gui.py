from tkinter import *
from cards import *

master = Tk()
w = Canvas(master, width=400, height=600)
w.pack()

def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]
    return w.create_polygon(points, **kwargs, smooth=True)


# SETTINGS

deck = StringVar(master)
deck.set("Full Deck")
set_deck = OptionMenu(master, deck, "Full Deck", "Major Arcana", "Minor Arcana")
set_deck.place(relx=0, rely=0)

revs = IntVar(master)
revs_button = Checkbutton(w, text="Reversals", variable=revs, onvalue=True, offvalue=False)
revs_button.place(relx=0.33, rely=0)

layout = StringVar(master)
layout.set("One Card")
set_layout = OptionMenu(master, layout, "One Card", "Three Card", "Celtic Cross")
set_layout.place(relx=0.66, rely=0)

all_deck = {"Full Deck": tarot, 
"Major Arcana": major, 
"Minor Arcana": minor}

response = ""

def button_press():
	response = draw_a_card(all_deck[deck.get()], revs.get(), layout.get())
	w.delete("card")
	if layout.get() == "One Card":
		round_rectangle(125, 75, 200, 200, radius=10, fill="white", outline="black", tags="card") # 75 across, 125 down
		w.create_text(162.5, 125, text=response["One Card"].replace(", ", ",\n"), tags="card")
	elif layout.get() == "Three Card":
		i = 0
		for k, v in response.items():
			round_rectangle(25+(100*i), 75, 100+(100*i), 200, radius=10, fill="white", outline="black", tags="card")
			w.create_text(62.5+(100*i), 125, text=v.replace(", ", ",\n"), font=("Arial", 8), justify="center", tags="card")
			i += 1
	elif layout.get() == "Celtic Cross":
		i = 0



reading = Button(master, text="Deal Cards", command=button_press)
reading.place(relx=0.33, y=30)

mainloop()