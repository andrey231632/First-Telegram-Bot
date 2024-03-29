import numpy as np
from io import BytesIO
import cv2
import tensorflow as tf
from model_congiguration import img_size, name_class


class MLData:

    def __init__(self):

        self.class_names = name_class

        self.model = tf.keras.models.load_model('../models/cifar_classifier.model2')

    def h_photo(self, update, context):

        ''' Обработка и предсказание маркера входящего визобржения от пользователя. '''

        file = context.bot.get_file(update.message.photo[-1].file_id)
        f = BytesIO(file.download_as_bytearray())
        file_bytes = np.asarray(bytearray(f.read()), dtype=np.uint8)

        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        img = cv2.resize(img, (32, 32), interpolation=cv2.INTER_AREA)
        img = img.reshape(img_size)

        prediction = self.model.predict(np.array(img / 255))

        return self.class_names[np.argmax(prediction)]
