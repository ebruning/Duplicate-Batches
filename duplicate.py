# Create multiple batches in Express
# dst_folder is the batch folder where the new batches will be created
# src_folder is the folder used to create the new batches

import distutils.dir_util

src_folder="C:\ProgramData\Kofax\Kofax Express 2.0\Batches\Large Multiple\Batch0001"
dst_folder="C:\ProgramData\Kofax\Kofax Express 2.0\Batches\Large Multiple"

batch_name="Batch"
start_folder_number=2
end_folder_number=20

for count in range(start_folder_number, end_folder_number + 1):
    destination = dst_folder + "\\" + batch_name + str(count).zfill(4)
    print "copying " + src_folder + "-> " + destination 
    distutils.dir_util.copy_tree(src_folder, destination)