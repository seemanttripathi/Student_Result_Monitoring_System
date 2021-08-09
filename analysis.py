import xlrd
import xlwt
import openpyxl
import xlsxwriter
import pandas as pd

def save():
    wb.save("test1.xls")


def validate_no_of_students(data):
    try:
        data[7][0] = int(data[7][0])
        if (data[7][0] + 9 == len(data)):

            return True, ''
        elif data[7][0] + 9 > len(data):
            return False, 'No of Students in (Row, Column) -> (7, 0) are ' + str(
                int(data[7][0])) + ' but less data provided'
        else:
            return False, 'No of Students in (Row, Column) -> (7, 0) are ' + str(
                int(data[7][0])) + ' but more data provided'
    except:
        return False, 'No of Students in (Row, Column) -> (7, 0) must be INTEGER'


def validate_datatype_of_marks(data):
    try:
        for row in data[9:]:
            for val in range(3, len(row)):
                if row[val] == 'AB' or row[val] == 'UFM' or row[val] == 'RI':
                    pass
                else:
                    row[val] = int(row[val])
    except:
        return False, 'Marks of R.No ' + str(int(row[1])) + ' is INVALID111'
    # print("Passed: validate_datatype_of_marks")
    return True, ''


def validate_unique_roll_number(data):
    rolls = []
    for row in data[9:]:
        rolls.append(row[1])
    if len(set(rolls)) == data[7][0]:
        # print('Passed: validate_unique_roll_number')
        return True, ''
    else:
        return False, 'Duplicate Roll Numbers Found, It must be UNIQUE'


def validate_passing_marks(data):
    try:
        for i in range(4, 9):
            data[1][i] = int(data[1][i])
        # print('Passed: validate_passing_marks')
    except:
        return False, 'Passing Marks Format in Row -> 1, Column -> (4, 5, 6, 7) is INVALID'
    return True, ''


def validate_total_marks(data):
    try:
        for row in data[9:]:
            total = 0
            for val in range(3, len(row) - 1):
                if row[val] == 'AB' or row[val] == 'UFM' or row[val] == 'RI':
                    pass
                else:
                    total += row[val]
            if total != row[-1]:
                return False, 'Incorrect Summation of Marks for R.No ' + str(row[1])
    except:
        return False, 'Marks of R.No ' + str(int(row[1])) + ' is INVALID'
    # print("Passed: validate_total_marks")
    return True, ''


def validate_marks_of_each_subject(data):
    try:
        for i in range(3, len(data[8])):
            data[8][i] = int(data[8][i])
    except:
        return False, 'Marks for each Subjects between (R, C) -> (D9 to X9) in INVALID'

    for row in data[9:]:
        for val in range(3, len(row)):
            if row[val] != 'AB' and row[val] != 'UFM' and row[val] != 'RI':
                if row[val] > data[8][val]:
                    return False, 'More Marks than expected in R.No ' + str(int(row[1]))
    # print("Passed: validate_marks_of_each_subject")
    return True, ''


def validate_input_sheet(df):
    valid, report = validate_no_of_students(df)
    if not valid:
        # print(report)
        return False, report

    valid, report = validate_datatype_of_marks(df)
    if not valid:
        # print(report)
        return False, report

    valid, report = validate_unique_roll_number(df)
    if not valid:
        # print(report)
        return False, report

    valid, report = validate_passing_marks(df)
    if not valid:
        # print(report)
        return False, report

    valid, report = validate_total_marks(df)
    if not valid:
        # print(report)
        return False, report

    valid, report = validate_marks_of_each_subject(df)
    if not valid:
        # print(report)
        return False, report

    # print("Done-validation")
    return True, ''


def setup_values():
    line1 = [['Year', 'Subject Code', 'Subject Name', 'Section', 'Total Students', 'Result Incomplete',
              'No. of Detained Students-D', 'No. of Absent Students-AB', 'No. of UFM Students',
              'No. of Students Appeared']]
    return line1


