from PIL import Image
import torch
import torchvision
import torchvision.transforms as transforms
import torchvision.models as models
import torch.nn as nn

class FruitClassify:
    def __init__(self, path):
        self.path = path
        self.check_point = torch.load('Classify_ob_model.pth', map_location=torch.device('cpu'), weights_only=True)
        self.model = models.mobilenet_v3_large(weights='IMAGENET1K_V2')
        nr_filters = self.model.classifier[0].in_features
        self.model.classifier = nn.Sequential(nn.Linear(nr_filters, 1, bias=False))
        # self.model.classifier[0].weight.data.zero_()
        self.model.load_state_dict(self.check_point['model_state_dict'])
        self.model = self.model.to('cpu')
        self.label = {0:"Not pomelo", 1:"Pomelo"}

        self.transforms = transforms.Compose([
            transforms.Resize((232, 232), interpolation=torchvision.transforms.InterpolationMode.BILINEAR),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
    
    def predict(self):
        img = Image.open(self.path)
        self.model.eval()
        sample = self.transforms(img).unsqueeze(0).to('cpu')
        with torch.no_grad():
            output = self.model(sample)
            p = torch.sigmoid((output))
            p = p.to('cpu').data.item()
        
        if p < 0.5:
            label = self.label[0]

        else:
            label = self.label[1]

        return label