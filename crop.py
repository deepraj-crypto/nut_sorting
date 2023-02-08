import cv2
import numpy as np

# circles = np.zeros((4,2),int)
# counter = 0
#
# def cordinates(event,x,y,flags,paras):
#     global counter
#     if event == cv2.EVENT_LBUTTONDOWN:
#
#         circles[counter]=x,y
#         counter=counter+1
#         print(circles)
#
# img = cv2.imread("./IMG-20221226-WA0003.jpg")
#
# while True:
#     if counter == 4:
#
#         width, height = 250, 350
#         # imgCropped = img[circles[0][0]:circles[0][1], circles[1][0]:circles[1][1]]
#         imgCropped = img[200:422, 222:400]
#         cv2.imshow('Output', imgCropped)
#
#     for x in range(0,4):
#         cv2.circle(img,(circles[x][0],circles[x][1]),3,(0,255,0),cv2.FILLED)
#
#     cv2.imshow("orgimage", img)
#     # cv2.imshow("Output", imgOutput)
#     cv2.setMouseCallback('orgimage', cordinates)
#
#     cv2.waitKey(1)

img = cv2.imread('./IMG-20221226-WA0003.jpg')
img_dup = np.copy(img)
mouse_pressed = False
# defining starting and ending point of rectangle (crop image region)
starting_x = starting_y = ending_x = ending_y = -1


def mousebutton(event, x, y, flags, param):
    global img_dup, starting_x, starting_y, ending_x, ending_y, mouse_pressed
    # if left mouse button is pressed then takes the cursor position at starting_x and starting_y
    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_pressed = True
        starting_x, starting_y = x, y
        img_dup = np.copy(img)

    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_pressed:
            img_dup = np.copy(img)
            cv2.rectangle(img_dup, (starting_x, starting_y), (x, y), (0, 255, 0), 1)
    # final position of rectange if left mouse button is up then takes the cursor position at ending_x and ending_y
    elif event == cv2.EVENT_LBUTTONUP:
        mouse_pressed = False
        ending_x, ending_y = x, y


cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.setMouseCallback('image', mousebutton)
counter = 0
cropped_imgs=[]
ev=True
while ev:
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow('image', img_dup)
    k = cv2.waitKey(1)
    if k == ord('c'):
        # remove these condition and try to play weird output will give you idea why its done
        if starting_y > ending_y:
            starting_y, ending_y = ending_y, starting_y
        if starting_x > ending_x:
            starting_x, ending_x = ending_x, starting_x
        if ending_y - starting_y > 1 and ending_x - starting_x > 0:
            image = img[starting_y:ending_y, starting_x:ending_x]
            img_dup = np.copy(image)
            img_dup_resized = cv2.resize(img_dup,(400,400),None, 0.8, 0.8)
            # saving cropped images in an array
            cropped_imgs.append(img_dup_resized)
            counter += 1
        elif k == 27:
            break

    if counter == 7:
        ev = False
    #
# print(len(cropped_imgs))

# stacking the images
stacked=np.hstack((cropped_imgs[0],cropped_imgs[1],cropped_imgs[2],cropped_imgs[3],cropped_imgs[4],cropped_imgs[5],
                   cropped_imgs[6]))
cv2.namedWindow("stacked images", cv2.WINDOW_NORMAL)
cv2.imshow('stacked images', stacked)
cv2.waitKey(0)
cv2.imwrite('stacked.jpg', stacked)


cv2.destroyAllWindows()