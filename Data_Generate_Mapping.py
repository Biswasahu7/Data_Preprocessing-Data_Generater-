import pandas
import pandas as pd
import xlrd
import datetime
import time
from Replace_Function import Replace

# Data Generate if they will give 5 digit code excel

def Data_Generate(path):

    finalcode = []
    # File path we need to give

    xls = pandas.ExcelFile(path)

    # Runnig for loop to consider sheet name
    sheets = xls.sheet_names

    for n in sheets:
        # print(n)

        data = pd.read_excel(xls, n)

        for column in data:

            columndata = data[column]

            k = (columndata.values)
            # print(columnSeriesObj.values)

            for m in k:

                if m == 1:

                    v2 = ['BOST', 'BOX', 'BOY','BON',]
                    v = data.columns.get_loc(column)
                    x = v + 1
                    y = v + 2

                    val = data.iloc[10, y]
                    # print(val)

                    for i in v2:

                        if i in str(val):

                            val1 = len(data.iloc[10, y - 1])
                            # print(n)

                            if val1 <= 9:

                                data.insert(x, "Code Generate1", data.iloc[:, y] + data.iloc[:, y - 1])

                                for i in data['Code Generate1']:
                                    finalcode.append(Replace(str(i)))
                                cleanedList = [x for x in finalcode if str(x) != 'nan']

                            else:

                                for i in data.iloc[:,y-1]:
                                    finalcode.append(str(i))
                                cleanedList = [x for x in finalcode if str(x) != 'nan']
    return cleanedList

# IMPORTING LIBRARIES
import time
import pandas as pd
import datetime
import requests
import logging
import numpy as np
import numbers
import pandas
import xlrd

