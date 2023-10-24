from wmdetection.models import get_watermarks_detection_model
from wmdetection.pipelines.predictor import WatermarksPredictor
from PIL import Image

# checkpoint is automatically downloaded
model, transforms = get_watermarks_detection_model(
    'convnext-tiny', 
    fp16=False, 
    cache_dir='weights',
    device='cpu'
)
predictor = WatermarksPredictor(model, transforms, 'cpu')
