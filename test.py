from model.model import predictor
from PIL import Image



file = 'data/Screenshot from 2023-10-25 02-01-14.png'
is_watermarked = predictor.predict_image(Image.open(file))
print(is_watermarked)