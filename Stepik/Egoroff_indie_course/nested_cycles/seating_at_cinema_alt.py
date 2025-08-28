"""
Наивное решение без вложеных циклов, сначала решил, потом вспомнил,
что нужно использовать вложеные циклы.
"""
booked = ["Р.1, М.2", "Р.2, М.5", "Р.3, М.1", "Р.4, М.7", "Р.5, М.10"]
occupied = {(int(hall.split(', ')[0].split('.')[1]), int(hall.split(', ')[1].split('.')[1])) for hall in booked}

for row in range(1, 6):
    print(' '.join('X' if (row, seat) in occupied else 'O' for seat in range(1, 11)))
