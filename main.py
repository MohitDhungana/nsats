import cv2
import numpy as np


# # import test image and convert to grayscale
# img1 = cv2.imread('a5_busy3.jpg', 0)
#
# # resize image
# img1 = cv2.resize(img1, (950, 540))
# # img1 = img1[0:539, 0:1493]
#
# # import sample image and convert to grayscale
# img2 = cv2.imread('a5_free.jpg', 0)
#
# # resize image
# img2 = cv2.resize(img2, (950, 540))
# # img2 = img2[0:539, 0:1493]
#
# # edge calculation of both images
# edges1 = cv2.Canny(img1, 100, 200)
# edge_testimg = cv2.Canny(img2, 100, 200)


def show_images(edges1, edge_testimg):
    # fuction to show original and edge picture
    # cv2.imshow('originalbusy', img1)
    cv2.imshow('edgesbusy', edges1)
    # cv2.imshow('originalfree', img2)
    cv2.imshow('edgesfree', edge_testimg)


def find_pixels(edges1, edge_testimg):
    # finding matched pixels
    matched_pixels = 0
    and_var = np.logical_and(edge_testimg, edges1)
    matched_pixels = np.sum(and_var == True)
    # for i in range(0, 4096):
    #     for j in range(0, 2304):
    #         if edge_testimg[i][j] == 255 and edges1[i][j] == 255:
    #             matched_pixels += 1
    return matched_pixels


def calc_percentage(match_num, edge_testimg):
    # calculation of traffic density using pixel matching
    white_pixels = np.sum(edge_testimg == 255)

    print("Matched pixels= " + str(match_num))
    print("White pixels in sample= " + str(white_pixels))
    perc = 100 - ((match_num / white_pixels) * 100)
    # print("traffic density = " + str(perc) + " %")
    return perc

# function call to display images
# show_images(edges1, edge_testimg)
#
# match_num = find_pixels(edges1, edge_testimg)
#
# calc_percentage(match_num)
#
# # close window and exit execution
# cv2.waitKey(0)
# cv2.destroyAllWindows()
