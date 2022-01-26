import os
from tkinter import *
from tkinter.messagebox import showerror, showinfo, askyesno

#--------------values
deb = "[DEBBUGING] "
err = "[ERROR] "
dis = "[DIAGNOSTICS] "
#--------------values

#--------------game values
hp = 10
damage = 1
money = 0
price = 10
temp = 0
#--------------game values

#--------------prices
price_1 = price
price_2 = price * 8
price_3 = price * 15
price_4 = price * 29
price_5 = price * 38
price_6 = price * 90
#--------------prices

#--------------codes
state_promo = "CLICKERGIFT" 	# + 100 to money, and + 1 to damage
temp_promo_1 = "QUUYKGYSC8L"	# + 50 to money, and + 2 to damage
temp_promo_2 = "GF63T71NCTQ"	# + 3 to damage
temp_promo_3 = "VL0BM3B7UKQ"	# + 150 to money
#--------------codes

app = Tk()
app.configure(bg="#514")
app.title("Game clicker")
app.resizable(0, 0)
app.geometry("450x420+550+170")
app.iconbitmap("clicker.ico")

#--------------labels
damage_label = Label(text="DMG: " + str(damage), justify=RIGHT, bg="#514", fg="#fff", font="Arial 13")
damage_label.place(relx=.05, rely=.3)

money_label = Label(text="$" + str(money), justify=RIGHT, bg="#514", fg="#fff", font="Arial 15")
money_label.place(relx=.05, rely=.65)
#--------------labels

#--------------buffes
def buff_1():
	global hp
	global damage
	global money
	global price_1

	if money >= price_1:
		money -= price_1
		damage += 1

		if temp == 0:
			hp += 90
			main_btn.config(text=hp)
		else:
			main_btn.config(text="HIT")

		damage_label.config(text="DMG: " + str(damage))
		money_label.config(text="$" + str(money))
		bonus_dmg_1['state'] = "disabled"
		main_btn['state'] = "normal"

		print(f"DMG = [{str(damage)}]")
	else:
		showerror("ALERT!", "Not enough money")


def buff_2():
	global hp
	global damage
	global money
	global price_2

	if money >= price_2:
		money -= price_2
		damage += 3

		if temp == 0:
			hp += 150
			main_btn.config(text=hp)
		else:
			main_btn.config(text="HIT")

		damage_label.config(text="DMG: " + str(damage))
		money_label.config(text="$" + str(money))
		bonus_dmg_2['state'] = "disabled"
		main_btn['state'] = "normal"

		print(f"DMG = [{str(damage)}]")
	else:
		showerror("ALERT!", "Not enough money")


def buff_3():
	global hp
	global damage
	global money
	global price_3

	if money >= price_3:
		money -= price_3
		damage += 5

		if temp == 0:
			hp += 290
			main_btn.config(text=hp)
		else:
			main_btn.config(text="HIT")

		damage_label.config(text="DMG: " + str(damage))
		money_label.config(text="$" + str(money))
		bonus_dmg_3['state'] = "disabled"
		main_btn['state'] = "normal"
		
		print(f"DMG = [{str(damage)}]")
	else:
		showerror("ALERT!", "Not enough money")


def buff_4():
	global hp
	global damage
	global money
	global price_4

	if money >= price_4:
		money -= price_4
		damage += 10

		if temp == 0:
			hp += 370
			main_btn.config(text=hp)
		else:
			main_btn.config(text="HIT")

		damage_label.config(text="DMG: " + str(damage))
		money_label.config(text="$" + str(money))
		bonus_dmg_4['state'] = "disabled"
		main_btn['state'] = "normal"
		
		print(f"DMG = [{str(damage)}]")
	else:
		showerror("ALERT!", "Not enough money")


def buff_5():
	global hp
	global damage
	global money
	global price_5

	if money >= price_5:
		money -= price_5
		damage *= 2

		if temp == 0:
			hp += 900
			main_btn.config(text=hp)
		else:
			main_btn.config(text="HIT")

		damage_label.config(text="DMG: " + str(damage))
		money_label.config(text="$" + str(money))
		bonus_dmg_5['state'] = "disabled"
		main_btn['state'] = "normal"
		
		print(f"DMG = [{str(damage)}]")
	else:
		showerror("ALERT!", "Not enough money")


