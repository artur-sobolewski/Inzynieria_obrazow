import math

def function(arg):
	return math.sin(math.radians(arg))

#utworzenie pliku z argumentami
in_filepath = "dane.txt"
file = open(in_filepath, "w")
x = range(361)
for n in x:
    file.write(str(n) + "\n")
file.close()

#wczytywanie danych z pliku i zapis wyników do innego pliku
in_filepath = "dane.txt"
out_filepath = "wyniki.txt"
file = open(in_filepath, 'r').read()
out_file = open(out_filepath, "w")
lines = file.split('\n')
for line in lines:
	if(line != ""):
		out_file.write(line + "  " + str(function(int(line))) + "\n")
out_file.close()