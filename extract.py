from pdf2image import convert_from_path
import glob, os

count = 0
imagez = []
currentDir = os.path.realpath('.')
print(currentDir)

os.chdir(currentDir)
for file in glob.glob("*.pdf"):
    imagez.append(file)

for image in imagez:
    images = convert_from_path(currentDir+"\\"+image)
    for img in images:
        img.save('img'+str(count)+'.jpg', 'JPEG')
        count += 1
