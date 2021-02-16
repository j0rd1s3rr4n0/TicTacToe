#TicTakToe
# By Jordi_Serrano
# [] !
"""
\|/
-X-
/|\
"""
import random, os, time

#Lists
Pos = []
One = []
Computer = []
Pos_Ava = ['tl','tc','tr','ml','mc','mr','bl','bc','br']
Pos_No = []
# None IN POSITION
tl = "*";tc = "*";tr = "*";ml = "*";mc = "*";mr = "*";bl = "*";bc = "*";br = "*";

#Table Print

try:
	a = ''
	while a == '':
		table = "           IN GAME          POSITIONS	\n	+---+---+---+   +----+----+----+\n	| "+tl+" | "+tc+" | "+tr+" |   | tl | tc | tr |\n	+---+---+---+   +----+----+----+\n	| "+ml+" | "+mc+" | "+mr+" |   | ml | mc | mr |\n	+---+---+---+   +----+----+----+\n	| "+bl+" | "+bc+" | "+br+" |   | bl | bc | br |\n	+---+---+---+   +----+----+----+\n"
		print('---------------------')
		print('\n---------------------\n')
	#        _____ _____  _    _ 
	#       / ____|  __ \| |  | |
	#      | |    | |__) | |  | |
	#      | |    |  ___/| |  | |
	#      | |____| |    | |__| |
	#       \_____|_|     \____/ 
		# Generate Position for 'O'
		#randi = random.randrange(0,int((len(Pos_Ava))-1))
		print(len(Pos_Ava))
		while len(Pos_Ava) > 0:
			randi = random.randrange(0,int(len(Pos_Ava)))
			cpu = Pos_Ava[int(randi)]
			print('C: '+str(cpu))
			while cpu in Pos_No:
				randi = random.randrange(0,int(len(Pos_Ava)))
				cpu = Pos_Ava[int(randi)]
				print(cpu)
			if cpu not in Pos_No:
				print(cpu,"N")
				#Pos_Ava.pop(2)
				print(cpu)
				Pos_Ava.remove(str(cpu))
				print(Pos_Ava,str(len(Pos_Ava)))
				time.sleep(1)
			else:
				print(cpu,"A")
				print(Pos_Ava,'d')
				#Pos_Ava.pop(2)
				print(cpu)
				#Pos_Ava.remove(str(cpu))
				print(Pos_Ava,"n")
				time.sleep(10)


		#list.append('option')
		#Pos_No
		#Computer
		





	#   _____                        _____                            
	#  / ____|                      |  __ \                           
	# | |  __  __ _ _ __ ___   ___  | |__) |_ _ _ __ __ _ _ __ ___    
	# | | |_ |/ _` | '_ ` _ \ / _ \ |  ___/ _` | '__/ _` | '_ ` _ \   
	# | |__| | (_| | | | | | |  __/ | |  | (_| | | | (_| | | | | | |_ 
	#  \_____|\__,_|_| |_| |_|\___| |_|   \__,_|_|  \__,_|_| |_| |_(_)
	                                                                 
		print(table)
		print('NO: ',Pos_No)
		#print('POS: ',Pos)
		print('One: ',One)
		#print('Compu: ',Computer)
		#print('Ava: ',Pos_Ava)                                                                 
		option = input("NEW POSITION FOR \'X\' > ")
		option = option.lower()

		if option == "tl":
			if tl == "*":
				tl = 'X'
				Pos_No.append('tl')
			
		elif option == "tc":
			if tc == "*":
				tc = 'X'
				Pos_No.append('tc')
			
		elif option == "tr":
			if tr == "*":
				tr = 'X'
				Pos_No.append('tr')
			
		elif option == "ml":
			if ml == "*":
				ml = 'X'
				Pos_No.append('ml')
			
		elif option == "mc":
			if mc == "*":
				mc = 'X'
				Pos_No.append('mc')
			
		elif option == "mr":
			if mr == "*":
				mr = 'X'
				Pos_No.append('mr')
			
		elif option == "bl":
			if bl == "*":
				bl = 'X'
				Pos_No.append('bl')
			
		elif option == "bc":
			if bc == "*":
				bc = 'X'
				Pos_No.append('bc')
			
		elif option == "br":
			if br == "*":
				br = 'X'
				Pos_No.append('br')
		table = "\n	+---+---+---+   +----+----+----+\n	| "+tl+" | "+tc+" | "+tr+" |   | tl | tc | tr |\n	+---+---+---+   +----+----+----+\n	| "+ml+" | "+mc+" | "+mr+" |   | ml | mc | mr |\n	+---+---+---+   +----+----+----+\n	| "+bl+" | "+bc+" | "+br+" |   | bl | bc | br |\n	+---+---+---+   +----+----+----+\n"
		print(table)
	# __          ___          _____                _ _ _   _                 
	# \ \        / (_)        / ____|              | (_) | (_)                
	#  \ \  /\  / / _ _ __   | |     ___  _ __   __| |_| |_ _  ___  _ __  ___ 
	#   \ \/  \/ / | | '_ \  | |    / _ \| '_ \ / _` | | __| |/ _ \| '_ \/ __|
	#    \  /\  /  | | | | | | |___| (_) | | | | (_| | | |_| | (_) | | | \__ \
	#     \/  \/   |_|_| |_|  \_____\___/|_| |_|\__,_|_|\__|_|\___/|_| |_|___/

		# Win ---
		if tl=='O' and tc=='O' and tr=='O':
			print('O Win')
			print(table)
			
		elif tl=='X' and tc=='X' and tr=='X':
			print('X Win')
			print(table)
			
		elif ml=='O' and mc=='O' and mr=='O':
			print('O Win')
			print(table)
			
		elif ml=='X' and mc=='X' and mr=='X':
			print('X Win')
			print(table)
			
		elif bl=='O' and bc=='O' and br=='O':
			print('O Win')
			print(table)
			
		elif bl=='X' and bc=='X' and br=='X':
			print('X Win')
			print(table)
			
		# Win |
		elif tl=='O' and ml=='O' and bl=='O':
			print('O Win')
			print(table)
			
		elif tl=='X' and ml=='X' and bl=='X':
			print('X Win')
			print(table)
			
		elif tc=='O' and mc=='O' and bc=='O':
			print('O Win')
			print(table)
			
		elif tc=='X' and mc=='X' and bc=='X':
			print('X Win')
			print(table)
			
		elif tr=='O' and mr=='O' and br=='O':
			print('O Win')
			print(table)
			
		elif tr=='X' and mr=='X' and br=='X':
			print('X Win')
			print(table)
			
		# Win \\ //
		elif tl=='O' and mc=='O' and br=='O':
			print('O Win')
			print(table)
			
		elif tl=='X' and mc=='X' and br=='X':
			print('X Win')
			print(table)
			
		elif tr=='O' and mc=='O' and bl=='O':
			print('O Win')
			print(table)
			
		elif tr=='X' and mc=='X' and bl=='X':
			print('X Win')
			print(table)
			
		else:
			dd = ''
	print('Exiting')
except:
	print('\n------------------\nYou Press Ctrl + C\n------------------')