import tkinter as tk 
import time
import csv 

from sklearn.neural_network import MLPRegressor 

from sklearn.model_selection import train_test_split 

 from tqdm import tqdm

from sklearn.metrics import mean_absolute_error, mean_squared_error

y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

mae = mean_absolute_error(y_true, y_pred)
mse = mean_squared_error(y_true, y_pred)

print("MAE:", mae)
print("MSE:", mse)




# Функция для чтения данных из файла 

def read_data(filename): 

    data = [] 

    with open(filename, 'r') as file: 

        reader = csv.reader(file, delimiter=';') 

        next(reader)  # Пропуск заголовков 

        for row in reader: 

            row_values = [] 

            for value in row: 

                if value: 

                    row_values.append(float(value)) 

                else: 

                    row_values.append(0.0)  # Или другое значение по умолчанию 

            data.append(row_values) 

    X = [row[:-1] for row in data] 

    y = [row[-1] for row in data] 

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)  # Разделение на обучающую и тестовую выборки 

    model = MLPRegressor(hidden_layer_sizes=(10, 10), random_state=1, max_iter=50000) 

    model.fit(X_train, y_train) 

    return X_train, X_test, y_train, y_test, model 

 

 

# Функция для записи данных в файл 

def write_data(filename, data): 

    with open(filename, 'w', newline='') as file: 

        writer = csv.writer(file, delimiter=';') 

        writer.writerow(["Геофизика - Гектар", "Геофизика - Время года", "Геофизика - Работа в поле или лесу", 

                         "Геофизика - Спец техника", "Геодезия - Гектар", "Геодезия - Время года", 

                         "Геодезия - Зима или не зима", "Геодезия - Местность", "Геодезия - Подеревка", 

                         "Экология - Гектар", "Экология - Река или не река", "Экология - Проверка на радиацию", 

                         "Экология - Нужно ли спец. оборудование", "Геология - Количество скважин", 

                         "Геология - Просадка", "Геология - Зима или не зима", "Геология - Рельеф", 

                         "Гидрометеорология - Площадь в га", "Гидрометеорология - Река или нет", 

                         "Гидрометеорология - Рельеф", "Гидрометеорология - Сезон"]) 

        writer.writerows(data) 

 epochs = 10
for epoch in tqdm(range(epochs)):
    
    

# Функция для прогнозирования затрат с помощью персептрона 

def predict_costs(features, X_train, y_train): 

    model = MLPRegressor(hidden_layer_sizes=(10, 10), random_state=1, max_iter=20000) 

    model.fit(X_train, y_train) 

    return model.predict([features])[0] 
            time.sleep(0.1)  # Симуляция времени обучения
 

# Создание главного окна приложения 

app = tk.Tk() 

app.title("Прогноз затрат на изыскания") 

 

# Создание метки для выбора типа изыскания 

survey_label = tk.Label(app, text="Тип изыскания:") 

survey_label.grid(row=0, column=0) 

 

# Создание выпадающего списка для выбора типа изыскания 

survey_options = ["Геофизика", "Геодезия", "Геология", "Экология", "Гидрометеорология"] 

survey_var = tk.StringVar(app) 

survey_var.set(survey_options[0]) 

survey_menu = tk.OptionMenu(app, survey_var, *survey_options) 

survey_menu.grid(row=0, column=1) 

 

# Создание меток и полей ввода для каждого типа изыскания 

labels = [] 

entries = [] 

 

