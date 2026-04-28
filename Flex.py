from linebot.v3.messaging.models import FlexContainer
from Classifier_model import SomOClassifier

def show_pred(image, time):
    predictor = SomOClassifier(image)
    conf, label = predictor.predict()
    confidence = f"{float(conf*100):.2f}"

    is_sweet = label == "Sweet"
    header_bg  = "#F9FFF5" if is_sweet else "#F8F8F8"
    result_color = "#2E7D00" if is_sweet else "#666666"
    bar_color  = "#00B900" if is_sweet else "#AAAAAA"
    badge_bg   = "#F0FFF0" if is_sweet else "#F5F5F5"
    badge_border = "#B2DFB2" if is_sweet else "#DDDDDD"
    badge_text = "✅ ส้มโอหวาน" if is_sweet else "❌ ส้มโอไม่หวาน"

    flex_pred = {
      "type": "bubble",
      "size": "mega",
      "header": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "weight": "bold",
            "size": "lg",
            "color": "#1A1A1A",
            "gravity": "center",
            "flex": 1,
            "text": "📊 ผลการทำนาย"
          },
          {
            "type": "text",
            "text": time,
            "size": "sm",
            "color": "#AAAAAA",
            "align": "end",
            "gravity": "center",
            "flex": 0
          }
        ],
        "backgroundColor": header_bg,
        "paddingAll": "14px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "PREDICTION RESULT",
            "size": "xs",
            "color": "#969494",
            "align": "center",
            "weight": "bold"
          },
          {
            "type": "separator",
            "margin": "sm",
            "color": "#d6d6d6"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "Prediction:",
                "size": "md",
                "color": "#888888",
                "gravity": "center"
              },
              {
                "type": "text",
                "text": label,
                "size": "md",
                "color": result_color,
                "weight": "bold",
                "align": "end",
                "gravity": "center"
              }
            ],
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "Confidence:",
                "size": "md",
                "color": "#888888",
                "gravity": "center"
              },
              {
                "type": "text",
                "text": confidence,
                "size": "md",
                "color": result_color,
                "weight": "bold",
                "align": "end",
                "gravity": "center"
              }
            ],
            "margin": "sm"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "width": confidence,
                "height": "8px",
                "backgroundColor": bar_color,
                "cornerRadius": "99px"
              }
            ],
            "backgroundColor": "#EEEEEE",
            "cornerRadius": "99px",
            "height": "8px",
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": badge_text,
                "color": bar_color,
                "weight": "bold",
                "size": "lg",
                "align": "center"
              }
            ],
            "backgroundColor": badge_bg ,
            "cornerRadius": "99px",
            "paddingAll": "8px",
            "margin": "lg",
            "borderWidth": "1px",
            "borderColor": badge_border
          }
        ],
        "backgroundColor": "#FFFFFF",
        "paddingAll": "16px"
      }
    }
    return FlexContainer.from_dict(flex_pred), label

