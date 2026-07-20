from PIL import Image
import cv2
import os

def playingback_to_gif (path):
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


def is_a_playingback (path):
    image = cv2.imread(path)
    try:
        if image.shape[1] == 1280 and image.shape[0] == 960:
            return(True)
        else:
            return(False)
    except:
        return(False)

def explore (root):
    for path, subdirs, files in os.walk(root):
        for name in files:
            file=os.path.join(path, name)
            print("opening",file)
            if is_a_playingback(file):
                print("converting",file,"to gif")
                playingback_to_gif(file)


rootdir="/"
explore(rootdir)
