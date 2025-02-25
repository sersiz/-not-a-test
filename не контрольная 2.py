import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных (пример с использованием вашего файла)
df = pd.read_excel('data.xlsx')

# Создание фигуры с тремя подграфиками
plt.figure(figsize=(18, 6))

# 1. Гистограмма
plt.subplot(1, 3, 1)
sns.histplot(df['Y'], kde=True, color='blue')
plt.title('Гистограмма Y')
plt.xlabel('Y')
plt.ylabel('Частота')

# 2. Круговая диаграмма
plt.subplot(1, 3, 2)
df['X'].value_counts().plot.pie(autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'lightcoral', 'lightsalmon'])
plt.title('Круговая диаграмма дней недели')
plt.ylabel('')

# 3. Диаграмма "ящик с усами"
plt.subplot(1, 3, 3)
sns.boxplot(x='X', y='Y', data=df, palette='pastel')
plt.title('Ящик с усами по дням недели')


# Отображение всех графиков
plt.tight_layout()
plt.show()