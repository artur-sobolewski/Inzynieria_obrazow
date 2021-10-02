class Product:
	def __init__(self, name, price):
		self.name = name
		self.price = price
		self.quantity = 1

	def __str__(self):
		return f'{self.name}, price - {self.price}'

available_prod = [
				Product("Toilet Paper", 5.99), Product("Cola", 7.99),
				Product("Chips", 2.30), Product("Chicken", 10.99),
				Product("Apple", 0.25), Product("Pear", 0.35),
				Product("Eggs", 6.99), Product("Yoghurt", 1.79),
				Product("Energy Drink", 4.99), Product("Coffe", 18.99),
				Product("Tea", 7.59), Product("Roll", 0.89),
				Product("Sasusage", 3.99), Product("Sugar", 2.99),
				Product("Orange Juice", 3.89), Product("Milk", 2.29)
				] 

com = ["cost", "available", "add", "Egs", "Eggs", "back", "cost", "str cart", "add", "Coffe", "back",  "cost",
		"remove", "chicen", "ChiCken", "back", "cost", "products", "add", "COLA", "back", "iter cart", "str cart", "space", "cost", "back"]

def see_prod():
	print("\nDostepne produkty:")
	for prod in available_prod:
		print(prod.name + ",  ")

def see_opt():
	print("\nDostepne opcje:")
	print("\tavailable - wyswietlenie dostepnych produktow")
	print("\tcost - wyswietlenie lacznej wartosci produktow z koszyka")
	print("\tadd - dodanie produktu do koszyka")
	print("\tremove - usuniecie poroduktu z koszyka")
	print("\tstr cart - wyswietlenie zawartosci koszyka (za pomoca __str__)")
	print("\titer cart - wyswietlenie zawartosci koszyka (za pomoca __iter__ i __next__)")
	print("\tspace - wyswietlenie ilosci produktow z koszyka (za pomoca __len__)")
	print("\tback - powrot/wyjscie z programu")


class Cart:
	def __init__(self):
		self.products = [
		Product("Toilet Paper", 5.99), Product("Cola", 7.99),
		Product("Chips", 2.30), Product("Chicken", 10.99)
		]

	def add(self, name):
		for prod in available_prod:
			if prod.name.lower() == name:
				for act_prod in self.products:
					if act_prod.name.lower() == name:
						act_prod.quantity+= 1
						print("Produkt dodano do koszyka")
						return
				self.products.append(prod)
				print("Produkt dodano do koszyka")
				return
		print("Brak takiego produktu w sklepie")

	def remove(self, name):
		for act_prod in self.products:
			if act_prod.name.lower() == name and act_prod.quantity > 1:
				act_prod.quantity-= 1
				print("Produkt usunieto z koszyka")
				return
			elif act_prod.name.lower() == name and act_prod.quantity == 1:
				self.products.remove(act_prod)
				print("Produkt usunieto z koszyka")
				return
		print("Brak takiego produktu w koszyku")

	def total_price(self):
		final_cost = 0
		for prod in self.products:
			final_cost += prod.price
		return round(final_cost, 2)

	def __str__(self):
		info = ""
		for prod in self.products:
			info+= f'{prod.quantity} - {prod.__str__()}\n'
		return info

	def __len__(self):
		len = 0
		for prod in self.products:
			len+=prod.quantity
		return len

	def __iter__(self):
		self.n = 0
		return self

	def __next__(self):
		result = ""
		if self.n < len(self.products):
			result = self.products[self.n]
			self.n += 1
			return result
		else:
			raise StopIteration



cart1 = Cart()
see_opt()
inp = ""
while inp != "back":
	
	#inp = input(">")
	if len(com) >= 1:
		inp = com.pop(0)
		print(f'>{inp}')
	else:
		exit()
	if inp.lower() == "available":
		see_prod()
	elif inp.lower() == "cost":
		print(str(cart1.total_price()))
	elif inp.lower() == "add":
		print("Podaj nazwe produktu jaki dodajesz")
		new_item_opt = ""
		while new_item_opt != "back":
			if len(com) >= 1:
				new_item_opt = com.pop(0).lower()
				print(f'>{new_item_opt}')
			else:
				exit()
			#new_item_opt = input("Dodawanie >").lower()
			if new_item_opt != "back":
				cart1.add(new_item_opt)
	elif inp.lower() == "remove":
		print("Podaj nazwe produktu jaki usuwasz")
		rm_item_opt = ""
		while rm_item_opt != "back":
			if len(com) >= 1:
				rm_item_opt = com.pop(0).lower()
				print(f'>{rm_item_opt}')
			else:
				exit()
			#rm_item_opt = input("Usuwanie >").lower()
			if rm_item_opt != "back":
				cart1.remove(rm_item_opt)
	elif inp.lower() == "products":
		print(available_prod[0].__str__())
	elif inp.lower() == "iter cart":
		for prod in cart1:
			print(prod.__str__())
	elif inp.lower() == "str cart":
		print(cart1.__str__())
	elif inp.lower() == "space":
		print(cart1.__len__())
	elif inp.lower() == "back":
		exit()
	else:
		print("\tNie ma takiej opcji")