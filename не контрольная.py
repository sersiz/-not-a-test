import pandas as pd

#берём данные с ексель файла
df = pd.read_excel('что-то.xlsx')

#показываем содержимое файла
print("Содержимое файла:")
print(df)

#выбераем столбец
indexy = int(input("введите cтолбец: "))
print(df.iloc[:,indexy])

#выбераем строку из выброного столбца
indexx = int(input("введите cтрока: "))
print(df.iat[indexx,indexy])

#выводим ячейку
current_value = df.iat[indexx, indexy]
print(f"Текущее значение в ячейке [{indexx}, {indexy}]: {current_value}")

#меняем значение
new_value = input("Введите новое значение: ")

#обновляем ячейку
df.iat[indexx, indexy] = new_value

#сохраняем новое значение
df.to_excel('что-то.xlsx', index=False)
print("изменения сохранены")

#выводим детасет после всех изменений для уверенности
print("Содержимое файла:")
print(df)

