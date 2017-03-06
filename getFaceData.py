#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import os

#配置区域

#图片文件路径
path = 'presidents/'
#face++参数
api_key = ''
api_secret = ''
#图片文件后缀
endName = 'jpg'
#特征点key
keyPoints = ['mouth_upper_lip_left_contour2',
             'contour_chin',
             'mouth_upper_lip_left_contour1',
             'left_eye_upper_left_quarter',
             'left_eyebrow_lower_middle',
             'mouth_upper_lip_left_contour3',
             'left_eyebrow_lower_left_quarter',
             'nose_contour_left3',
             'right_eye_pupil',
             'left_eyebrow_upper_left_quarter',
             'mouth_lower_lip_left_contour2',
             'mouth_lower_lip_right_contour3',
             'mouth_lower_lip_bottom',
             'contour_left9',
             'left_eye_lower_right_quarter',
             'mouth_lower_lip_top',
             'contour_right6',
             'right_eye_bottom',
             'contour_right9',
             'contour_left6',
             'contour_left5',
             'contour_left4',
             'contour_left3',
             'contour_left2',
             'contour_left1',
             'left_eye_lower_left_quarter',
             'contour_right1',
             'contour_right3',
             'contour_right2',
             'contour_right5',
             'contour_right4',
             'contour_right7',
             'left_eyebrow_left_corner',
             'nose_right',
             'nose_tip',
             'nose_contour_lower_middle',
             'right_eye_top',
             'mouth_lower_lip_left_contour3',
             'right_eye_right_corner',
             'left_eye_left_corner',
             'right_eye_lower_right_quarter',
             'mouth_upper_lip_right_contour2',
             'right_eyebrow_lower_right_quarter',
             'contour_left7',
             'mouth_right_corner',
             'mouth_lower_lip_right_contour1',
             'contour_right8',
             'left_eyebrow_right_corner',
             'right_eye_center',
             'left_eye_pupil',
             'left_eye_upper_right_quarter',
             'mouth_upper_lip_top',
             'nose_left',
             'right_eyebrow_lower_middle',
             'left_eye_top',
             'left_eye_center',
             'contour_left8',
             'right_eyebrow_left_corner',
             'right_eye_left_corner',
             'right_eyebrow_lower_left_quarter',
             'left_eye_bottom',
             'mouth_left_corner',
             'right_eyebrow_upper_left_quarter',
             'left_eye_right_corner',
             'right_eye_lower_left_quarter',
             'right_eyebrow_right_corner',
             'right_eye_upper_left_quarter',
             'left_eyebrow_upper_middle',
             'mouth_lower_lip_right_contour2',
             'nose_contour_left1',
             'nose_contour_left2',
             'mouth_upper_lip_right_contour1',
             'nose_contour_right1',
             'nose_contour_right2',
             'nose_contour_right3',
             'mouth_upper_lip_bottom',
             'right_eyebrow_upper_middle',
             'left_eyebrow_lower_right_quarter',
             'right_eyebrow_upper_right_quarter',
             'mouth_upper_lip_right_contour3',
             'left_eyebrow_upper_right_quarter',
             'right_eye_upper_right_quarter',
             'mouth_lower_lip_left_contour1']

#读取文件名
def readFile():
    list = os.listdir(path)
    return list

#请求数据
def requestData():
    url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
    param = {
        'api_key':api_key,
        'api_secret':api_secret,
        # 'img_url': '',
        'return_landmark':1
    }
    fileList = readFile()

    for index,file in enumerate(fileList):
        # fileName = file[0:8]
        fileName = file
        if file.endswith("."+endName):
            if not os.path.isfile(path+fileName+'.txt'):
                files = {'image_file': open(path + file, 'rb')}
                print '请求fece++接口中...获取'+file+'图像信息'
                res = requests.post(url,data = param,files = files)
                if res.status_code == 200:
                    # print (index+1)/len(fileList)*100
                    print '数据获取成功，开始字段解析  已完成'+str(int((index+1.0)/len(fileList)*100))+'%'
                    dataProcess(res,fileName)
                else:
                    print '数据获取失败，终止文件为'+fileName
                    break



def dataProcess(param,fileName):
    landmark = param.json()['faces'][0]['landmark']
    result = ''
    for index,i in enumerate(keyPoints):
        # if i == 'right_eye_right_corner':
        #     print 'right_eye_right_corner索引值为：'+ str(index) +' '+ '具体值为：'+str(landmark[i])
        # if i == 'left_eye_left_corner':
        #     print 'left_eye_left_corner索引值为：'+ str(index)+' '+ '具体值为：'+str(landmark[i])
        list = landmark[i]
        result += str(list['x']) +' '+ str(list['y']) + '\n'

    print '字段解析完成，文件写入开始'
    writeFile(result,fileName)

def writeFile(result,fileName):
    fs = open(path+fileName+'.txt','w+')
    fs.write(result)
    fs.close()
    print fileName+'.txt写入完成!'


def init():
    requestData()

init()




