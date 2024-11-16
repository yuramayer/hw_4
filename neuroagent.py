
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


history = []

# Наша моделька
def create_model():
    model = Sequential([
        Dense(16, activation='relu', input_shape=(6,)),  # вход 6 данных, скрытый слой 16 нейронов
        Dense(16, activation='relu'),                    # допслой
        Dense(3, activation='softmax')                   # на выходе вероятность для каждого хода
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy')
    return model

model = create_model()

def neuroagent(observation, configuration):
    global history, model

    # Добавляем предыдущий ход соперника и наш ход в историю
    if observation.step > 0:
        history.append(observation.lastOpponentAction)
        history.append(history[-2])

    # Если данных недостаточно, выбираем случайный ход
    if len(history) < 6:
        action = int(np.random.randint(configuration.signs))
        history.append(action)
        return action

    # Формируем входные данные из последних 6 ходов
    input_data = np.array(history[-6:]).reshape(1, -1)

    # Прогнозируем следующий ход соперника
    opponent_pred = np.argmax(model.predict(input_data, verbose=0)[0])

    # Выбираем действие, которое побеждает предсказанный ход соперника
    action = (opponent_pred + 1) % configuration.signs
    history.append(action)

    # Обучение модели
    if observation.step > 0:
        target = np.zeros(configuration.signs)
        target[observation.lastOpponentAction] = 1
        model.fit(input_data, target.reshape(1, -1), epochs=1, verbose=0)

    return int(action)