def not_pomelo():
    flex = {
  "type": "bubble",
  "size": "mega",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "❌",
            "size": "xxl",
            "align": "center",
            "gravity": "center",
            "flex": 0
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ตรวจไม่พบรูปส้มโอ",
                "weight": "bold",
                "size": "xl",
                "color": "#CC0000"
              },
              {
                "type": "text",
                "text": "กรุณาส่งรูปส้มโอมาอีกทีค่ะ 🙏",
                "size": "sm",
                "color": "#888888",
                "wrap": True
              }
            ],
            "spacing": "xs",
            "margin": "md"
          }
        ],
        "spacing": "md",
        "margin": "sm"
      }
    ],
    "backgroundColor": "#FFF5F5",
    "paddingAll": "20px"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "📋 วิธีถ่ายรูปที่ถูกต้อง",
        "weight": "bold",
        "size": "md",
        "color": "#1A5C1A"
      },
      {
        "type": "separator",
        "margin": "sm",
        "color": "#00B900"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "1",
                    "color": "#FFFFFF",
                    "align": "center",
                    "gravity": "center",
                    "weight": "bold"
                  }
                ],
                "backgroundColor": "#00B900",
                "cornerRadius": "20px",
                "width": "28px",
                "height": "28px",
                "justifyContent": "center",
                "alignItems": "center"
              },
              {
                "type": "text",
                "text": "เปิดกล้องถ่ายรูป 📷",
                "margin": "md",
                "gravity": "center",
                "color": "#333333"
              }
            ],
            "spacing": "sm"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "2",
                    "color": "#FFFFFF",
                    "align": "center",
                    "gravity": "center",
                    "weight": "bold"
                  }
                ],
                "backgroundColor": "#00B900",
                "cornerRadius": "20px",
                "width": "28px",
                "height": "28px",
                "justifyContent": "center",
                "alignItems": "center"
              },
              {
                "type": "text",
                "text": "ถ่ายรูปด้านล่างของส้มโอ 🖼️",
                "margin": "md",
                "gravity": "center",
                "color": "#333333",
                "wrap": True,
                "flex": 1
              }
            ],
            "spacing": "sm"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "3",
                    "color": "#FFFFFF",
                    "align": "center",
                    "gravity": "center",
                    "weight": "bold"
                  }
                ],
                "backgroundColor": "#00B900",
                "cornerRadius": "20px",
                "width": "28px",
                "height": "28px",
                "justifyContent": "center",
                "alignItems": "center"
              },
              {
                "type": "text",
                "text": "กดส่งรูป แล้วรอผลลัพธ์ 💯",
                "margin": "md",
                "gravity": "center",
                "color": "#333333"
              }
            ],
            "spacing": "sm"
          }
        ],
        "spacing": "lg",
        "margin": "lg"
      }
    ],
    "backgroundColor": "#FFFFFF",
    "paddingAll": "20px"
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "📷  ถ่ายภาพใหม่",
          "data": "action=open_camera",
          "displayText": "ฉันต้องการถ่ายภาพส้มโอ"
        },
        "style": "primary",
        "color": "#00B900",
        "height": "sm"
      }
    ],
    "backgroundColor": "#FFFFFF",
    "paddingAll": "16px"
  }
}
    return FlexContainer.from_dict(flex)

