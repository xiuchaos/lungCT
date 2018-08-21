# lungCT
> Following [Julian's Blog](http://juliandewit.github.io/kaggle-ndsb2017/)
start from Aug 20.

**Goal**
To predict the development of lung cancer in a patient given a set of CT images.

**Solution**
To spoonfeed a neural network with examples with a better snr and a more direct relationship between the labels and the features. 
	* Train a network to detect nodules and predict the malignancy of detected nodules.
	* Estimate the chance that the patient would develop a cancer given this information and some other features.



### 1. Preprocessing 

**step1_preprocess_ndsb.py**
	* This will extract all the *ndsb* dicom files , scale to 1x1x1 mm, and make a directory containing .png slice images. Lung segmentation mask images are also generated. They will be used later in the process for faster predicting.

**step1_preprocess_luna16.py**
	* This will extract all the *LUNA* source files , scale to 1x1x1 mm, and make a directory containing .png slice images. Lung segmentation mask images are also generated. This step also generates various CSV files for positive and negative examples.

**step1b_preprocess_make_train_cubes.py**
	The nodule detectors are trained on positive and negative 3d cubes which must be generated from the *LUNA16 and NDSB* datasets. step1b_preprocess_make_train_cubes.py takes the different csv files and cuts out 3d cubes from the patient slices. The cubes are saved in different directories. 

**resources/step1_preprocess_mass_segmenter.py** 
	generate the mass u-net trainset. The generated resized images + labels is provided in this archive so this step does not need to be run. However, this file can be used to regenerate the traindata.


### 2. Training neural nets

**step2_train_nodule_detector.py**
	train the 3D convnets that detect nodules and predict malignancy.T his will train various combinations of positive and negative labels. The resulting models (NAMES) are stored in the ./workdir directory and the final results are copied to the models folder.

**step2_train_mass_segmenter.py**
	train the mass detector. It trains 3 folds and final models are stored in the models (names) folder. Training the 3D convnets will be around 10 hours per piece. The 3 mass detector folds will take around 8 hours in total.


### 3. Predicting neural nets

**step3_predict_nodules.py**
	 detect nodules in a 3d grid per patient. The detected nodules and predicted malignancy are stored per patient in a separate directory. 


### 4. Training of submissions, combining submissions

**step4_train_submissions.py**
	Based on the per-patient csv’s the masses.csv and other metadata we will train an **xgboost model** to generate submissions. 

	There are 3 levels of submissions. First the per-model submissions. (level1). Different models are combined in level2, and Daniel’s submissions are added. These level 2 submissions will be combined (averaged) into one final submission. Below are the different models that will be generated/combined.

	**Level 1**
	Luna16_fs (trained on full luna16 set)
	Luna16_ndsbposneg v1 (trained on luna16 + manual pos/neg labels in ndsb)
	Luna16_ndsbposneg v2 (trained on luna16 + manual pos/neg labels in ndsb)
	Daniel model 1
	Daniel model 2
	posneg, daniel will be averaged into one level 2 model

	**Level 2**
	Luna16_fs
	Luna16_ndsbposneg
	Daniel


These 3 models will be averaged into 1 final_submission.csv
