# SPDX-License-Identifier: AGPL-3.0-only


#    Copyright (C) 2024 Zone24x7, Inc  
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License version 3 as
#    published by the Free Software Foundation. 
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License version 3.0 for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
import os
import cv2
import numpy as np
import torch
from torch.utils.data.dataset import Dataset
from utils.utils import *

IMG_SIZE = 192

class OnlyTest(Dataset):
    def __init__(self, file_path):
        self.file_list = []
        for filename in os.listdir(file_path):
            self.file_list.append(os.path.join(file_path, filename))

    def __getitem__(self, index):
        name_list = ["ANTAX", "MIDLINE", "MCL"]
        img_list = []
        for name in name_list:   
            
            file_name = os.path.join(self.file_list[index], "liver-slice", name + ".png")
            img = cv2.imread(file_name, 0).astype(np.float32)
            if img.shape==(1470, 2316):
                img=img[90:,300:1800].copy()
                temp_img = np.zeros((1500, 1500))
                temp_img[60:1440, :] = img
                temp_img =cv2.resize(temp_img, (IMG_SIZE, IMG_SIZE)) 
                img_list.append(temp_img)

            elif img.shape==(889, 1639):
                img=img[:,0:1339].copy()
                temp_img = np.zeros((1500, 1500))
                temp_img[300:1189, 80:1419] = img
                temp_img =cv2.resize(temp_img, (IMG_SIZE, IMG_SIZE)) 
                img_list.append(temp_img)

            elif img.shape==(1113,548):
                img=img[137:837,28:].copy()
                temp_img = np.zeros((700, 700))
                temp_img[:,90:610] = img
                temp_img =cv2.resize(temp_img, (IMG_SIZE, IMG_SIZE)) 
                img_list.append(temp_img)

        img_data = np.array(img_list)
        img_data = normalization2(img_data, max=1, min=0)
        img_as_tensor = torch.from_numpy(img_data).float()

        return (img_as_tensor)