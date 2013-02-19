pic_sorter
==========

I had to do a hard drive recovery. This dumped all the Jpegs on my drive in one folder. The file names did not make sense. Also it was hard to browse through them since I am used to browsing my pictures in folders by the year->month->date they were taken on.
This script takes a directory of .jpeg files.
Grabs them one by one and creates folders and puts them in the respwctive folders using the  EXIF data.
This also filters out images smaller than 100 KB (because thoise are I mages i dont particularly care for) or images with no EXIF data.
