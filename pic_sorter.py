from os import listdir
from os.path import isfile, join
from PIL import Image
from PIL.ExifTags import TAGS
import datetime
import shutil
import sys
import os

DATE_TAG = 306
DATE_STRING ='%Y:%m:%d %H:%M:%S'
created_dirs = list()
source_dir = sys.argv[1]
dest_dir = sys.argv[2]
files = listdir(source_dir)
created_dirs = list()

def create_folder_struct(date):
    year_path = "%s%s" % (dest_dir, date.year)
    month_path = "%s/%s_%s" % (year_path, date.year,date.month)
    date_path = "%s/%s_%s" % (month_path,date.month, date.day)
    if date_path in created_dirs:
        return date_path
    if not os.path.exists(year_path):
        os.mkdir(year_path)
    if not os.path.exists(month_path):
        os.mkdir(month_path)
    if not os.path.exists(date_path):
        os.mkdir(date_path)
    created_dirs.append(date_path)
    return date_path

def get_image_date(source_file):
    image = Image.open(source_file)
    info = image._getexif()
    date = datetime.datetime.strptime(info[DATE_TAG], DATE_STRING)
    return date

success, total = 0,0
print files
small_files = "%s%s" % (dest_dir,"small_files")
no_data = "%s%s" % (dest_dir,"no_data")
os.mkdir(small_files)
os.mkdir(no_data)
for f in files:
    source_file = source_dir+f
    try:
        size = os.path.getsize(source_file)/1024
        if size < 65:
            shutil.move(source_file, "%s/%s" % (small_files,f))
            continue
        date = get_image_date(source_file)
        path = create_folder_struct(date)
        dest_file = "%s/%s" % (path,f)
        shutil.move(source_file, dest_file)
        print source_file
        success += 1
    except Exception as err:
        shutil.move(source_file, "%s/%s" % (no_data,f))
        print "Error in file %s : %s" % (source_file, err)
    finally:
        total += 1
    if total % 10 ==0:
        print "success : %d, total : %d " % (success, total)
