# diagnostics4u.github.io

# LiverUSRecon: Automatic 3D Reconstruction and Volumetry of the Liver with a Few Partial Ultrasound Scans

###  MICCAI 2024

[Kaushalya Sivayogaraj](170597a@uom.lk)1, [Sahan
Guruge](sahang@physiol.cmb.ac.lk)2, [Udari Liyanage](udari@anat.cmb.ac.lk)2,
[Jeevani Udupihille](jeevani.udupihille@med.pdn.ac.lk)3,  [Saroj
Jayasinghe](saroj@clinmed.cmb.ac.lk)2,  [Gerard
Fernando](gerardf@zone24x7.com)4,  [Ranga Rodrigo](ranga@uom.lk)1 [Rukshani
Liyanaarachchi](rukshanil@uom.lk)1

1University of Moratuwa, 2University of Colombo, 3University of Peradeniya,
4Zone 24x7 (Pvt) Ltd,

[ __ Paper ](https://arxiv.org/pdf/2406.19336) [ __ arXiv
](https://arxiv.org/abs/2406.19336)

![Interpolate start reference image.](main.PNG)

##  LiverUSRecon Overview:Binary masks of the three US slices generate the
shape parameters through the parametric regression MLP. These warp the SSM to
generate the 3D liver reconstruction.

##  US segmentation and 3D reconstruction results. Three input US sagittal
plane images, corresponding segmentations, and 3D liver reconstructions using
the shape parameters for three subjects.

## Abstract

3D reconstruction of the liver for volume measurement and 3D visual shape
analysis using an accessible medical imaging modality like ultrasound (US)
imaging is important. We present the first method capable of reconstructing
liver from few partial Ultrasound scans aquired at midline, midclavicular line
and anterior-auxillay line.

To the best of our knowledge, this is the first automated deep learning method
that calculates the liver volume from three incomplete 2D US scans. Further,
we introduce a new US liver database with parallel, annotated CT scans
comprising 134 scans.

Our volumetry results are statistically closer to the ground-truth volumes
obtained from CT scans than the volumes computed by radiologists using the
Childs’ method.

Your browser does not support the video tag.  Your browser does not support
the video tag.

##  US segmentation and 3D reconstruction results. Three input US sagittal
plane images, corresponding segmentations, and 3D liver reconstructions using
the shape parameters for three subjects.

## Main Results

Statistical analysis: RMSE is less in estimated volumes from our method.
Paired t-test shows that there is no significant difference in volumes between
CT and our method (p > 0.05). Our method is statistically more accurate. µ:
mean difference, SEM: standard error mean.

![Interpolate start reference image.](main_results.PNG)

## Volume Comparision

A subset of liver volume estimated by radiologists using Child’s method (US
Vol), CT segmentation (CT Vol), and the volumes computed using the proposed
method (Our Vol).

![Interpolate start reference image.](volumes.PNG)

## BibTeX

    
    
    @article{kaushalya2024liverusrecon,
      author    = {Kaushalya Sivayogaraj, Sahan T. Guruge, Udari Liyanage, Jeevani Udupihille, Saroj Jayasinghe, Gerard Fernando, Ranga Rodrigo, M. Rukshani Liyanaarachchi},
      title     = {LiverUSRecon: Automatic 3D Reconstruction and Volumetry of the Liver with a Few Partial Ultrasound Scans},
      journal   = {MICCAI},
      year      = {2024},
    }