def buff_6():
	global hp
	global damage
	global money
	global price_6

	if money >= price_6:
		money -= price_6
		damage *= 3

		if temp == 0:
			hp += 2500
			main_btn.config(text=hp)
		else:
			main_btn.config(text="HIT")

		damage_label.config(text="DMG: " + str(damage))
		money_label.config(text="$" + str(money))
		bonus_dmg_6['state'] = "disabled"
		main_btn['state'] = "normal"
		
		print(f"DMG = [{str(damage)}]")

		main_btn.config(command=next_step)
	else:
		showerror("ALERT!", "Not enough money")
#--------------buffes

#--------------main code
def hit_monster():
	global hp
	global money
	hp -= damage
	money += damage

	main_btn.config(text=hp)
	money_label.config(text="$" + str(money))
	
	if hp <= 0:
		main_btn['state'] = "disabled"
		hp = 0
		main_btn.config(text=hp)
	else:
		print(f"HP = [{str(hp)}]")


def next_step():
	global hp
	global money
	hp -= damage
	money += damage

	main_btn.config(text=hp)
	money_label.config(text="$" + str(money))
	
	if hp <= 0:
		main_btn['state'] = "disabled"
		hp = 0
		main_btn.config(text=hp)
		if temp == 0:
			continues()
		else:
			main_btn.config(text="HIT", command=hard_mode)
			change_prices()
	else:
		print(f"HP = [{str(hp)}]")


def continues():
	global damage
	global money
	global hp
	global temp

	global price_1
	global price_2
	global price_3
	global price_4
	global price_5
	global price_6

	showinfo("Is this the end?", "Hi\nI`m developer of this game")
	showinfo("Is this the end?", "And if you see that message, you must ended the game")
	showinfo("Is this the end?", "But that`s wrong.\nThe game continue and becomes more difficult")
	if askyesno("Is this the end?", "Do you want to contine the game?") == True:
		print(deb + "Player answer 'yes'")
		change_prices()
	else:
		print(deb + "Player answer 'no'")
		showinfo("Good luck", "Ok, see you next time.")
		app.quit()


def hard_mode():
	global money
	money += damage

	money_label.config(text="$" + str(money))


def change_prices():
	global damage
	global money
	global hp
	global temp

	global price_1
	global price_2
	global price_3
	global price_4
	global price_5
	global price_6

	damage = 1
	money = 0
	hp = 0
	temp = 1

	damage_label.config(text="DMG: " + str(damage))
	money_label.config(text="$" + str(money))
	main_btn.config(text="HIT", command=hard_mode)

	price_1 += price * 10
	price_2 += price * 25
	price_3 += price * 50
	price_4 += price * 100
	price_5 += price * 200
	price_6 += price * 600

	cost_label_1.config(text="$" + str(price_1))
	cost_label_2.config(text="$" + str(price_2))
	cost_label_3.config(text="$" + str(price_3))
	cost_label_4.config(text="$" + str(price_4))
	cost_label_5.config(text="$" + str(price_5))
	cost_label_6.config(text="$" + str(price_6))


	main_btn['state'] = "normal"
	bonus_dmg_1['state'] = "normal"
	bonus_dmg_2['state'] = "normal"
	bonus_dmg_3['state'] = "normal"
	bonus_dmg_4['state'] = "normal"
	bonus_dmg_5['state'] = "normal"
	bonus_dmg_6['state'] = "normal"
#--------------main code

