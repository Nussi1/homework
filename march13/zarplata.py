О = int(input('укажите оклад: '))
Дк = int(input('укажите количество календарных дней по производственному календарю: '))
Дф = int(input('укажите количество фактически отработанных дней: '))
П = int(input('премии и надбавки: '))
Н = 13
У = int(input('введите сумму удержаний: '))
ЗП = (О/Дк*Дф+П)*((100-Н)/100)-У
print(ЗП)
