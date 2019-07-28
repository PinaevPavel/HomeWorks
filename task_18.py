import random 
# сделать список с загаданными словами. 
WORDS = ['кошка', 'дом', 'дверь', 'улица']

G_WORDS = WORDS[random.randint(0, 4)]
    #Загадывает рандомное слово из списка 
    #Добавляет это слово в переменную G_WORDS
print('Компьютер загадал слово из', len(G_WORDS), 'букв, необходимо его отгадать.') #Отладка

def cipher_words(G_WORDS):
	#Превращает загаданное слово в набор звезд
	i = 0
	cipher = ''
	while i < len(G_WORDS):
		i = i + 1
		cipher = cipher + "*"
	return cipher

def input_words(words, cipher, x):
	latter = input('Введите 1 букву: ')
	if len(latter) != 1:
		raise IndexError('Вы ввели больше одного символа, необходимо ввести один символ.')
	if latter in words:
		#if words.index(latter) == 0:
		#	cipher = latter + cipher[words.index(latter) + 1:]
		#else:
		cipher = cipher[:words.index(latter)] + latter + cipher[words.index(latter) + 1:]
		words = words[:words.index(latter)] + '*' + words[words.index(latter) + 1:]
	else:
		print('Введенной буквы нет в загаданном слове')
		print('Осталось', 10-x, 'попыток.')
		x = x + 1
	print(cipher)#Отладка
	return cipher, words, x
	#принимает букву от игрока, обрабатывает ошибки:
	#не принимает 2 буквы или цифры

def main():
	x = 0 "cmd": ["/usr/local/bin/python3", "-u", "$file"],
 "file_regex": "^[ ]File \"(...?)\", line ([0-9]*)",
 "selector": "source.python"
	words = G_WORDS
	cipher = cipher_words(G_WORDS)
	print(cipher)#Отладка
	while not G_WORDS == cipher:
		if x == 10:
			print('Вы не отгадали слово')
			break
		try:
			cipher, words, x = input_words(words, cipher, x)
		except IndexError as e:
			print(e)
	print('Игра окончена')
#Проверяет исключения в программе и вообще главная функция
main()

#Нужно поменять звездочку на отгаданную букву, по индексу в загаданном слове