#--------------enter promocode
def enter_promocode():
	print(deb + "Enter promocode")
	enter_code['state'] = "disabled"
	
	promo_app = Tk()
	promo_app.configure(bg="#625")
	promo_app.title("Promocode")
	promo_app.resizable(0, 0)
	promo_app.geometry("300x200+550+170")
	promo_app.iconbitmap("clicker.ico")

	#--------------label
	text_label = Label(promo_app, text="Enter your promocode", justify=RIGHT, bg="#625", fg="#fff", font="Arial 13")
	text_label.place(relx=.215, rely=.15)
	#--------------label

	#--------------entry
	promo_entry = Entry(promo_app, bg="#066", fg="#eee", font="Arial  11")
	promo_entry.place(relx=.5, rely=.4, anchor="c", heigh=30, width=210)
	#--------------entry

	#--------------check promo
	def check_promocode():
		global money
		global damage
		promocode = promo_entry.get()
		print(f"Promocode = [{promocode}]")

		if not promocode:
			print(deb + "No entry promo")

		elif state_promo == promocode:
			try:
				os.remove("temp/1.txt")

				money += 100
				damage += 1
				damage_label.config(text="DMG: " + str(damage))
				money_label.config(text="$" + str(money))

				print(deb + "Promocode succsessfully activated")
				showinfo("Succses", "Promocode succsessfully activated")
			except FileNotFoundError:
				print(err + "Promocode was activated earlier")
				showerror("Error", "Promocode was activated earlier")

		elif temp_promo_1 == promocode:
			try:
				os.remove("temp/2.txt")

				money += 50
				damage += 2
				damage_label.config(text="DMG: " + str(damage))
				money_label.config(text="$" + str(money))

				print(deb + "Promocode succsessfully activated")
				showinfo("Succses", "Promocode succsessfully activated")
			except FileNotFoundError:
				print(err + "Promocode was activated earlier")
				showerror("Error", "Promocode was activated earlier")

		elif temp_promo_2 == promocode:
			try:
				os.remove("temp/3.txt")

				damage += 3
				damage_label.config(text="DMG: " + str(damage))

				print(deb + "Promocode succsessfully activated")
				showinfo("Succses", "Promocode succsessfully activated")
			except FileNotFoundError:
				print(err + "Promocode was activated earlier")
				showerror("Error", "Promocode was activated earlier")

		elif temp_promo_3 == promocode:
			try:
				os.remove("temp/4.txt")

				money += 150
				money_label.config(text="$" + str(money))

				print(deb + "Promocode succsessfully activated")
				showinfo("Succses", "Promocode succsessfully activated")
			except FileNotFoundError:
				print(err + "Promocode was activated earlier")
				showerror("Error", "Promocode was activated earlier")

		else:
			print(f"{err}Not this promo: {str(promocode)}")
			showerror("Error", "Not this promo: " + str(promocode))

		promo_entry.delete(0, END)
	#--------------check promo

	#--------------btn
	check_code = Button(promo_app, text="Enter code", bd=0.5, bg="#514", fg="#fff", padx="20", pady="8", font="Arial 14", command=check_promocode)
	check_code.place(relx=.5, rely=.7, anchor="c", height=38, width=110)
	#--------------btn

	promo_app.mainloop()
#--------------enter promocode

#--------------check actived promo and save it
def saves_checker():
	global money
	global damage

	if not os.path.exists("temp/1.txt"):
		money += 100
		damage += 1
		damage_label.config(text="DMG: " + str(damage))
		money_label.config(text="$" + str(money))
		print(f"{dis}Promo active [{state_promo}]")
	else:
		print(f"{dis}Promo not active [{state_promo}]")

	if not os.path.exists("temp/2.txt"):
		money += 50
		damage += 2
		damage_label.config(text="DMG: " + str(damage))
		money_label.config(text="$" + str(money))
		print(f"{dis}Promo active [{temp_promo_1}]")
	else:
		print(f"{dis}Promo not active [{temp_promo_1}]")

	if not os.path.exists("temp/3.txt"):
		damage += 3
		damage_label.config(text="DMG: " + str(damage))
		money_label.config(text="$" + str(money))
		print(f"{dis}Promo active [{temp_promo_2}]")
	else:
		print(f"{dis}Promo not active [{temp_promo_2}]")

	if not os.path.exists("temp/4.txt"):
		money += 150
		money_label.config(text="$" + str(money))
		print(f"{dis}Promo active [{temp_promo_3}]")
	else:
		print(f"{dis}Promo not active [{temp_promo_3}]")