def analysing_results(data):
    store = []
    ri_, d_, ab_, ufm_, appeared_ = [], [], [], [], []
    for j in range(3, len(data[3]) - 1):
        ri, d, ab, ufm, appeared = 0, 0, 0, 0, 0
        for i in range(9, len(data)):
            if data[i][j] == 'RI':
                ri += 1
            elif data[i][j] == 'D':
                d += 1
            elif data[i][j] == 'AB':
                ab += 1
            elif data[i][j] == 'UFM':
                ufm += 1
            if data[i][j] != 'AB' and data[i][j] != 'D':
                appeared += 1

        ri_.append(ri)
        d_.append(d)
        ab_.append(ab)
        ufm_.append(ufm)
        appeared_.append(appeared)
    ri_.append(0)
    d_.append(0)
    ab_.append(0)
    ufm_.append(0)
    appeared_.append(0)
    for i in range(9, len(data)):
        if 'RI' in data[i]:
            ri_[-1] += 1
        if 'D' in data[i]:
            d_[-1] += 1
        if 'AB' in data[i]:
            ab_[-1] += 1
        if 'UFM' in data[i]:
            ufm_[-1] += 1
    return True, [ri_, d_, ab_, ufm_, appeared_]


def analysing_pass_fail(data):
    fail_ = []
    student_count = data[7][0]
    for j in range(3, len(data[3]) - 1):
        count = 0
        per30 = (data[8][j] * 30) / 100
        for i in range(9, len(data)):
            if data[i][j] not in ['RI', 'D', 'UFM', 'AB'] and data[i][j] < per30:
                count += 1
        fail_.append(count)
    pass_ = [student_count - item for item in fail_]
    pass_percentage = [float("{0:.2f}".format(item / student_count)) * 100 for item in pass_]

    return True, [pass_, fail_, pass_percentage]


def pointing_marks(data):
    max_, min_, avg_ = [], [], []
    student_count = data[7][0]
    for j in range(3, len(data[3])):
        max1, min2, avg3 = 0, 1000, 0
        for i in range(9, len(data)):
            if data[i][j] not in ['RI', 'D', 'UFM', 'AB']:
                max1 = max(max1, data[i][j])
                min2 = min(min2, data[i][j])
                avg3 += data[i][j]
        max_.append(max1)
        min_.append(min2)
        avg_.append(float("{0:.1f}".format(avg3 / student_count)))

    return True, [max_, min_, avg_]


def percentage_classification(data):
    above_equal_80_, between_80_60_, between_60_40_, between_40_30_, below_30_ = [], [], [], [], []
    for j in range(3, len(data[3])):
        above_equal_80, between_80_60, between_60_40, between_40_30, below_30 = 0, 0, 0, 0, 0
        per80 = (data[8][j] * 80) / 100
        per60 = (data[8][j] * 60) / 100
        per40 = (data[8][j] * 40) / 100
        per30 = (data[8][j] * 30) / 100
        for i in range(9, len(data)):
            if data[i][j] not in ['AB', 'D', 'UFM', 'RI']:
                if data[i][j] >= per80:
                    above_equal_80 += 1
                elif data[i][j] < per80 and data[i][j] >= per60:
                    between_80_60 += 1
                elif data[i][j] < per60 and data[i][j] >= per40:
                    between_60_40 += 1
                elif data[i][j] < per40 and data[i][j] >= per30:
                    between_40_30 += 1
                else:
                    below_30 += 1
        above_equal_80_.append(above_equal_80)
        between_80_60_.append(between_80_60)
        between_60_40_.append(between_60_40)
        between_40_30_.append(between_40_30)
        below_30_.append(below_30)

    return True, [above_equal_80_, between_80_60_, between_60_40_, between_40_30_, below_30_]

# analysis(data_a)


workbook_chart = xlsxwriter.Workbook("test-Charts.xlsx")


