"""
Переменная people содержит строку в формате JSON,
в которой вы можете получить личные данные 100 человек.

Каждого человека представляет предмет (словарь) с ключами:

имя
страна
возраст
Распечатайте информацию о каждом человеке
в соответствии с примером ниже.

...
Melissa Crawford, Lebanon, 17
Paul Herrera, Kiribati, 17
Justin Galvan, Namibia, 19
Mary Estes, Montenegro, 19
Larry Bray, Brunei Darussalam, 21
...
<Имя>, <Страна>, <Возраст>
Распечатку необходимо отсортировать по возрасту,
а при равенстве возраста необходимо расположить в алфавитном порядке
"""

import json

# people = '[{"name": "Haley Whitney", "country":
# "British Indian Ocean Territory (Chagos Archipelago)", "age": 54},
#           {"name": "Matthew King", "country": "Colombia", "age": 34},
#           {"name": "Sean Sullivan", "country": "Mayotte", "age": 40},
#           {"name": "Erik Mclaughlin", "country": "Austria", "age": 24}]'

people = '[{"name": "Erik Mclaughlin", "country": "Austria", "age": 24}]'

pipz = json.loads(people)

for ppl in sorted(pipz, key=lambda x: (x['age'], x['name'])):
    print(*ppl.values(), sep=', ')
