# # # import cv2
# # #
# # # img = cv2.imread('a5_busy.jpg', 0)
# # # img = cv2.resize(img, (950, 540))
# # # edge = cv2.Canny(img, 100, 200)
# # # cv2.imwrite('edge.jpg', edge)
# # # cv2.imshow('edge',edge)
# # # cv2.waitKey(0)
# # # cv2.destroyAllWindows()
# # import mysql.connector
# #
# # from mysql.connector import errorcode
# # #
# # # try:
# # #     mydb = mysql.connector.connect(user="root", database="test", )
# # # except mysql.connector.Error as err:
# # #     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
# # #         print("Something is wrong with your user name or password")
# # #     elif err.errno == errorcode.ER_BAD_DB_ERROR:
# # #         print("Database does not exist")
# # #     else:
# # #         print(err)
# # # else:
# # #     print("Connected to Database")
# # #
# # # mycursor = mydb.cursor()
# # # sql = "INSERT INTO test_table (crn,name) values (%s,%s)"
# # # val = 2,'mohit'
# # # mycursor.execute(sql, val)
# # # mydb.commit()
# # # print("Successfully inserted to NSATS database.\n")
# # import datetime
# #
# # dt = datetime.datetime.now()
# # # print ("Current date and time using str method of datetime object:")
# # # print(str(dt))
# # print(dt.strftime("%Y-%m-%d %H:%M:%S"))
# import cv2
# import numpy as np
#
# img1 = cv2.imread('simple.jpg', 0)
# edge1 = cv2.Canny(img1, 100, 200)
# cv2.imshow('edf', edge1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import tensorflow as tf
# import os
# # os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# hello = tf.constant('Hello, TensorFlow!')
# sess = tf.Session()
# print(sess.run(hello))
#
# a=tf.constant(10)
# b=tf.constant(32)
# print(sess.run(a + b))
