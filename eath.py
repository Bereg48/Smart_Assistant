import cv2
import numpy as np

# Указываем путь к файлу с весами и конфигурации модели
weights_path = 'yolov4.weights'
config_path = 'yolov4.cfg'

# Загружаем модель YOLO
net = cv2.dnn.readNet(weights_path, config_path)

# Указываем путь к файлу с классами объектов
names_path = 'coco.names'

# Загружаем список классов
with open(names_path) as f:
    class_names = f.read().splitlines()

# Захватываем видео с веб-камеры
camera = cv2.VideoCapture(0)

while True:
    # Считываем текущий кадр с веб-камеры
    ret, image = camera.read()

    # Получаем размеры кадра
    (H, W) = image.shape[:2]

    # Создаем blob изображения и передаем его в модель YOLO
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)

    # Получаем список обнаруженных объектов с их координатами и вероятностями
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    outputs = net.forward(output_layers)

    # Проходим по каждому обнаруженному объекту и выводим информацию
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = int(np.argmax(scores))
            confidence = float(scores[class_id])
            if confidence > 0.5:
                # Рисуем рамку и название класса объекта
                box = detection[0:4] * np.array([W, H, W, H])
                (x, y, w, h) = box.astype("int")
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(image, class_names[class_id], (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Показываем кадр с распознанными объектами
    cv2.imshow("Image", image)

    # Для выхода из цикла нажмите клавишу "q"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождаем ресурсы
camera.release()
cv2.destroyAllWindows()
