import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Загрузка данных из Excel файла
file_path = r'C:\Users\Admin\Desktop\New file\CentralAsia.xlsx'
df = pd.read_excel(file_path)

# Проверка, какие колонки есть в файле
st.write("Доступные колонки:", df.columns.tolist())

# Выбор страны для анализа
country = st.selectbox("Выберите страну:", df['country'].unique())

# Фильтрация данных по выбранной стране
country_data = df[df['country'] == country]

# Построение графиков
st.subheader(f"Данные для {country}")

# Гистограмма для 'F_mod_sev_ad'
plt.figure(figsize=(10, 5))
plt.bar(country_data['year'], country_data['F_mod_sev_ad'], color='skyblue')
plt.xlabel('Год')
plt.ylabel('Уровень умеренной нехватки продовольствия')
plt.title(f'Уровень умеренной нехватки продовольствия в {country}')
plt.xticks(rotation=45)
st.pyplot(plt)

# Линейный график для 'Pop_mod_sev_tot'
plt.figure(figsize=(10, 5))
plt.plot(country_data['year'], country_data['Pop_mod_sev_tot'], marker='o', linestyle='-', color='orange')
plt.xlabel('Год')
plt.ylabel('Общее население с умеренной нехваткой продовольствия')
plt.title(f'Общее население с умеренной нехваткой продовольствия в {country}')
plt.xticks(rotation=45)
st.pyplot(plt)

# Запуск приложения
st.title("Анализ продовольственной безопасности в Центральной Азии")
