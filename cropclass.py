from PIL import Image
import torch
import torchvision
import torchvision.transforms as transforms
import torchvision.models as models
import torch.nn as nn
# import matplotlib.pyplot as plt
import os
import io



class CropSomOClassifier:
    def __init__(self, path):
        self.path = path
        self.check_point = torch.load('mobile_adam01_model.pth', map_location=torch.device('cpu'))
        self.model = models.mobilenet_v3_large(weights='IMAGENET1K_V2')
        nr_filters = self.model.classifier[0].in_features
        self.model.classifier = nn.Sequential(nn.Linear(nr_filters, 1, bias=False))
        # self.model.classifier[0].weight.data.zero_()
        self.model.load_state_dict(self.check_point['model_state_dict'])
        self.model = self.model.to('cpu')
        self.label = {0:"Not Sweet", 1:"Sweet"}

        self.transforms = transforms.Compose([
            transforms.Resize((232, 232), interpolation=torchvision.transforms.InterpolationMode.BILINEAR),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

    def predict(self, base = 3456, target_size = 1800):
        img = Image.open(self.path)
        # img = img.resize((base, base))
        # print('original',img.size)

        original_width, original_height = img.size
        square_size = min(original_width, original_height)

        left = (original_width - square_size) // 2
        upper = (original_height - square_size) // 2
        right = left + square_size
        lower = upper + square_size
        square_image = img.crop((left, upper, right, lower))
        square_image = square_image.resize((base, base))

        square_width, square_height = square_image.size
        # print('square',square_image.size)

        left1 = (square_width - target_size) // 2
        upper1 = (square_height - target_size) // 2
        right1 = left1 + target_size
        lower1 = upper1 + target_size
        cropped_image = square_image.crop((left1, upper1, right1, lower1))
        # cropped_image.save(os.path.join(output_dir, 'images/{}.jpg'.format(img_id)))
        # print('crop',cropped_image.size)

        sample = self.transforms(cropped_image).unsqueeze(0).to('cpu')
        self.model.eval()
        
        with torch.no_grad():
            output = self.model(sample)
            p = torch.sigmoid((output))
            p = p.to('cpu').data.item()
        
        if p < 0.5:
            conf = round(1-p, 4)
            label = self.label[0]

        else:
            conf = round(p, 4)
            label = self.label[1]

        return conf, label