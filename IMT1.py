
m = float (input("Введите ваш вес в кг: "))
h = float (input("Введите ваш рост в см: "))
h = h/100
index_mass = float(m / (h*h))


if float(index_mass) < 16:
    print ("Индекс тела равен:", "%.2f" % index_mass, "кг/м²", "и у Вас выраженный дефицит массы тела")
elif float(index_mass) >= 16 and float(index_mass) <= 18.5:
    print ("Индекс тела равен:", "%.2f" % index_mass, "кг/м²", "и у Вас Недостаточный (дефицит) массы тела")
elif float(index_mass) >= 18.5 and float(index_mass) <= 24.99:
    print ("Индекс тела равен:", "%.2f" % index_mass, "кг/м²", "у Вас норма!")
elif float(index_mass) >= 18.5 and float(index_mass) <= 24.99:
    print ("Индекс тела равен:", "%.2f" % index_mass, "кг/м²", "у Вас норма!")
elif float(index_mass) >= 25 and float(index_mass) <= 30:
    print ("Индекс тела равен:", "%.2f" % index_mass, "кг/м²", "и у Вас избыточная масса тела (предожирение)")
elif float(index_mass) >= 30 and float(index_mass) <= 35:
    print ("Индекс тела равен:", "%.2f" % index_mass, "кг/м²", "и у Вас ожирение")
elif float(index_mass) >= 35 and float(index_mass) <= 40:
    print ("Индекс тела равен:", "%.2f" % index_mass, "кг/м²", "и у Вас резкое ожирение")
elif float(index_mass) >= 40:
    print ("Индекс тела равен:", "%.2f" % index_mass, "кг/м²", "и у Вас очень резкое ожирение!")


Tab = """
====================================================
|16 и менее     Выраженный дефицит массы тела        |
|16—18,5     Недостаточная (дефицит) масса тела   |
|18,5—24,99     Норма                                |
|25—30             Избыточная масса тела (предожирение) |
|30—35             Ожирение                             |
|35—40             Ожирение резкое                      |
|40 и более     Очень резкое ожирение                |
====================================================
"""

print (Tab)
input('Press ENTER to exit')