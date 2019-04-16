import cv2
import os
import main
import inserttodb



def extractFrames(pathIn, pathOut):
    junction_id = 1

    try:
        os.mkdir(pathOut)
    except(FileExistsError):
        print('path already exists')

    cap = cv2.VideoCapture(pathIn, 0)
    count = 1
    # num=1
    # frameRate = cap.get(5)
    while cap.isOpened():
        # Capture frame-by-frame
        # Go to the 'count*100' sec. position where count is in millisecond
        cap.set(cv2.CAP_PROP_POS_MSEC, count * 100)
        ret, frame = cap.read()
        if ret == True:
            print('Read %dth frame: ' % count, ret)
            # cv2.imwrite(os.path.join(pathOut, "frame{:d}.jpg".format(count)), frame)  # save frame as JPEG file
            # cv2.imwrite(os.path.join(pathOut, "frame.jpg"), frame)  # save frame as JPEG file
            cv2.imwrite('frame.jpg', frame)

            # load images
            sample_img = cv2.imread('sample.jpg', 0)
            # test_img = cv2.imread('frames/frame.jpg', 0)
            test_img = cv2.imread('frame.jpg', 0)

            # canny edge detection
            edge_sampleimg = cv2.Canny(sample_img, 100, 200)
            edge_testimg = cv2.Canny(test_img, 100, 200)
            # cv2.imwrite('edge'+str(num)+'.jpg',edge_testimg)
            # num+=1

            # calculations
            match_num = main.find_pixels(edge_testimg, edge_sampleimg)
            perc = main.calc_percentage(match_num, edge_testimg)
            count += 5
            inserttodb.insert_to_db(junction_id, perc)
            junction_id += 1
            if junction_id == 5:
                junction_id += 1
        else:
            print('completed!!')
            break

    # When everything done, release the capture
    cap.release()


extractFrames('traffic_video_2.mp4', 'frames')  # video file name and folder name
cv2.waitKey(0)
cv2.destroyAllWindows()
