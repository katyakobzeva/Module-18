sum_tickets = 0 #полная стоимость билетов
discount = 0 #скидка
qnt_tickets = int(input("Введите количество билетов: ")) #количество билетов
for i in range(qnt_tickets):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        sum_tickets += 0
    elif 18 <= age <= 24:
        sum_tickets += 990
    else:
        sum_tickets += 1390
    if qnt_tickets >= 3:
        discount = (int(sum_tickets * 0.9))
        print("Стоимость билета со скидкой: ", discount, " рублей.")
    else:
        print("Стоимость билетов: ", sum_tickets, " рублей.")