def piechart(name, headings, data):
    #     workbook = creating_charts()

    worksheet_chart = workbook_chart.add_worksheet('pie-charts' + name)
    bold = workbook_chart.add_format({'bold': 1})
    worksheet_chart.write_row('A1', headings, bold)
    worksheet_chart.write_column('A2', data[0])
    worksheet_chart.write_column('B2', data[1])

    chart1 = workbook_chart.add_chart({'type': 'pie'})

    chart1.add_series({
        'name': 'Pie Sales Data',
        'categories': ['pie-charts' + name, 1, 0, 3, 0],
        'values': ['pie-charts' + name, 1, 1, 3, 1], })

    chart1.set_title({'name': name})
    chart1.set_style(10)
    worksheet_chart.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})


def section_wise(noOfSheets):
    ws = wb.add_sheet('SECTION WISE')

    complete_data = []
    for i in range(noOfSheets):
        sheet = workbook.sheet_by_index(i)
        data_a = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(0, sheet.nrows)]
        complete_data.append(data_a)

    sheet = workbook.sheet_by_index(0)
    data_a = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(0, sheet.nrows)]
    no_of_subj = int(data_a[2][0])
    list_of_subject_codes = []
    for i in range(no_of_subj):
        list_of_subject_codes.append(data_a[2][i + 1])
    # print(no_of_subj, list_of_subject_codes)

    indices_codes = []
    for item in list_of_subject_codes:
        l = []
        for j in range(3, len(data_a[6])):
            if data_a[6][j] == item:
                l.append(j)
        indices_codes.append(l)

    section_wise = []
    #     print(noOfSheets, complete_data)
    for k in range(noOfSheets):
        branch = complete_data[k][0][1]
        section = complete_data[k][1][2]
        year = complete_data[k][1][1]
        l = [branch, year, section, int(complete_data[k][7][0])]
        ri = 0
        for i in range(9, len(complete_data[k])):
            for j in range(3, len(complete_data[k][i])):
                if complete_data[k][i][j] == 'RI':
                    ri += 1
                    break
        l.append(l[-1] - ri)
        cp1, cp2, cp3, cp3g = 0, 0, 0, 0
        for i in range(9, len(complete_data[k])):
            cp = 0
            for j in range(len(indices_codes)):
                if complete_data[k][i][indices_codes[j][0]] not in ['RI', 'AB', 'D', 'UFM'] and complete_data[k][i][
                    indices_codes[j][1]] not in ['RI', 'AB', 'D', 'UFM'] and complete_data[k][i][indices_codes[j][0]] + \
                        complete_data[k][i][indices_codes[j][1]] < complete_data[k][1][4]:
                    cp += 1
            if cp == 1:
                cp1 += 1
            elif cp == 2:
                cp2 += 1
            elif cp == 3:
                cp3 += 1
            elif cp == 0:
                pass
            else:
                cp3g += 1
        cp = cp1 + cp2 + cp3 + cp3g
        l.append(l[-1] - cp)
        l.append(ri);
        l.append(cp1);
        l.append(cp2);
        l.append(cp3);
        l.append(cp3g);
        l.append(cp);
        l.append(round((l[5] / l[4]) * 100, 2))
        section_wise.append(l)
    ll = ['', '', 'Total', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(section_wise)):
        for j in range(3, len(section_wise[i])):
            ll[j] += section_wise[i][j]
    ll[-1] = round(ll[-1] / 2, 2)
    section_wise.append(ll)

    ###################################  PIE-CHART ########################################
    for i in range(len(section_wise) - 1):
        name = section_wise[i][2]
        headings = ['Category', 'Values']
        data = [['Pass', 'Result Incomplete', 'Total CP'],
                [section_wise[i][5], section_wise[i][6], section_wise[i][-2]], ]
        # print(name, data)
        piechart(name, headings, data)
    ###################################  PIE-CHART ########################################

    prepare_subj_sheet = [[complete_data[0][0][0]], [complete_data[0][0][1]], ['SECTION WISE  RESULT ANALYSIS'],
                          ['Branch', 'Year', 'Section', 'No. of Students Appeared',
                           'No. of students with declared result', 'No. of Pass Students', 'Result Incomplete', 'CP(1)',
                           'CP(2)', 'CP(3)', 'CP(>3)', 'Total CP Students', 'Pass %', 'Remark']]
    for i in range(len(prepare_subj_sheet)):
        for j in range(len(prepare_subj_sheet[i])):
            ws.write(i, j, prepare_subj_sheet[i][j])
    for i in range(len(section_wise)):
        for j in range(len(section_wise[i])):
            ws.write(i + 4, j, section_wise[i][j])

    # print(section_wise)


