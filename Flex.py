from linebot.v3.messaging.models import FlexContainer
import numpy as np
from predict import Classify

def show_pred(event, url):
    predict, conf = Classify(event)
    flex_pred = {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": url,
        "aspectMode": "cover",
        "aspectRatio": "20:20",
        "size": "full"
      },
      "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "Prediction Result",
          "weight": "bold",
          "size": "xl",
          "align": "center"
        },
        {
          "type": "separator",
          "color": "#778899",
          "margin": "sm"
        },
        {
          "type": "box",
          "layout": "horizontal",
          "contents": [
            {
              "type": "text",
              "text": "Prediction: ",
              "margin": "none",
              "size": "md"
            },
            {
              "type": "text",
              "text": f"{predict}",
              "weight": "bold",
              "color": "#336600"
            },
            {
              "type": "filler"
            }
          ],
          "spacing": "none",
          "margin": "md"
        },
        {
          "type": "box",
          "layout": "horizontal",
          "contents": [
            {
              "type": "text",
              "text": "Confidence: ",
              "margin": "none",
              "size": "md"
            },
            {
              "type": "text",
              "text": f"{conf}%",
              "weight": "bold",
              "color": "#336600",
              "flex": 2,
              "offsetStart": "sm"
            },
          ],
          "spacing": "none",
          "margin": "md"
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "filler"
                }
              ],
              "width": f"{conf}%",
              "backgroundColor": "#336600",
              "height": "8px",
              "spacing": "none"
            }
          ],
          "backgroundColor": "#D3D3D3",
          "height": "8px",
          "margin": "sm",
          "spacing": "none"
        },
        {
          "type": "text",
          "text": f"{conf}%",
          "weight": "bold",
          "align": "end",
          "size": "xs",
          "margin": "xs"
        }

      ]
    }
  }
    return FlexContainer.from_dict(flex_pred)

