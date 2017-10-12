#coding=utf-8

# 完成debug,创建Data_matrix实体类就可以获得datax 和datay
import numpy as np
import time

class User:
    def __init__(self, info):
        self.id = int(info[0])
        self.grade = int(info[1])
        self.sex = int(info[2])
        if info[3] != '':
            timestring = info[3]
            self.brith = int(time.mktime(time.strptime(timestring, '%Y-%m-%d %H:%M:%S')))
        else:
            self.brith = -99
        self.age = int(info[4])
        if info[5] != '':
            timestring = info[5]
            self.babyBrith = int(time.mktime(time.strptime(timestring, '%Y-%m-%d %H:%M:%S')))
        else:
            self.babyBrith = -99
        self.babyAge = int(info[6])
        self.babySex = int(info[7])


class Product:
    def __init__(self, info):
        i = 5
        self.product = int(info[0])
        self.store = int(info[1])
        self.brand = int(info[2])
        self.cla = int(info[3])
        self.label = info[4]
        self.price = int(info[5])
        self.labelNum = 0
        self.labels = []
        self.dealLabel()

    def dealLabel(self):
        self.labels = self.label.split(' ')
        self.labelNum = self.labels.__len__();

class Behavior:
    def __init__(self, info):
        self.userId = int(info[0])
        self.productId = int(info[1])
        self.time = int(info[2])
        self.cla_be = int(info[3])


def getUserInfo():
    user_info = open('./user_info.txt', 'r')
    user_line = user_info.readline()
    user_line = user_line.split('\n')[0]
    users = []
    while user_line != '':
        user_data = user_line.split('\t')
        users.append(User(user_data))
        user_line = user_info.readline()
        user_line = user_line.split('\n')[0]
    return users


def getProductInfo():
    product_info = open('./product_info.txt', 'r')
    product_line = product_info.readline()
    product_line = product_line.split('\n')[0]
    products = []
    while product_line != '':
        product_data = product_line.split('\t')
        product = Product(product_data)
        products.append(product)
        product_line = product_info.readline()
        product_line = product_line.split('\n')[0]
    return products

def getBehaviorInfo():
    behavior_info = open('./behavior_info.txt', 'r')
    behavior_line = behavior_info.readline()
    behavior_line = behavior_line.split('\n')[0]
    behaviors = []
    while behavior_line != '':
        behavior_data = behavior_line.split('\t')
        behavior = Behavior(behavior_data)
        behaviors.append(behavior)
        behavior_line = behavior_info.readline()
        behavior_line = behavior_line.split('\n')[0]
    return behaviors



class Data_matrix:

    def __init__(self):
        self.users = getUserInfo()
        # self.products = getProductInfo()
        self.behaviors = getBehaviorInfo()
        self.inputMatrix = np.array
        self.outputMatrix = np.array
        self.getMatrix()

    def getMatrix(self):
        inputDataList = []
        outputDataList = []
        for behavior in self.behaviors:
            temp_data_list = []
            temp_out_list = []
            user = self.users[behavior.userId - 1]
            # length = 9
            temp_data_list.append(behavior.userId)
            temp_data_list.append(int(user.grade))
            temp_data_list.append(user.brith)
            temp_data_list.append(user.age)
            temp_data_list.append(user.sex)
            temp_data_list.append(user.babyBrith)
            temp_data_list.append(user.babyAge)
            temp_data_list.append(user.babySex)
            temp_data_list.append(behavior.time)

            # length = 2
            temp_out_list.append(behavior.productId)
            temp_out_list.append(behavior.cla_be)

            inputDataList.append(temp_data_list)
            outputDataList.append(temp_out_list)

        self.inputMatrix = np.array(inputDataList)
        self.outputMatrix = np.array(outputDataList)

#test code

# data = Data_matrix()
#
# data_x = data.inputMatrixdata = Data_matrix()

# data_x = data.inputMatrix
# data_y = data.outputMatrix
#
# print data.inputMatrix[1], data.outputMatrix[0]
# data_y = data.outputMatrix
#
# print data.inputMatrix[1], data.outputMatrix[0]