import glob
import os
import shutil

src = 'C:\\Users\\KimHeeSu\\Desktop\\shw_practice\\data\\rear_signal_dataset'
path = '.\\data\\vehicle_rear_signal'
file_list = glob.glob(path)
#print(file_list)
id = 0

def search(src):
    filenames = os.listdir(src)
    global id
    for filename in filenames:
        full_filename = os.path.join(src,filename)
        if os.path.isdir(full_filename):
            if filename == 'light_mask':
                id += 1
                print(id)
            search(full_filename)
        else:
            ext = os.path.splitext(full_filename)[-1]
            if ext == '.png':
                if 'OOO' in full_filename:
                    id_dir = path+'/OOO/' + str(id)
                    if not os.path.exists(id_dir):
                        os.makedirs(id_dir)
                    shutil.move(full_filename, id_dir+'\\'+filename)

                if 'BOO' in full_filename:
                    id_dir = path+'/BOO/' + str(id)
                    if not os.path.exists(id_dir):
                        os.makedirs(id_dir)
                    shutil.move(full_filename, id_dir+'\\'+filename)

                if 'OLO' in full_filename:
                    id_dir = path+'/OLO/' + str(id)
                    if not os.path.exists(id_dir):
                        os.makedirs(id_dir)
                    shutil.move(full_filename, id_dir+'\\'+filename)
                if 'BLO' in full_filename:
                    id_dir = path+'/BLO/' + str(id)
                    if not os.path.exists(id_dir):
                        os.makedirs(id_dir)
                    shutil.move(full_filename, id_dir+'\\'+filename)
                if 'OOR' in full_filename:
                    id_dir = path+'/OOR/' + str(id)
                    if not os.path.exists(id_dir):
                        os.makedirs(id_dir)
                    shutil.move(full_filename, id_dir+'\\'+filename)
                if 'BOR' in full_filename:
                    id_dir = path+'/BOR/' + str(id)
                    if not os.path.exists(id_dir):
                        os.makedirs(id_dir)
                    shutil.move(full_filename, id_dir+'\\'+filename)
                if 'OLR' in full_filename:
                    id_dir = path+'/OLR/' + str(id)
                    if not os.path.exists(id_dir):
                        os.makedirs(id_dir)
                    shutil.move(full_filename, id_dir+'\\'+filename)
                if 'BLR' in full_filename:
                    id_dir = path+'/BLR/' + str(id)
                    if not os.path.exists(id_dir):
                        os.makedirs(id_dir)
                    shutil.move(full_filename, id_dir+'\\'+filename)

if __name__ == "__main__":
    search(src)
