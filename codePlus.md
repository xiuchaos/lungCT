
Aug 23. Luna16 image processing.

Problems:
1. coordinate system in itk
    itk_img = SimpleITK.ReadImage(src_path)
    img_array = SimpleITK.GetArrayFromImage(itk_img)

2. image processing: rescale
	img_array = helpers.rescale_patient_images(img_array, spacing, settings.TARGET_VOXEL_MM)

3. image processing: segment lung tissue 
	seg_img, mask = helpers.get_segmented_lungs(img.copy())

4. image processing: write image
	cv2.imwrite(dst_dir + "i.png", img * 255)

Solutions:
read itk tutorial
try on single img: resize,segment,imwrite


Linux commands:

	ps ax | grep python
	kill -9 ***
	killall -9 python

	top (shift+m)
	ps ****
	history

	sudo fdisk -l /dev/sda (-l, list) (dev, device)
	umount /dev/sda4
	sudo mount /dev/sda4 /home/xiuchao/winC

	tar -C /home/xiuchao/winC -xvf dcm.tar (decompress to target directory, C- change directory)


Linux commands: - release buffer and cache

	su (switch to root)
	# sync; echo 1 > /proc/sys/vm/drop_caches  (clear pageCache)
	# sync; echo 2 > /proc/sys/vm/drop_caches  (clear dentries and inodes)
	# sync; echo 3 > /proc/sys/vm/drop_caches  (1 and 2)










