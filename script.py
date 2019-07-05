from PIL import Image
import os
import sys

#pass path to directory and final width, height of images as arguments when you run the script
directory = sys.argv[1]
w = int(sys.argv[2])
h = int(sys.argv[3])

for file_name in os.listdir(directory):
  print("Processing %s" % file_name)
  image = Image.open(os.path.join(directory, file_name))

  x,y = image.size
  new_dimensions = (w, h)
  output = image.resize(new_dimensions, Image.ANTIALIAS)

  output_file_name = os.path.join(directory, "small_" + file_name)
  output.save(output_file_name, "PNG", quality = 95)

print("All done")