def bargraph(headings, data):
    worksheet_chart = workbook_chart.add_worksheet('bar-graphs')
    bold = workbook_chart.add_format({'bold': 1})
    s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    worksheet_chart.write_row('A1', headings, bold)
    for i in range(len(headings)):
        worksheet_chart.write_column(s[i] + '2', data[i])

    chart1 = workbook_chart.add_chart({'type': 'column'})
    for i in range(1, len(headings)):
        chart1.add_series({
            'name': ['bar-graphs', 0, i],
            'categories': ['bar-graphs', 1, 0, 6, 0],
            'values': ['bar-graphs', 1, i, 6, i], })

    chart1.set_title({'name': 'Subject Wise Comparision'})
    chart1.set_x_axis({'name': 'Sections'})
    chart1.set_y_axis({'name': 'Data length (mm)'})

    chart1.set_style(11)
    worksheet_chart.insert_chart('G2', chart1)
    workbook_chart.close()

def subject_wise(complete_data):
    ws = wb.add_sheet('SUBJ WISE')

    sheet = workbook.sheet_by_index(0)
    data_a=[[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(0,sheet.nrows)]
    no_of_subj = int(data_a[2][0])
    list_of_subject_codes = []
    for i in range(no_of_subj):
        list_of_subject_codes.append(data_a[2][i+1])
    # print(no_of_subj, list_of_subject_codes)

    indices_codes = []
    for item in list_of_subject_codes:
        l = []
        for j in range(3, len(data_a[6])):
            if data_a[6][j]==item:
                l.append(j)
        indices_codes.append(l)
    # print(indices_codes)
    subj_wise_list = []
    dic = {}

    for k in range(no_of_subj):
        for j in range(len(complete_data)):
            ri, d, ab, ufm, fail, high, low, add, eig, six, forty, thirty, below30 = 0, 0, 0, 0, 0, 0, 1000, 0, 0, 0, 0, 0, 0
            for i in range(9, len(complete_data[j])):
                if complete_data[j][i][indices_codes[k][0]]=='RI' or complete_data[j][i][indices_codes[k][1]]=='RI':
                    ri += 1
                elif complete_data[j][i][indices_codes[k][0]]=='AB' or complete_data[j][i][indices_codes[k][1]]=='AB':
                    ab += 1
                elif complete_data[j][i][indices_codes[k][0]]=='D' or complete_data[j][i][indices_codes[k][1]]=='D':
                    d += 1
                elif complete_data[j][i][indices_codes[k][0]]=='UFM' or complete_data[j][i][indices_codes[k][1]]=='UFM':
                    ufm += 1
                else:
                    add += complete_data[j][i][indices_codes[k][1]]
                    if complete_data[j][i][indices_codes[k][0]] + complete_data[j][i][indices_codes[k][1]] < complete_data[j][1][4]:
                        fail += 1
                    if complete_data[j][i][indices_codes[k][1]] > high:
                        high = complete_data[j][i][indices_codes[k][1]]
                    if complete_data[j][i][indices_codes[k][1]] < low:
                        low = complete_data[j][i][indices_codes[k][1]]
                    if complete_data[j][i][indices_codes[k][1]] >= (complete_data[j][8][indices_codes[k][1]]*(80/100)):
                        eig += 1
                    elif complete_data[j][i][indices_codes[k][1]] >= (complete_data[j][8][indices_codes[k][1]]*(60/100)):
                        six += 1
                    elif complete_data[j][i][indices_codes[k][1]] >= (complete_data[j][8][indices_codes[k][1]]*(40/100)):
                        forty += 1
                    elif complete_data[j][i][indices_codes[k][1]] >= (complete_data[j][8][indices_codes[k][1]]*(30/100)):
                        thirty += 1
                    else:
                        below30 += 1

            subj_wise_list.append([complete_data[j][1][1], list_of_subject_codes[k], complete_data[j][1][2],
                                   int(complete_data[j][7][0]), ri, d, ab, ufm, int(complete_data[j][7][0]),
                                   int(complete_data[j][7][0]-fail),
                                   fail, round((100/complete_data[j][7][0])*(complete_data[j][7][0]-fail), 2),
                                   int(high), int(low), round(add/complete_data[j][7][0], 2), eig, six,
                                   forty, thirty, below30])
            if complete_data[j][1][2] not in dic.keys():
                dic[complete_data[j][1][2]] = [round((100/complete_data[j][7][0])*(complete_data[j][7][0]-fail), 2)]
            else:
                dic[complete_data[j][1][2]].append(round((100/complete_data[j][7][0])*(complete_data[j][7][0]-fail), 2))
        ll = ['', '', 'Total']
        newll = [[], []]
        for m in range(3, len(subj_wise_list[0])):
            val = 0
            for j in range(-1, -(len(complete_data)+1), -1):
                val += subj_wise_list[j][m]
                if m==12:
                    newll[0].append(subj_wise_list[j][m])
                elif m==13:
                    newll[1].append(subj_wise_list[j][m])
            ll.append(val)
        ll[11] = round(ll[11]/2, 2)
        ll[14] = round(ll[14]/2, 2)
        ll[12] = max(newll[0])
        ll[13] = min(newll[1])
        subj_wise_list.append(ll)

    # print(subj_wise_list)

    ###################################  BAR-GRAPH ########################################
    headings = ['Subject Code']
    for k in range(len(complete_data)):
        section = complete_data[k][1][2]
        headings.append(section)
    data = [list_of_subject_codes]
    for i in dic.keys():
        data.append(dic[i])
    bargraph(headings, data)
    ###################################  BAR-GRAPH ########################################


    prepare_subj_sheet = [[complete_data[0][0][0]], [complete_data[0][0][1]], ['SUBJECT WISE  RESULT ANALYSIS'],
                         ['Year', 'Subject Code', 'Section', 'Total Students', 'Result Incomplete', 'No. of Detained Students-D', 'No. of Absent Students-AB', 'No. of UFM Students', 'No. of Students Appeared', 'No. of Pass Students', 'No. of Fail Students(less than 30%)', 'Clear Pass %age', 'Highest Marks(in each subject)', 'Lowest Marks(in each subject)', 'Average Marks (in each subject)', 'No. of students marks secured (above 80%)', 'No. of students marks secured (between 60% - 80%)', 'No. of students marks secured (between 40% - 60%)', 'No. of students marks secured (between 30% - 40%)', 'No. of students marks secured (below 30%)']]
    for i in range(len(prepare_subj_sheet)):
        for j in range(len(prepare_subj_sheet[i])):
            ws.write(i, j, prepare_subj_sheet[i][j])
    for i in range(len(subj_wise_list)):
        for j in range(len(subj_wise_list[i])):
            ws.write(i+4, j, subj_wise_list[i][j])


def gaia(complete_data):
    ws = wb.add_sheet('GAIA')

    sheet = workbook.sheet_by_index(0)
    data_a=[[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(0,sheet.nrows)]
    no_of_subj = int(data_a[2][0])
    list_of_subject_codes = []
    for i in range(no_of_subj):
        list_of_subject_codes.append(data_a[2][i+1])
    # print(no_of_subj, list_of_subject_codes)

    indices_codes = []
    for item in list_of_subject_codes:
        l = []
        for j in range(3, len(data_a[6])):
            if data_a[6][j]==item:
                l.append(j)
        indices_codes.append(l)
    # print(indices_codes)
    gaia_list = [[complete_data[0][1][1], i+1, list_of_subject_codes[i], 0, 0] for i in range(len(indices_codes))]

    for k in range(len(complete_data)):
        for i in range(9, len(complete_data[k])):
            for j in range(len(indices_codes)):
                if complete_data[k][i][indices_codes[j][1]] not in ['RI', 'AB', 'D', 'UFM']:
                    gaia_list[j][-2]+=1
                    gaia_list[j][-1]+=int(complete_data[k][i][indices_codes[j][1]])
    for i in range(len(indices_codes)):
        gaia_list[i].append(round(gaia_list[i][-1]/gaia_list[i][-2], 2))
    ll = ['', '', 'Total', 0, 0, 0]
    for item in gaia_list:
        ll[-1] += item[-1]
        ll[-2] += item[-2]
        ll[-3] += item[-3]
    ll[-1] = round(ll[-1]/len(gaia_list), 2)
    gaia_list.append(ll)

    # print(gaia_list)

    prepare_subj_sheet = [[complete_data[0][0][0]], [complete_data[0][0][1]], ['GRAND AVERAGE SUBJECT WISE'],
                         ['Year', 'S.No.', 'Subject Code', 'No of Students', 'Total Marks', 'Avg marks pre subject']]
    for i in range(len(prepare_subj_sheet)):
        for j in range(len(prepare_subj_sheet[i])):
            ws.write(i, j, prepare_subj_sheet[i][j])
    for i in range(len(gaia_list)):
        for j in range(len(gaia_list[i])):
            ws.write(i+4, j, gaia_list[i][j])

def toppers_list(complete_data):
    ws = wb.add_sheet('Toppers-Branch Wise')

    branch_toppers_list = []
    highest = []
    for k in range(len(complete_data)):
        for i in range(9, len(complete_data[k])):
            highest.append(complete_data[k][i][-1])
    highest.sort(reverse = True)
    third = highest[2]
    for k in range(len(complete_data)):
        for i in range(9, len(complete_data[k])):
            if complete_data[k][i][-1] >= third:
                branch_toppers_list.append([int(complete_data[k][i][-1]), int(complete_data[k][8][-1]), complete_data[k][i][2], int(complete_data[k][i][1])])
    branch_toppers_list.sort(reverse = True)
    for i in range(len(branch_toppers_list)):
        branch_toppers_list[i][:] = branch_toppers_list[i][::-1]
        branch_toppers_list[i].append(round(branch_toppers_list[i][-1]*100/branch_toppers_list[i][-2], 2))
    branch = complete_data[0][0][1]
    year = complete_data[0][1][1]
    for i in range(len(branch_toppers_list)):
        branch_toppers_list[i] = [year, branch, i+1]+branch_toppers_list[i]

    # print(branch_toppers_list)

    prepare_subj_sheet = [[complete_data[0][0][0]], [complete_data[0][0][1]], ['Toppers List'],
                         ['Year', 'Branch', 'S.No.', 'Roll Number', 'Student Name', 'Max Marks', 'Marks Obtained', 'Percentage']]
    for i in range(len(prepare_subj_sheet)):
        for j in range(len(prepare_subj_sheet[i])):
            ws.write(i, j, prepare_subj_sheet[i][j])
    for i in range(len(branch_toppers_list)):
        for j in range(len(branch_toppers_list[i])):
            ws.write(i+4, j, branch_toppers_list[i][j])


def analysis(df):
    valid, report = validate_input_sheet(df)       # Validating Input_Sheet
    if not valid:
        return False, report

    name = df[1][2]
    ws = wb.add_sheet(name)
    ws_i, ws_j = 0, 0
    for i in range(6, len(df)):
        for j in range(len(df[i])):
            if i == 7 and j == 0:
                pass
            else:
                ws.write(ws_i, ws_j, df[i][j])
            ws_j += 1
        ws_i += 1
        ws_j = 0

    ls = ['Total Students', 'Result Incomplete', 'No. of Detained Students-D', 'No. of Absent Students-AB',
          'No. of UFM Students', 'No. of Students Appeared', 'No. of Pass Students',
          'No. of Fail Students(less than 30%)', 'Clear Pass %age', 'Highest Marks(in each subject)',
          'Lowest Marks(in each subject)', 'Average Marks (in each subject)',
          'No. of students marks secured (above 80%)', 'No. of students marks secured (between 60% - 80%)',
          'No. of students marks secured (between 40% - 60%)', 'No. of students marks secured (between 30% - 40%)',
          'No. of students marks secured (below 30%)']
    temp_i = ws_i
    for item in ls:
        ws.write(temp_i, 2, item)
        temp_i += 1

    report, resultant_value = analysing_results(df)  # RI, D, AB, UFM, Appeared

    if not report:
        return False, 'Failed at analysing_results'

    ws_j = 3
    student_count = df[7][0]
    for i in range(len(resultant_value[1])):
        ws.write(ws_i, ws_j, student_count)
        ws_j += 1

    ws_i += 1
    ws_j = 3
    for i in range(len(resultant_value)):
        for j in range(len(resultant_value[i])):
            ws.write(ws_i, ws_j, resultant_value[i][j])
            ws_j += 1
        ws_i += 1
        ws_j = 3

    report, resultant_value2 = analysing_pass_fail(df)  # Pass, Failed(<30%), Clear Pass %
    if not report:
        return False, 'Failed at analysing_pass_fail'

    for i in range(len(resultant_value2)):
        for j in range(len(resultant_value2[i])):
            ws.write(ws_i, ws_j, resultant_value2[i][j])
            ws_j += 1
        ws_i += 1
        ws_j = 3

    report, resultant_value3 = pointing_marks(df)  # Highest Marks, Lowest Marks, Average Marks
    if not report:
        return False, 'Failed at pointing_marks'

    for i in range(len(resultant_value3)):
        for j in range(len(resultant_value3[i])):
            ws.write(ws_i, ws_j, resultant_value3[i][j])
            ws_j += 1
        ws_i += 1
        ws_j = 3

    report, resultant_value4 = percentage_classification(
        df)  # (>=80%), (>=60% and <80%), (>=40% and <60%), (>=30% and <40%), (<30%)
    if not report:
        return False, 'Failed at percentage_classification'

    for i in range(len(resultant_value4)):
        for j in range(len(resultant_value4[i])):
            ws.write(ws_i, ws_j, resultant_value4[i][j])
            ws_j += 1
        ws_i += 1
        ws_j = 3

    # print("Section Page-Done")
    return True, ''


wb = xlwt.Workbook()


def analysis1(file_location):
    global workbook
    workbook = xlrd.open_workbook(file_location, on_demand=True)
    xl = pd.ExcelFile(file_location)
    noOfSheets = len(xl.sheet_names)
    # print(noOfSheets)
    complete_data = []
    for i in range(noOfSheets):
        sheet = workbook.sheet_by_index(i)
        data_a = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(0, sheet.nrows)]
        complete_data.append(data_a)

        valid, report = analysis(data_a)
        if not valid:
            return False, report
    section_wise(noOfSheets)
    subject_wise(complete_data)
    gaia(complete_data)
    toppers_list(complete_data)
    print("analysis-Done")
    save()
    return True, 'Analysis Completed Successfully!!'

# analysis1(file_location)