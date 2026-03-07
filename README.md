# LiverUSRecon: Automatic 3D Reconstruction and Volumetry of the Liver with a Few Partial Ultrasound Scans

This website holds information for [LiverUSRecon: Automatic 3D Reconstruction and Volumetry of the Liver with a Few Partial Ultrasound Scans](https://arxiv.org/pdf/2406.19336)

## 📰 News
* Codes are available at [LiverUSRecon](https://github.com/diagnostics4u/diagnostics4u.github.io/).
* If you need the data, please email to [Kaushalya Sivayogaraj](mailto:170597a@uom.lk).  
* Weights are available at [Segmentation model](https://duvad-research.s3.amazonaws.com/pretrained_models/models/seg_model_epoch_100.pkl) and [Reconstruction model](https://duvad-research.s3.amazonaws.com/pretrained_models/models/parametric_model_epoch_100.pkl).

###  MICCAI 2024

[Kaushalya Sivayogaraj](mailto:170597a@uom.lk), 
[Sahan T. Guruge](mailto:sahang@physiol.cmb.ac.lk), [Udari Liyanage](mailto:udari@anat.cmb.ac.lk),
[Jeevani Udupihille](mailto:jeevani.udupihille@med.pdn.ac.lk),  [Saroj Jayasinghe](mailto:saroj@clinmed.cmb.ac.lk),
[Gerard Fernando](mailto:gerardf@zone24x7.com),  [Ranga Rodrigo](mailto:ranga@uom.lk), 
[Rukshani Liyanaarachchi](mailto:rukshanil@uom.lk)

![Interpolate start reference image.](./videos/usliverrecon_fo_gif.gif)

3D reconstruction of the liver for volume measurement and 3D visual shape
analysis using an accessible medical imaging modality like ultrasound (US)
imaging is important. We present the first method capable of reconstructing
liver from few partial Ultrasound scans aquired at midline, midclavicular line
and anterior-auxillay line. To the best of our knowledge, this is the first automated deep learning method
that calculates the liver volume from three incomplete 2D US scans. Further,
we introduce a new US liver database with parallel, annotated CT scans
comprising 134 scans.Our volumetry results are statistically closer to the ground-truth volumes
obtained from CT scans than the volumes computed by radiologists using the
Childs’ method.

## Ultrasound segmentation and 3D reconstruction results
![Overall framework 3D Reconstruction](./videos/3d.gif)


### 3D Reconstruction
![Overla[ between GT and prediction]](./videos/overlap.gif)
![Absoulte point to point distance](./videos/distance.gif)

## Statistical analysis

![Main Results](./images/main_results.PNG)

## Volume Comparision

![Volume comparision](./images/volumes.PNG)


## Running

### 1. Download Google pre-trained ViT model
* [Download R50-ViT-B_16 models in this link](https://console.cloud.google.com/storage/vit_models/): R50-ViT-B_16
* Move the downloaded model to folder `./model/vit_checkpoint/imagenet21k/` and rename it to `R50-ViT-B_16.npz`
* Download the pretrained segmentation and reconstruction models from [pretrained segmentation models](https://duvad-research.s3.amazonaws.com/pretrained_models/models/seg_model_epoch_100.pkl) [pretrained reconstruction models](https://duvad-research.s3.amazonaws.com/pretrained_models/models/parametric_model_epoch_100.pkl) and move it to folder named "models" under the results folder

### 2. Prepare data

* Please email to [Kaushalya Sivayogaraj](170597a@uom.lk) to collect the inference datasets.

### 3. Download liver dataset SSM information

* Download SSM information [shape parameters](https://duvad-research.s3.amazonaws.com/pretrained_models/liver_ssm/VT.txt), [mean shape](https://duvad-research.s3.amazonaws.com/pretrained_models/liver_ssm/liver_aver.obj), [pca ratio](https://duvad-research.s3.amazonaws.com/pretrained_models/liver_ssm/pca_ratio.txt) and [normalization info](https://duvad-research.s3.amazonaws.com/pretrained_models/liver_ssm/nor_list.txt)
* Once you download the SSM information, place it in the folder `./SSM/`

### 4. Environment

* Create an environment with python=3.7 and install the dependencies.

```bash
pip install -r requirements.txt
```

### 5. Train/Test

* Run the inference_liverusrecon script on the downloaded dataset. 
  
```bash
CUDA_VISIBLE_DEVICES=0 python inference_liverusrecon.py --inference {dataset path} --save {results path} --ssm_info {ssm_info path}
```

## Licenses

### Code Copyright (C) 2024 Zone24x7, Inc

Code is covered under the GNU Affero General Public License version 3.0
 
You should have received a copy of the GNU Affero General Public License along with the code. If not, see <https://www.gnu.org/licenses/>.


### ML Weights copyright (c) by Zone24x7, Inc

ML Weights are licensed under a
Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License.
 
You should have received a copy of the license along with this work. If not, see <https://creativecommons.org/licenses/by-nc-nd/3.0/>.


### Patient data copyright (c) by Zone24x7, Inc

Patient data is licensed under a
Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License.
 
You should have received a copy of the license along with this work. If not, see <https://creativecommons.org/licenses/by-nc-nd/3.0/>.


## Citation
If you find this project or this repository useful, please consider cite:

```bibtex
@InProceedings{10.1007/978-3-031-72104-5_42,
author="Sivayogaraj, Kaushalya
and Guruge, Sahan I. T.
and Liyanage, Udari A.
and Udupihille, Jeevani J.
and Jayasinghe, Saroj
and Fernando, Gerard M. X.
and Rodrigo, Ranga
and Liyanaarachchi, Rukshani",
editor="Linguraru, Marius George
and Dou, Qi
and Feragen, Aasa
and Giannarou, Stamatia
and Glocker, Ben
and Lekadir, Karim
and Schnabel, Julia A.",
title="LiverUSRecon: Automatic 3D Reconstruction and Volumetry of the Liver with a Few Partial Ultrasound Scans",
booktitle="Medical Image Computing and Computer Assisted Intervention -- MICCAI 2024",
year="2024",
publisher="Springer Nature Switzerland",
address="Cham",
pages="436--445",
isbn="978-3-031-72104-5"
}
```




