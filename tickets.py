LOW_AGE_PRICE = 0
MIDDLE_AGE_PRICE = 990
HIGH_AGE_PRICE = 1390

ticketsQuantity = int(input("Введите количество участников: "))
totalSum = 0

for i in range(ticketsQuantity):
    guestAge = int(input("Введите возраст " + str(i+1) + " участника: "))
    if guestAge <= 18:
        totalSum += LOW_AGE_PRICE
    elif 18 < guestAge <= 25:
        totalSum += MIDDLE_AGE_PRICE
    elif guestAge > 25:
        totalSum += HIGH_AGE_PRICE

if ticketsQuantity > 3:
    discount = (totalSum * 10)/100
    totalSum -= discount

print("Итоговая стоимость билетов: ", int(totalSum))