#--------------check actived promo and save it

#--------------cheat
def cheat_on():
	global money
	money += 50000
	money_label.config(text="$" + str(money))
	cheat_btn.destroy()

cheat_btn = Button(text="cheat", bg="#514", fg="#fff", padx="20", pady="8", font="Arial 10", command=cheat_on)
#cheat_btn.place(relx=.5, rely=.7, anchor="c", height=22, width=50)
#--------------cheat

#--------------btns
main_btn = Button(text=hp, bg="#066", fg="#fff", padx="20", pady="8", font="Arial 35", command=hit_monster)
main_btn.place(relx=.5, rely=.5, anchor="c", height=120, width=135)

enter_code = Button(text="(?)", bd=0, bg="#514", fg="#fff", padx="20", pady="8", font="Arial 10", command=enter_promocode)
enter_code.place(relx=.95, rely=.3, anchor="c", height=25, width=26)
enter_code['state'] = "normal"


bonus_dmg_1 = Button(text="Bonus dmg\n+1", bg="#625", fg="#fff", padx="20", pady="8", font="Arial 12", command=buff_1)
bonus_dmg_1.place(relx=.2, rely=.1, anchor="c", height=44, width=110)

bonus_dmg_2 = Button(text="Bonus dmg\n+3", bg="#625", fg="#fff", padx="20", pady="8", font="Arial 12", command=buff_2)
bonus_dmg_2.place(relx=.5, rely=.1, anchor="c", height=44, width=110)

bonus_dmg_3 = Button(text="Bonus dmg\n+5", bg="#625", fg="#fff", padx="20", pady="8", font="Arial 12", command=buff_3)
bonus_dmg_3.place(relx=.8, rely=.1, anchor="c", height=44, width=110)

bonus_dmg_4 = Button(text="Bonus dmg\n+10", bg="#625", fg="#fff", padx="20", pady="8", font="Arial 12", command=buff_4)
bonus_dmg_4.place(relx=.2, rely=.9, anchor="c", height=44, width=110)

bonus_dmg_5 = Button(text="Bonus dmg\n*2", bg="#625", fg="#fff", padx="20", pady="8", font="Arial 12", command=buff_5)
bonus_dmg_5.place(relx=.5, rely=.9, anchor="c", height=44, width=110)

bonus_dmg_6 = Button(text="Bonus dmg\n*3", bg="#625", fg="#fff", padx="20", pady="8", font="Arial 12", command=buff_6)
bonus_dmg_6.place(relx=.8, rely=.9, anchor="c", height=44, width=110)
#--------------btns

#--------------cost labels
cost_label_1 = Label(text="$" + str(price_1), bg="#514", fg="#fff", font="Arial 13")
cost_label_1.place(relx=.165, rely=.17)

cost_label_2 = Label(text="$" + str(price_2), bg="#514", fg="#fff", font="Arial 13")
cost_label_2.place(relx=.465, rely=.17)

cost_label_3 = Label(text="$" + str(price_3), bg="#514", fg="#fff", font="Arial 13")
cost_label_3.place(relx=.75, rely=.17)

cost_label_4 = Label(text="$" + str(price_4), bg="#514", fg="#fff", font="Arial 13")
cost_label_4.place(relx=.15, rely=.77)

cost_label_5 = Label(text="$" + str(price_5), bg="#514", fg="#fff", font="Arial 13")
cost_label_5.place(relx=.45, rely=.77)

cost_label_6 = Label(text="$" + str(price_6), bg="#514", fg="#fff", font="Arial 13")
cost_label_6.place(relx=.75, rely=.77)
#--------------cost labels
#continues()
if __name__ == '__main__':
	saves_checker()
	print(f"{deb}Game start\nHP = [{str(hp)}]\nDMG = [{str(damage)}]")
	app.mainloop()
	print(deb + "Program finished")
