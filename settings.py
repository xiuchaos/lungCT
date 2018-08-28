import os
import socket 
COMPUTER_NAME = socket.gethostname()
print("Computer: ", COMPUTER_NAME)

WORKER_POOL_SIZE = 6

TARGET_VOXEL_MM = 1.00
MEAN_PIXEL_VALUE_NODULE = 41
LUNA_SUBSET_START_INDEX = 0
SEGMENTER_IMG_SIZE = 320

BASE_DIR = "/home/xiuchao/Desktop/lungCT/"
LUNA16_RAW_SRC_DIR = BASE_DIR + "luna_raw/"
NDSB3_RAW_SRC_DIR = "/home/xiuchao/winC/ndsb_dcm/"
EXTRA_DATA_DIR = "resources/"

BASE_DIR_SSD = "/home/xiuchao/winD/kaggle/"
NDSB3_EXTRACTED_IMAGE_DIR = BASE_DIR_SSD  + "ndsb3_extracted_images"
LUNA16_EXTRACTED_IMAGE_DIR = BASE_DIR_SSD + "luna16_extracted_images"
NDSB3_NODULE_DETECTION_DIR = BASE_DIR_SSD + "ndsb3_nodule_predictions"