def how_to_use():
    contents = {
        "type": "bubble",
        "size": "mega",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "วิธีใช้งาน",
                    "weight": "bold",
                    "size": "xl",
                    "color": "#1A1A1A",
                    "align": "center"
                },
                {
                    "type": "text",
                    "text": "ตรวจสอบความหวานส้มโอด้วยภาพถ่าย",
                    "size": "sm",
                    "color": "#888888",
                    "align": "center",
                    "margin": "sm"
                }
            ],
            "backgroundColor": "#FFFFFF",
            "paddingAll": "20px",
            "paddingBottom": "10px"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "separator",
                    "color": "#F0F0F0"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "1",
                                            "color": "#FFFFFF",
                                            "align": "center",
                                            "gravity": "center",
                                            "weight": "bold",
                                            "size": "sm"
                                        }
                                    ],
                                    "backgroundColor": "#00B900",
                                    "cornerRadius": "20px",
                                    "width": "30px",
                                    "height": "30px",
                                    "justifyContent": "center",
                                    "alignItems": "center"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "เปิดกล้องถ่ายรูป 📷",
                                            "weight": "bold",
                                            "size": "sm",
                                            "color": "#1A1A1A"
                                        },
                                        {
                                            "type": "text",
                                            "text": "กดปุ่มด้านล่างเพื่อเปิดกล้อง",
                                            "size": "xs",
                                            "color": "#AAAAAA",
                                            "margin": "xs"
                                        }
                                    ],
                                    "margin": "lg",
                                    "justifyContent": "center"
                                }
                            ],
                            "alignItems": "center"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "2",
                                            "color": "#FFFFFF",
                                            "align": "center",
                                            "gravity": "center",
                                            "weight": "bold",
                                            "size": "sm"
                                        }
                                    ],
                                    "backgroundColor": "#00B900",
                                    "cornerRadius": "20px",
                                    "width": "30px",
                                    "height": "30px",
                                    "justifyContent": "center",
                                    "alignItems": "center"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "ถ่ายรูปด้านล่างของส้มโอ 🖼️",
                                            "weight": "bold",
                                            "size": "sm",
                                            "color": "#1A1A1A"
                                        },
                                        {
                                            "type": "text",
                                            "text": "ให้เห็นก้นส้มโอชัดเจน ไม่เบลอ",
                                            "size": "xs",
                                            "color": "#AAAAAA",
                                            "margin": "xs",
                                            "wrap": True
                                        }
                                    ],
                                    "margin": "lg",
                                    "justifyContent": "center"
                                }
                            ],
                            "alignItems": "center"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "3",
                                            "color": "#FFFFFF",
                                            "align": "center",
                                            "gravity": "center",
                                            "weight": "bold",
                                            "size": "sm"
                                        }
                                    ],
                                    "backgroundColor": "#00B900",
                                    "cornerRadius": "20px",
                                    "width": "30px",
                                    "height": "30px",
                                    "justifyContent": "center",
                                    "alignItems": "center"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "กดส่งรูป ⬆️",
                                            "weight": "bold",
                                            "size": "sm",
                                            "color": "#1A1A1A"
                                        },
                                        {
                                            "type": "text",
                                            "text": "ระบบจะวิเคราะห์รูปอัตโนมัติ",
                                            "size": "xs",
                                            "color": "#AAAAAA",
                                            "margin": "xs"
                                        }
                                    ],
                                    "margin": "lg",
                                    "justifyContent": "center"
                                }
                            ],
                            "alignItems": "center"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "4",
                                            "color": "#FFFFFF",
                                            "align": "center",
                                            "gravity": "center",
                                            "weight": "bold",
                                            "size": "sm"
                                        }
                                    ],
                                    "backgroundColor": "#00B900",
                                    "cornerRadius": "20px",
                                    "width": "30px",
                                    "height": "30px",
                                    "justifyContent": "center",
                                    "alignItems": "center"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "รอรับผลลัพธ์ 💯",
                                            "weight": "bold",
                                            "size": "sm",
                                            "color": "#1A1A1A"
                                        },
                                        {
                                            "type": "text",
                                            "text": "น้องทองดีจะแจ้งผลคุณภาพส้มโอทันที",
                                            "size": "xs",
                                            "color": "#AAAAAA",
                                            "margin": "xs"
                                        }
                                    ],
                                    "margin": "lg",
                                    "justifyContent": "center"
                                }
                            ],
                            "alignItems": "center"
                        }
                    ],
                    "spacing": "xl",
                    "margin": "xl"
                },
                {
                    "type": "separator",
                    "color": "#F0F0F0",
                    "margin": "xl"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "text",
                            "text": "💡",
                            "size": "sm",
                            "flex": 0
                        },
                        {
                            "type": "text",
                            "text": "ถ่ายในที่มีแสงสว่างเพียงพอเพื่อผลลัพธ์ที่ดีที่สุด",
                            "size": "xs",
                            "color": "#888888",
                            "wrap": True,
                            "margin": "sm",
                            "flex": 1
                        }
                    ],
                    "margin": "lg",
                    "alignItems": "flex-start"
                }
            ],
            "backgroundColor": "#FFFFFF",
            "paddingAll": "20px"
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "postback",
                        "label": "📷  เริ่มถ่ายภาพเลย",
                        "data": "action=open_camera",
                        "displayText": "ฉันต้องการถ่ายภาพส้มโอ"
                    },
                    "style": "primary",
                    "color": "#00B900",
                    "height": "sm"
                }
            ],
            "backgroundColor": "#FFFFFF",
            "paddingAll": "16px",
            "paddingTop": "8px"
        }
    }
    return FlexContainer.from_dict(contents)