def Datamapping(path,code):

    # VARIABLES
    num11list = []
    num4_list = []
    num5list = []
    num6list = []
    num7_list = []
    num8_list = []
    num9_list = []
    num10_list = []
    wagonid = []
    det = 0
    out_dict = {}
    num5_list = []
    x = []
    z = []

    # CREATE DATAFRAME FOR STORING 4 TO 11 DIGIT DETECTED NUMBERS
    # df1 = pd.DataFrame(columns=["four", "five", "six", "seven", "eight", "nine", "ten", "eleven"])

        # Loading csv
    # df = pd.read_csv(path)
    # except:
    #     df = pd.read_excel(path,sheet_name = "T2 LS")
    #     print(df)
    # df = Data_Generate(path)
    # print("Column data-{}".format(df))

    # Assigning code column from data
    codecolumn = Data_Generate(path)

    # print(codecolumn)

    try:
        x = len(codecolumn[7])

        # if len(str(codecolumn[0] > 8)):
        if x > 7:
            # print("bbb")

            if code:
                # print(len(str(code)))
                # print(code)

                for r in code:

                    # print(type(code))

                    if len(str(r)) >= 11:
                        num11list.append(str(r))

                        # print("DETECTED-{}".format(r))
                        # wagonid.append(int(r))
                        # det=1

                    elif len(str(r)) == 10:
                        # if str(r) not in num10_list:
                        num10_list.append(str(r))

                    elif len(str(r)) == 9:

                        # if str(r) not in num9_list:
                        num9_list.append(str(r))
                        # print(num9_list)

                    elif len(str(r)) == 8:
                        # if str(r) not in num8_list:
                        num8_list.append(str(r))

                    elif len(str(r)) == 7:
                        # if str(r) not in num7_list:
                        num7_list.append(str(r))

                    elif len(str(r)) == 6:
                        # if str(r) not in num6list:
                        num6list.append(str(r))
                        # num56_list.append(str(r))

                    elif len(str(r)) == 5:
                        # if str(r) not in num5list:
                        num5list.append(str(r))
                        # print(num5list)
                        # num56_list.append(str(r))

                    elif len(str(r)) == 4:
                        num4_list.append(str(r))

                    temp_list = []

                    # CHECK IF ANY 11 DIGIT wagonid DETECTED...IF YES..THEN WE GOT ONE
                    if len(num11list) > 0:
                        n11 = max(num11list, key=num11list.count)
                        for i in codecolumn:
                            if str(n11) in str(i):
                                temp_list.append(str(n11))

                                db = 11
                                # logger.info("DETECTED-{}".format(n11))
                                # logger.info("Detected from 11 digit DB")
                                wagonid.append(n11)
                                # #print("DETECTED-{}".format(n11))
                                out_dict['Wagon_Number'] = str(n11)
                                # out_dict['Path'] = code_img_path_list
                                det = 1

                    if len(num11list) > 0:
                        n11 = max(num11list, key=num11list.count)
                        n11_5 = n11[-5:]
                        for i in codecolumn:
                            if str(n11_5) in str(i):
                                temp_list.append(str(i))

                                db = 11
                                # logger.info("DETECTED-{}".format(n11))
                                # logger.info("Detected from 11 digit DB")
                                wagonid.append(i)
                                # #print("DETECTED-{}".format(n11))
                                # out_dict['Wagon_Number'] = str(n11_5)
                                # out_dict['Path'] = code_img_path_list
                                det = 1

                                # break

                    # CHECK IN DB (INDIVIDUALLY FOR 7/8/9/10 DIGIT )
                    if det != 1:
                        if len(num10_list) > 0:
                            temp = max(num10_list, key=num10_list.count)
                            # for n in num10_list:
                            for wn in codecolumn:
                                if str(temp) in str(wn):
                                    det = 1
                                    db = 10
                                    wagonid.append(wn)
                                    # out_dict['Wagon_Number'] = str(wn)
                                    # out_dict['Path'] = code_img_path_list
                                    # logger.info("Detected from DB (10 digit)-{}".format(wn))
                                    temp_list.append(str(wn))

                    if det != 1:
                        if len(num10_list) > 0:
                            temp = max(num10_list, key=num10_list.count)
                            temp_5 = temp[-4:]
                            # for n in num10_list:
                            for wn in codecolumn:

                                if str(temp_5) in str(wn):
                                    det = 1
                                    db = 10
                                    wagonid.append(wn)
                                    # out_dict['Wagon_Number'] = str(wn)
                                    # out_dict['Path'] = code_img_path_list
                                    # logger.info("Detected from DB (10 digit)-{}".format(wn))
                                    temp_list.append(str(wn))

                                    # break
                    if det != 1:
                        if len(num9_list) > 0:
                            temp = max(num9_list, key=num9_list.count)
                            # for n in num9_list:
                            for wn in codecolumn:
                                if str(temp) in str(wn):
                                    det = 1
                                    db = 9
                                    wagonid.append(wn)
                                    # out_dict['Wagon_Number'] = str(wn)
                                    # out_dict['Path'] = code_img_path_list
                                    # logger.info("Detected from DB (9 digit)-{}".format(wn))
                                    temp_list.append(str(wn))

                    if det != 1:
                        if len(num9_list) > 0:
                            temp = max(num9_list, key=num9_list.count)
                            temp_5 = temp[-4:]
                            # for n in num9_list:
                            for wn in codecolumn:
                                if str(temp_5) in str(wn):
                                    det = 1
                                    db = 9
                                    wagonid.append(wn)
                                    # out_dict['Wagon_Number'] = str(wn)
                                    # out_dict['Path'] = code_img_path_list
                                    # logger.info("Detected from DB (9 digit)-{}".format(wn))
                                    temp_list.append(str(wn))
                                    # break
                    if det != 1:
                        if len(num8_list) > 0:
                            temp = max(num8_list, key=num8_list.count)
                            # for n in num8_list:
                            for wn in codecolumn:
                                if str(temp) in str(wn):
                                    det = 1
                                    db = 8
                                    wagonid.append(wn)
                                    # out_dict['Wagon_Number'] = str(wn)
                                    # out_dict['Path'] = code_img_path_list
                                    temp_list.append(str(wn))
                                    # logger.info("Detected from DB (8 digit)-{}".format(wn))
                                    # break

                    if det != 1:
                        if len(num8_list) > 0:
                            temp = max(num8_list, key=num8_list.count)
                            temp_5 = temp[-4:]
                            # for n in num8_list:
                            for wn in codecolumn:
                                if str(temp_5) in str(wn):
                                    det = 1
                                    db = 8
                                    wagonid.append(wn)
                                    # out_dict['Wagon_Number'] = str(wn)
                                    # out_dict['Path'] = code_img_path_list
                                    temp_list.append(str(wn))

                    if det != 1:
                        if len(num7_list) > 0:
                            temp = max(num7_list, key=num7_list.count)
                            # for n in num7_list:
                            for wn in codecolumn:
                                if str(temp) in str(wn):
                                    det = 1
                                    db = 7
                                    wagonid.append(wn)
                                    # out_dict['Wagon_Number'] = str(wn)
                                    # out_dict['Path'] = code_img_path_list
                                    temp_list.append(str(wn))
                                    # logger.info("Detected from DB (7 digit)-{}".format(wn))
                                    # break
                    if det != 1:
                        if len(num5list) > 0:
                            temp = max(num5list, key=num5list.count)
                            # print(temp)
                            # for n in num7_list:
                            for wn in codecolumn:

                                if str(temp) in str(wn):
                                    # print(wn)

                                    det = 1
                                    db = 7
                                    wagonid.append(wn)
                                    # out_dict['Wagon_Number'] = str(wn)
                                    # out_dict['Path'] = code_img_path_list
                                    temp_list.append(str(wn))
                                    # logger.info("Detected from DB (7 digit)-{}".format(wn))
                                    # break

                    # IF NO 11 DIGIT wagonid DETECTED SO FAR THEN CHECK FOR 5 & 6 DIGIT COMBINATION
                    if det != 1:
                        if len(num5list) > 0 and len(num6list) > 0:
                            n5 = max(num5list, key=num5list.count)
                            n6 = max(num6list, key=num6list.count)
                            if str(n5) not in str(n6):
                                n = str(n6) + str(n5)
                                if len(str(n)) == 11:

                                    for i in codecolumn:

                                        if str(n) in str(i):
                                            db = 56
                                            temp_list.append(str(n))
                                            wagonid.append(str(n))
                                            # #print("DETECTED-{}".format(n))
                                            # logger.info("Detected from DB (5+6 digit combo)-{}".format(wn))
                                            # logger.info("DETECTED-{}".format(n))
                                            # out_dict['Wagon_Number'] = str(n)
                                            # out_dict['Path'] = code_img_path_list
                                            det = 1
                                            # break

                    # CHECK IF SOMETHING MAPPED SO FAR
                    if det == 1:
                        return temp_list

                        # for i in range(0, len(temp_list)):
                        #     temp_list[i] = int(temp_list[i])
                        #
                        #
                        # for i in temp_list:
                        #     if i in codecolumn:
                        #         x.append(codecolumn.index(i))
                        # x.sort()
                        # code = x[0]
                        # return codecolumn[code]

                        # print("Mapping ir data={}".format(temp_list))
                        # logger.info("mapped ... wagonid-{} & temmmp_list-{}".format(wagonid, temp_list))
                        # with open("/home/amol/OCR/logistics/result/modular/easy_ocr/text_data/{}.txt".format(video_name[45:-4]), "a") as f:
                        #     f.write("Mapped {} digit from DB:-{}".format(db,str(temp_list)))
                        #     f.write("\n")
                        #     f.write("*" * 50)
                        #     f.write("\n")
            else:
                print("Blank OCR Result")

        else:

            if code:

                for r in code:
                    # print(r)

                    if len(str(r)) == 11:
                        num11list.append(str(r))
                        # print("DETECTED-{}".format(r))
                        # wagonid.append(int(r))
                        # det=1

                    elif len(str(r)) == 10:
                        # if str(r) not in num10_list:
                        num10_list.append(str(r))

                    elif len(str(r)) == 9:
                        # if str(r) not in num9_list:
                        num9_list.append(str(r))

                    elif len(str(r)) == 8:
                        # if str(r) not in num8_list:
                        num8_list.append(str(r))

                    elif len(str(r)) == 7:
                        # if str(r) not in num7_list:
                        num7_list.append(str(r))

                    elif len(str(r)) == 6:
                        # if str(r) not in num6list:
                        num6list.append(str(r))
                        # num56_list.append(str(r))

                    elif len(str(r)) == 5:
                        # if str(r) not in num5list:
                        num5list.append(str(r))

                        # num56_list.append(str(r))

                    elif len(str(r)) == 4:
                        num4_list.append(str(r))

                    temp_list = []
                    # print(num5list)

                    # CHECK IF ANY 11 DIGIT wagonid DETECTED...IF YES..THEN WE GOT ONE
                    if len(num11list) > 0:
                        n11 = max(num11list, key=num11list.count)
                        n11_5 = n11[-5:]
                        for i in codecolumn:
                            if str(n11_5) in str(i):
                                temp_list.append(str(i))

                                db = 11
                                # logger.info("DETECTED-{}".format(n11))
                                # logger.info("Detected from 11 digit DB")
                                wagonid.append(i)
                                # #print("DETECTED-{}".format(n11))
                                # out_dict['Wagon_Number'] = str(n11_5)
                                # out_dict['Path'] = code_img_path_list
                                det = 1

                                # break

                    # CHECK IN DB (INDIVIDUALLY FOR 7/8/9/10 DIGIT )
                    if det != 1:
                        if len(num10_list) > 0:
                            temp = max(num10_list, key=num10_list.count)
                            temp_5 = temp[-4:]
                            # for n in num10_list:
                            for wn in codecolumn:
                                if str(temp_5) in str(wn):
                                    det = 1
                                    db = 10
                                    wagonid.append(wn)
                                    # out_dict['Wagon_Number'] = str(wn)
                                    # out_dict['Path'] = code_img_path_list
                                    # logger.info("Detected from DB (10 digit)-{}".format(wn))
                                    temp_list.append(str(wn))

                                    # break
                    if det != 1:
                        if len(num9_list) > 0:
                            temp = max(num9_list, key=num9_list.count)
                            temp_5 = temp[-4:]
                            # for n in num9_list:
                            for wn in codecolumn:
                                if str(temp_5) in str(wn):
                                    det = 1
                                    db = 9
                                    wagonid.append(wn)
                                    # out_dict['Wagon_Number'] = str(wn)
                                    # out_dict['Path'] = code_img_path_list
                                    # logger.info("Detected from DB (9 digit)-{}".format(wn))
                                    temp_list.append(str(wn))

                                    # break
                    if det != 1:
                        if len(num8_list) > 0:
                            temp = max(num8_list, key=num8_list.count)
                            temp_5 = temp[-4:]
                            # for n in num8_list:
                            for wn in codecolumn:
                                if str(temp_5) in str(wn):
                                    det = 1
                                    db = 8
                                    wagonid.append(wn)
                                    # out_dict['Wagon_Number'] = str(wn)
                                    # out_dict['Path'] = code_img_path_list
                                    temp_list.append(str(wn))
                                    # logger.info("Detected from DB (8 digit)-{}".format(wn))

                                    # break

                    if det != 1:
                        if len(num7_list) > 0:
                            temp = max(num7_list, key=num7_list.count)
                            temp_5 = temp[-4:]
                            # for n in num7_list:
                            for wn in codecolumn:
                                if str(temp_5) in str(wn):
                                    det = 1
                                    db = 7
                                    wagonid.append(wn)
                                    # out_dict['Wagon_Number'] = str(wn)
                                    # out_dict['Path'] = code_img_path_list
                                    temp_list.append(str(wn))
                                    # logger.info("Detected from DB (7 digit)-{}".format(wn))
                                    # break
                    if det != 1:
                        if len(num5list) > 0:

                            temp = max(num5list, key=num5list.count)
                            temp_5 = temp[-4:]
                            # print(temp_5)
                            # for n in num7_list:
                            for wn in codecolumn:
                                if str(temp_5) in str(wn):
                                    # print(wn)
                                    det = 1
                                    db = 7
                                    wagonid.append(wn)
                                    # out_dict['Wagon_Number'] = str(wn)
                                    # out_dict['Path'] = code_img_path_list
                                    temp_list.append(str(wn))
                                    # logger.info("Detected from DB (7 digit)-{}".format(wn))
                                    # break
                                    # print(temp_list,det)

                    # IF NO 11 DIGIT wagonid DETECTED SO FAR THEN CHECK FOR 5 & 6 DIGIT COMBINATION

                    # if det != 1:
                    #     if len(num5list) > 0 and len(num6list) > 0:
                    #         n5 = max(num5list, key=num5list.count)
                    #         n6 = max(num6list, key=num6list.count)
                    #         if str(n5) not in str(n6):
                    #             n = str(n6) + str(n5)
                    #             if len(str(n)) == 11:
                    #
                    #                 for i in codecolumn:
                    #
                    #                     if str(n) in str(i):
                    #                         db = 56
                    #                         temp_list.append(str(n))
                    #                         wagonid.append(str(n))
                    #                         # #print("DETECTED-{}".format(n))
                    #                         # logger.info("Detected from DB (5+6 digit combo)-{}".format(wn))
                    #                         # logger.info("DETECTED-{}".format(n))
                    #                         # out_dict['Wagon_Number'] = str(n)
                    #                         # out_dict['Path'] = code_img_path_list
                    #                         det = 1
                    #                         # break

                    # CHECK IF SOMETHING MAPPED SO FAR
                    if det == 1:
                        return temp_list

                        # for i in range(0, len(temp_list)):
                        #     temp_list[i] = int(temp_list[i])
                        #
                        # for i in temp_list:
                        #     if i in codecolumn:
                        #         z.append(codecolumn.index(i))
                        # z.sort()
                        # code = z[0]
                        # return codecolumn[code]

                        # print("Mapping ir data={}".format(temp_list))
                        # logger.info("mapped ... wagonid-{} & temmmp_list-{}".format(wagonid, temp_list))
                        # with open("/home/amol/OCR/logistics/result/modular/easy_ocr/text_data/{}.txt".format(video_name[45:-4]), "a") as f:
                        #     f.write("Mapped {} digit from DB:-{}".format(db,str(temp_list)))
                        #     f.write("\n")
                        #     f.write("*" * 50)
                        #     f.write("\n")
            else:
                print("Blank OCR Result")

    except Exception as e:
        print("Theres an exception..-{}".format(e))

# path = ("/home/jsw/Documents/Data_Master sheet.xlsx")
# # x =
#
# x = Data_Generate(path)
# print(x)