import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest

# Крок 1: Завантаження даних
def load_data(filepath):
    return pd.read_csv(filepath)

# Крок 2: Очищення даних
def clean_data(data):
    # Перевірка на відсутні значення
    print(data.isnull().sum())
    # Заповнення відсутніх значень
    data = data.ffill()
    return data

# Крок 3: Виявлення аномалій
def detect_anomalies(data, column):
    model = IsolationForest(n_estimators=100, contamination=float(.01))
    data['anomaly'] = model.fit_predict(data[[column]])
    anomalies = data[data['anomaly'] == -1]
    return anomalies

# Крок 4: Аналіз типів атак
def analyze_attack_types(data):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x='Attack Type')
    plt.title('Розподіл типів атак')
    plt.show()

# Крок 5: Кореляційний аналіз
def correlation_analysis(data):
    numerical_data = data.select_dtypes(include=['float64', 'int64'])
    correlation_matrix = numerical_data.corr()
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f")
    plt.title('Кореляційна матриця')
    plt.show()

# Крок 6: Візуалізація даних
def visualize_data(data):
    # Гістограма для змінної
    plt.figure(figsize=(10, 6))
    sns.histplot(data=data, x='Packet Length', bins=30, kde=True)
    plt.title('Розподіл довжини пакетів')
    plt.show()

# Крок 7: Висновки
def draw_conclusions():
    print("На основі проведеного аналізу було ідентифіковано ключові шаблони атак...")

# Основна програма
if __name__ == '__main__':
    data = load_data('cybersecurity_attacks.csv')
    data = clean_data(data)
    anomalies = detect_anomalies(data, 'Packet Length')
    analyze_attack_types(data)
    correlation_analysis(data)
    visualize_data(data)
    draw_conclusions()