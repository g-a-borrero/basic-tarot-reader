import random
import copy

minor_suits = ["Cups", "Pentacles", "Swords", "Wands"]
minor_numbers = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
"Ten", "Page", "Knight", "Queen", "King"]
minor = [num + " of " + suit for num in minor_numbers for suit in minor_suits]
major = ["0 - The Fool", "I - The Magician", "II - The High Priestess", "III - The Empress", 
"IV - The Emperor", "V - The Hierophant", "VI - The Lovers", "VII - The Chariot", 
"VIII - Justice", "IX - The Hermit", "X - Wheel of Fortune", "XI - Strength", 
"XII - The Hanged Man", "XIII - Death", "XIV - Temperance", "XV - The Devil", 
"XVI - The Tower", "XVII - The Star", "XVIII - The Moon", "XIX - The Sun", 
"XX - Judgement", "XXI - The World"]
tarot = major + minor

def draw_a_card(cards_copy=tarot, reversals=True, layout="One Card"):
	cards = copy.deepcopy(cards_copy)
	to_draw = {
	"One Card": ["One Card"],
	"Three Card": ["Past", "Present", "Future"],
	"Celtic Cross": ["Self", "Conflict", "Basis of Conflict", "Past", "Hopes", "Near Future", 
	"Self (Perceived by Others)", "Self (Perceived by Self)", "Fears", "Far Future"]
	}
	to_draw["Romani"] = [time + " " + aspect for time in to_draw["Three Card"] for aspect in 
	["Self", "Home", "Hopes & Fears", "Known Factors", "Hidden Factors", "Short Term Future", "Long Term Future"]]
	drawn = {}
	for card_type in to_draw[layout]:
		drawn[card_type] = ""
	for each_card in drawn.keys():
		if layout == "Celtic Cross" and each_card == "Conflict":
			drawn[each_card] = cards.pop(random.randint(0,len(cards)-1))
		else:
			drawn[each_card] = cards.pop(random.randint(0,len(cards)-1)) + (", Reversed" if random.randint(0, 1) and reversals else "")
	drawn_string = "\n".join([k + ": " + v for k, v in drawn.items()])
	print(drawn_string)
	return(drawn)

if __name__ == "__main__":
	draw_a_card(layout="celtic cross")