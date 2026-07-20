from PIL import Image
import cv2

path="/Users/Eli/Downloads/DSC03709.JPG"
image = cv2.imread(path)
image_list=[]
for i in range(4):
    for u in range(4):
        ys, ye, xs, xe = i*240,(i+1)*240,u*320,(u+1)*320
        cropped_image = image[ys:ye, xs:xe]
        image_list.append(Image.fromarray(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)))

image_list[0].save(
            path.split('.')[0]+".gif",
            save_all=True,
            append_images=image_list[1:],
            duration=1000/30,
            loop=0)

