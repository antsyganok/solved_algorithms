# Яндекс Контест Задача D. "Хаотичность погоды."

days = int(input())
temps = list(map(int, input().strip().split()))


def chaothic_weather(days, temps):
    if days == 1:
        return 1
    else:
        counter = 0
        for day in range(days):
            now = temps[day]
            if day == 0 and now > temps[day+1]:
                counter += 1
            elif day == days - 1 and now > temps[day-1]:
                counter += 1
            elif now > temps[day-1] and now > temps[day+1]:
                counter += 1
    return counter


print(chaothic_weather(days, temps))
