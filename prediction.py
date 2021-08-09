import pandas as pd
import numpy as np
import math
from sklearn import linear_model
import xlrd
import xlwt

wb = xlwt.Workbook()

def predict_percentage(file_location):
    try:
        workbook = xlrd.open_workbook(file_location, on_demand=True)
        sheet = workbook.sheet_by_index(1)
        data_train = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(0, sheet.nrows)]

        a = [[], [], [], [], [], []]
        for i in range(1, len(data_train)):
            for j in range(len(data_train[i])):
                a[j].append(data_train[i][j])
        a = np.array(a)

        df = pd.DataFrame(
            {'Sem1Percent': a[0], 'Sem2Percent': a[1], 'PUT': a[2], 'Attendence': a[3], 'CP': a[4], 'OutcomePercent': a[5]})

        sheet = workbook.sheet_by_index(0)
        data_test = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(0, sheet.nrows)]

        b = [[], [], [], [], [], []]
        for i in range(9, len(data_test)):
            b[0].append(int(data_test[i][1]))
            b[1].append(int(data_test[i][-4]))
            b[2].append(int(data_test[i][-3]))
            p = int(data_test[2][0])
            val = 0
            for j in range(3 + p * 2, 3 + p * 3):
                if data_test[i][j] in ['AB', 'D']:
                    continue
                val += int(data_test[i][j])
            val /= p
            b[3].append(round(val, 1))
            b[4].append(data_test[i][-5])
            b[5].append(data_test[i][-1] + data_test[i][-2])

        dfPredict = pd.DataFrame(
            {'RNo': b[0], 'Sem1Percent': b[1], 'Sem2Percent': b[2], 'PUT': b[3], 'Attendence': b[4], 'CP': b[5]})

        df.Sem1Percent = df.Sem1Percent.fillna(math.floor(df.Sem1Percent.median()))
        df.Sem2Percent = df.Sem2Percent.fillna(math.floor(df.Sem2Percent.median()))
        df.PUT = df.PUT.fillna(math.floor(df.PUT.median()))
        df.Attendence = df.Attendence.fillna(math.floor(df.Attendence.median()))
        df.CP = df.CP.fillna(math.floor(df.CP.median()))
        df.OutcomePercent = df.OutcomePercent.fillna(math.floor(df.OutcomePercent.median()))

        reg = linear_model.LinearRegression()
        reg.fit(df[['Sem1Percent', 'Sem2Percent', 'PUT', 'Attendence', 'CP']], df.OutcomePercent)
        # print(reg.coef_, reg.intercept_)

        y_p = reg.predict(dfPredict[['Sem1Percent', 'Sem2Percent', 'PUT', 'Attendence', 'CP']])

        op = pd.DataFrame({'R.No': dfPredict.RNo, 'Predicted': y_p})

        ws = wb.add_sheet('percentage prediction')

        ws.write(0, 0, 'R.No.')
        ws.write(0, 1, 'Predicted Percentage')
        for i in range(len(y_p)):
            ws.write(i + 1, 0, int(dfPredict.RNo[i]))
            ws.write(i + 1, 1, round(y_p[i], 1))
        wb.save("testPrediction.xls")
        return True, ''
    except:
        return False, 'Error in predict_percentage'


def conditional_prediction(file_location):
    try:
        workbook = xlrd.open_workbook(file_location, on_demand=True)
        sheet = workbook.sheet_by_index(0)
        data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(0, sheet.nrows)]

        credit = {}
        noOfSub = int(data[2][0])
        noOfSem = int(data[3][0])
        for i in range(9, len(data)):
            rno = int(data[i][1])
            credit[rno] = 0
            for j in range(3, len(data[i])):
                if data[i][j] in ['AB', 'D']:
                    continue
                elif j < 3 + 2 * noOfSub:
                    credit[rno] += data[i][j] / data[8][j]
                elif j < 4 + 3 * noOfSub + noOfSem:
                    credit[rno] += 2 * (data[i][j] / data[8][j])
                else:
                    credit[rno] -= data[i][j] * 10
            credit[rno] = round(credit[rno], 1)

        ws = wb.add_sheet('remidial')
        ws.write(0, 0, 'R.No.')
        ws.write(0, 1, 'Credit Scores')
        i = 1
        for item in credit.keys():
            ws.write(i, 0, item)
            ws.write(i, 1, credit[item])
            i += 1
        #     wb.save("testPrediction.xls")
        ########################  predict_percentage  ###########################
        predict_percentage(file_location)
        ########################  predict_percentage  ###########################

        return True, ''
    except:
        return False, 'Error in predict_percentage'


def prediction_call(file_location):
    resp = conditional_prediction(file_location)
    if resp[0]==True:
        print('prediction-Done')
        return True, 'Prediction Completed Successfully!!'
    else:
        return False, resp[1]
