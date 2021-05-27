import cv2
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import time
import numpy as np
from matplotlib.colors import to_rgb
from skimage import io
from mrcnn.model import mold_image
from mrcnn.model import MaskRCNN
from mrcnn.config import Config

pathImage = "/home/c1611760/image"

# Load Model
MODEL_DIR = "\"/model\""

CLASSES_MAP = {
    1: "without_mask",
    2: "mask_weared_incorrect",
    3: "with_mask"
}
COLOR_MAP = {
    1: "red",
    2: "yellow",
    3: "lime"
}


class PredictionConfig(Config):
	NAME = "face_mask_detection_config"
	NUM_CLASSES = 1 + 3  # Background + 3 classes
	# Set GPU configs for testing, would raise errors if not set this way
	GPU_COUNT = 1
	IMAGES_PER_GPU = 1


cfg = PredictionConfig()
mdl = MaskRCNN(mode='inference', model_dir=MODEL_DIR, config=cfg)

weight_path = os.path.join(
    MODEL_DIR[1:-1],
    'mask_rcnn_face_mask_detection_config_0050.h5'  # Name of weight
)
mdl.load_weights(
	"model/mask_rcnn_face_mask_detection_config_0050.h5", by_name=True)


def getNewFile():
    path = pathImage
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)


IMG_PATH = getNewFile()
test_img = io.imread(IMG_PATH)


scaled_image = mold_image(test_img, cfg)
sample = np.expand_dims(scaled_image, 0)
yhat = mdl.detect(sample, verbose=0)[0]

plotted_img = np.copy(test_img)
for i, box in enumerate(yhat['rois']):
  y1, x1, y2, x2 = box
  label_id = yhat['class_ids'][i]
  start = (x1, y1)
  end = (x2, y2)

  color = COLOR_MAP[label_id]
  color = to_rgb(color)
  color = (np.array(color)*255)
  color = tuple(color)
  plotted_img = cv2.rectangle(plotted_img, start, end, color, 3)


timestamp = int(time.time())
# This is just an example name format, change name based on need
save_path = 'objek/{}_{}'.format(timestamp, "detection.jpg")
io.imsave(
    save_path,
    plotted_img
)

# print(save_path)
