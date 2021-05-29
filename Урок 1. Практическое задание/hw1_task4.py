"""
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""

activated_logins = [log1, log2, log3]

dict_logins = {log1 = '123', log2 = 'password', log3 = '1442If!jk', log4 = '001', log10 = '002'}

def check_login(name, password):
	if name in activated_logins:
		tekpas = dict_logins[name]
		if tekpas == password:
			print('успешно')
		else:
		    print('неверный login/password')
    elif name in list(dict_logins.keys()):
    	activate = input('Учетная запись не активиирована, активировать? (y/n)')
    	if activate = 'y':
    		activated_logins.append(name)
    		check_login(name, password)
        else:
        	print('всего доброго!')
    else:
    	print('неверный login/password')

#сложность O(N), где N или длина списка активированных логинов, или всех логинов (по одной из веток условия), в случае активации O(N) + O(N)  или O(N), т.к. вызываем рекурсивно

def check_login1(name, password):
	for curname in dict_logins:
		if name == curname:
			logged = False
			passmatch = False
			for nameact in activated_logins:
				if nameact == name:
					if password = dict_logins[curname]:
						
						logged = True
						passmatch = True
					else:
						print('Неверно')
						logged = True
						passmatch = False
    if logged == True and passmatch == True:
		print('Успешно')
	elif logged ==  True and passmatch = False:
		print('неверный login/password')
	else:
	    activate = input('Учетная запись не активиирована, активировать? (y/n)')
	    if activate = 'y':
			activated_logins.append(name)
    		check_login(name, password)
        else:
        	print('всего доброго!')
#сложность O(N1*N2)  или приближенно O(N^2), в случае активации удваивается, но приближенно то же значение

#сложность второго алгоритма больше сложности первого, так как используется вложенный цикл




