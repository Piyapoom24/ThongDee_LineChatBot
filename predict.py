from PIL import Image
from Classifier_model import SomOClassifier
from linebot.v3.messaging import TextMessage

def Classify(event):
    id = event.message.id
    path = f'./img/{id}.jpg'
    # image = Image.open(path)

    predictor = SomOClassifier(path)
    conf, label = predictor.predict()
    confidence = conf*100

    return label, f"{float(confidence):.2f}"