def create_survey_fields(survey_type): 

    if survey_type == "Геофизика": 

        labels.append(tk.Label(app, text="Количество гектар:")) 

        labels[-1].grid(row=1, column=0) 

        entries.append(tk.Entry(app)) 

        entries[-1].grid(row=1, column=1) 

 

        labels.append(tk.Label(app, text="Время года (0 - не зима, 1 - зима):")) 

        labels[-1].grid(row=2, column=0) 

        entries.append(tk.Entry(app)) 

        entries[-1].grid(row=2, column=1) 

 

        labels.append(tk.Label(app, text="Работа в поле или лесу (0 - поле, 1 - лес):")) 

        labels[-1].grid(row=3, column=0) 

        entries.append(tk.Entry(app)) 

        entries[-1].grid(row=3, column=1) 

 

        labels.append(tk.Label(app, text="Наличие спец.техники (0 - нет, 1 - есть):")) 

        labels[-1].grid(row=4, column=0) 

        entries.append(tk.Entry(app)) 

        entries[-1].grid(row=4, column=1) 

 

    elif survey_type == "Геодезия": 

        labels.append(tk.Label(app, text="Количество гектар:")) 

        labels[-1].grid(row=1, column=0) 

        entries.append(tk.Entry(app)) 

        entries[-1].grid(row=1, column=1) 

 

        labels.append(tk.Label(app, text="Время года (0 - не зима, 1 - зима):")) 

        labels[-1].grid(row=2, column=0) 

        entries.append(tk.Entry(app)) 

        entries[-1].grid(row=2, column=1) 

 

        labels.append(tk.Label(app, text="Местность (0 - равнинная, 1 - горная):")) 

        labels[-1].grid(row=3, column=0) 

        entries.append(tk.Entry(app)) 

        entries[-1].grid(row=3, column=1) 

 

        labels.append(tk.Label(app, text="Подеревка (0 - нет, 1 - есть):")) 

        labels[-1].grid(row=4, column=0) 

        entries.append(tk.Entry(app)) 

        entries[-1].grid(row=4, column=1) 

 

    elif survey_type == "Экология": 

        labels.append(tk.Label(app, text="Количество гектар:")) 

        labels[-1].grid(row=1, column=0) 

        entries.append(tk.Entry(app)) 

        entries[-1].grid(row=1, column=1) 

 

        labels.append(tk.Label(app, text="Река или не река (0 - нет, 1 - есть):")) 

        labels[-1].grid(row=2, column=0) 

        entries.append(tk.Entry(app)) 

        entries[-1].grid(row=2, column=1) 

 

        labels.append(tk.Label(app, text="Проверка на радиацию (0 - нет, 1 - есть):")) 

        labels[-1].grid(row=3, column=0) 

        entries.append(tk.Entry(app)) 

        entries[-1].grid(row=3, column=1) 

 

        labels.append(tk.Label(app, text="Нужно ли спец.оборудование (0 - нет, 1 - есть):")) 

        labels[-1].grid(row=4, column=0) 

        entries.append(tk.Entry(app)) 

        entries[-1].grid(row=4, column=1) 

 

    elif survey_type == "Геология": 

        labels.append(tk.Label(app, text="Количество скважин:")) 

        labels[-1].grid(row=1, column=0) 

        entries.append(tk.Entry(app)) 

        entries[-1].grid(row=1, column=1) 

 

        labels.append(tk.Label(app, text="Просадка (0 - нет, 1 - есть):")) 

        labels[-1].grid(row=2, column=0) 

        entries.append(tk.Entry(app)) 

        entries[-1].grid(row=2, column=1) 

 

        labels.append(tk.Label(app, text="Зима или не зима (0 - не зима, 1 - зима):")) 

        labels[-1].grid(row=3, column=0) 

        entries.append(tk.Entry(app)) 

        entries[-1].grid(row=3, column=1) 

 

        labels.append(tk.Label(app, text="Рельеф (0 - горный, 1 - в поле):")) 

        labels[-1].grid(row=4, column=0) 

        entries.append(tk.Entry(app)) 

        entries[-1].grid(row=4, column=1) 

 

    elif survey_type == "Гидрометеорология": 

        labels.append(tk.Label(app, text="Площадь в га:")) 

        labels[-1].grid(row=1, column=0) 

        entries.append(tk.Entry(app)) 

        entries[-1].grid(row=1, column=1) 

 

        labels.append(tk.Label(app, text="Река или нет (0 - нет, 1 - да):")) 

        labels[-1].grid(row=2, column=0) 

        entries.append(tk.Entry(app)) 

        entries[-1].grid(row=2, column=1) 

 

        labels.append(tk.Label(app, text="Рельеф (0 - горный, 1 - равнинный):")) 

        labels[-1].grid(row=3, column=0) 

        entries.append(tk.Entry(app)) 

        entries[-1].grid(row=3, column=1) 

 

        labels.append(tk.Label(app, text="Сезон (0 - лето, 1 - зима):")) 

        labels[-1].grid(row=4, column=0) 

        entries.append(tk.Entry(app)) 

        entries[-1].grid(row=4, column=1) 

 

# Функция для обработки события нажатия кнопки "Прогнозировать" 

def predict_button_click(): 

    survey_type = survey_var.get() 

    features = [float(entry.get()) for entry in entries] 

    X_train, X_test, y_train, y_test, model = read_data("data.csv") 

    predicted_costs = predict_costs(features, X_train, y_train) 

    result_label.config(text=f"Прогнозируемые затраты: {predicted_costs} тыс. руб.") 

 

    # Оценка производительности модели на тестовой выборке 

    test_score = model.score(X_test, y_test) 

    print(f"Оценка производительности на тестовой выборке: {test_score}") 

 

 

# Создание кнопки "Прогнозировать" 

predict_button = tk.Button(app, text="Прогнозировать", command=predict_button_click) 

predict_button.grid(row=5, column=0, columnspan=2) 

 

# Создание метки для вывода результата 

result_label = tk.Label(app, text="") 

result_label.grid(row=6, column=0, columnspan=2) 

 

# Обновление полей ввода при изменении типа изыскания 

def update_survey_fields(*args): 

    for label in labels: 

        label.grid_forget() 

    for entry in entries: 

        entry.grid_forget() 

    labels.clear() 

    entries.clear() 

    create_survey_fields(survey_var.get()) 

 

survey_var.trace("w", update_survey_fields) 

 

# Создание полей ввода для первого типа изыскания 

create_survey_fields(survey_options[0]) 

 

# Запуск главного цикла приложения 

app.mainloop()1 