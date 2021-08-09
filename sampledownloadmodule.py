#code
import xlwt

def for_prediction():
   test_data = [['College', 'Branch', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                 '', '', '', '', '', '', ''],
                ['Course', 'Year', 'Section', 'Session', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                 '', '', '', '', '', '', ''],
                ['No. of Theory Subjects Internal', 'Subject Code', 'Subject Code', 'Subject Code', 'Subject Code',
                 'Subject Code',
                 'Subject Code', 'Subject Code', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                 ''],
                ['2(No. of Semester result)(fixed)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                 '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                                                   '', '', '', '', '', '', '', '', '', ''],
                ['', '', '', 'Sessional 1', '', '', '', '', '', 'Sessional 2',
                 '', '', '', '', '', 'PUT', '', '', '', '', '', 'Attendence', 'Sem 3 %', 'Sem 4 %', 'Sem 1 CP',
                 'Sem 2 CP'],
                ['', '', '', 'RAS 401', 'RVE 401', 'REC 406', 'RCS 401', 'RCS 402', 'RCS 403', 'RAS 401', 'RVE 401',
                 'REC 406',
                 'RCS 401', 'RCS 402', 'RCS 403', 'RAS 401', 'RVE 401', 'REC 406', 'RCS 401', 'RCS 402', 'RCS 403', '',
                 '',
                 '', '', ''],
                ['4(No of Students)', '', '', 19.0, 19.0, 19.0, 19.0, 19.0, 19.0, 19.0, 19.0, 19.0, 19.0, 19.0, 19.0,
                 21.0,
                 21.0, 21.0, 21.0, 21.0, 21.0, 65.0, '', '', '', ''],
                ['S.No', 'R.No', 'S.Name', 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 70.0,
                 70.0, 70.0, 70.0, 70.0, 70.0, 100.0, 100.0, 100.0, '', ''],
                [1.0, 1701.0, 'AAA', 30.0, 30.0, 30.0, 30.0,
                 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 85.0, 78.0, 80.0,
                 0.0, 0.0], [2.0, 1702.0, 'BBB', 19.0, 23.0, 19.0, 19.0, 19.0, 20.0, 19.0, 23.0, 19.0, 19.0, 19.0, 20.0,
                             31.0, 42.0, 21.0, 38.0, 34.0, 40.0, 80.0, 67.0, 65.0, 0.0, 0.0],
                [3.0, 1703.0, 'CCC', 19.0, 17.0, 19.0,
                 19.0, 19.0, 19.0, 19.0, 17.0, 19.0, 19.0, 19.0, 19.0, 32.0, 26.0, 41.0, 29.0, 22.0, 36.0, 85.0, 48.0,
                 60.0, 4.0, 0.0], [4.0, 1704.0, 'DDD', 19.0, 19.0, 19.0, 19.0, 19.0, 19.0, 19.0, 19.0, 19.0, 19.0, 19.0,
                                   19.0, 24.0, 21.0, 7.0, 25.0, 25.0, 22.0, 85.0, 55.0, 54.0, 1.0, 1.0]]

   train_data = [['Sem1Percent', 'Sem2Percent', 'PUT', 'Attendence', 'CP', 'OutcomePercent'],
                 [78.0, 80.0, 71.0, 80.0, 0.0, 83.0], [67.0, 65.0, 60.0, 80.0, 0.0, 65.0],
                 [48.0, 60.0, 51.0, 80.0, 6.0, 60.0],
                 [55.0, 54.0, 51.0, 80.0, 4.0, 59.0], [69.0, 72.0, 63.0, 80.0, 0.0, 70.0],
                 [57.0, 61.0, 62.0, 80.0, 1.0, 65.0],
                 [80.0, 79.0, 75.0, 80.0, 0.0, 78.0], [79.0, 77.0, 74.0, 80.0, 0.0, 78.0],
                 [66.0, 70.0, 69.0, 80.0, 0.0, 73.0],
                 [70.0, 69.0, 71.0, 80.0, 0.0, 75.0], [60.0, 66.0, 61.0, 80.0, 1.0, 66.0],
                 [55.0, 56.0, 52.0, 80.0, 4.0, 59.0],
                 [78.0, 74.0, 75.0, 80.0, 0.0, 78.0], [70.0, 68.0, 65.0, 80.0, 0.0, 71.0],
                 [66.0, 67.0, 69.0, 80.0, 0.0, 71.0],
                 [65.0, 63.0, 59.0, 80.0, 0.0, 67.0], [63.0, 63.0, 60.0, 80.0, 0.0, 63.0],
                 [70.0, 63.0, 59.0, 80.0, 1.0, 64.0],
                 [67.0, 67.0, 63.0, 80.0, 0.0, 71.0], [79.0, 73.0, 67.0, 80.0, 0.0, 78.0],
                 [82.0, 83.0, 80.0, 80.0, 0.0, 84.0],
                 [87.0, 88.0, 82.0, 80.0, 0.0, 89.0], [63.0, 68.0, 67.0, 80.0, 0.0, 69.0],
                 [67.0, 72.0, 68.0, 80.0, 1.0, 72.0],
                 [79.0, 81.0, 78.0, 80.0, 0.0, 85.0], [78.0, 75.0, 78.0, 80.0, 0.0, 78.0],
                 [70.0, 67.0, 62.0, 80.0, 0.0, 70.0],
                 [64.0, 66.0, 56.0, 80.0, 0.0, 60.0], [80.0, 69.0, 72.0, 80.0, 0.0, 79.0],
                 [79.0, 78.0, 77.0, 80.0, 0.0, 73.0],
                 [65.0, 67.0, 66.0, 80.0, 1.0, 67.0], [64.0, 65.0, 61.0, 80.0, 0.0, 71.0],
                 [75.0, 82.0, 77.0, 80.0, 0.0, 82.0],
                 [71.0, 78.0, 70.0, 80.0, 0.0, 74.0], [75.0, 82.0, 76.0, 80.0, 0.0, 76.0],
                 [73.0, 80.0, 77.0, 80.0, 0.0, 79.0],
                 [65.0, 71.0, 71.0, 80.0, 1.0, 75.0], [72.0, 78.0, 71.0, 80.0, 0.0, 76.0],
                 [72.0, 79.0, 67.0, 80.0, 0.0, 71.0],
                 [77.0, 76.0, 72.0, 80.0, 0.0, 69.0], [62.0, 64.0, 62.0, 80.0, 1.0, 64.0],
                 [57.0, 61.0, 60.0, 80.0, 3.0, 63.0],
                 [67.0, 67.0, 63.0, 80.0, 0.0, 71.0]]

   wb = xlwt.Workbook()
   ws = wb.add_sheet('test data')
   for i in range(len(test_data)):
      for j in range(len(test_data[i])):
         ws.write(i, j, test_data[i][j])
   ws = wb.add_sheet('train data')
   for i in range(len(train_data)):
      for j in range(len(train_data[i])):
         ws.write(i, j, train_data[i][j])
   wb.save("SampleForPrediction.xls")


def for_analysis():
   sec_a = [['IPEC', 'IT', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            ['B.Tech', 2.0, 'Section', 'Session', 40.0, 0.0, 21.0, 20.0, 20.0, '', '', '', '', '', '', '', '', '',
             '', '', '', '', '', ''],
            [6.0, 'RAS 101', 'RAS 202', 'RAS 303', 'RAS 404', 'RAS 505', 'RAS 606', '', '', '', '', '', '', '', '', '',
             '', '', '', '', '', '', '', ''],
            [3.0, 'PAS 101', 'PAS 202', 'PAS 303', 'PAS 404', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
             '', '', '', '', ''],
            [6.0, 'RAS 101', 'RAS 202', 'RAS 303', 'RAS 404', 'RAS 505', 'RAS 606', '', '', '', '', '', '', '', '', '',
             '', '', '', '', '', '', '', ''],
            [3.0, 'PAS 101', 'PAS 202', 'PAS 303', 'PAS 404', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
             '', '', '', '', ''],
            ['', '', '',
             'RAS 101', 'RAS 202', 'RAS 303', 'RAS 404', 'RAS 505', 'RAS 606', 'PAS 101', 'PAS 202', 'PAS 303',
             'PAS 404',
             'RAS 101', 'RAS 202', 'RAS 303', 'RAS 404', 'RAS 505', 'RAS 606', 'PAS 101', 'PAS 202', 'PAS 303',
             'PAS 404',
             ''],
            [6.0, '', '', 'Sub 1', 'Sub 2', 'Sub 3', 'Sub 4', 'Sub 5', 'Sub 6', 'Practical 1', 'Practical 2',
             'Practical 3',
             'Practical 4', 'Sub 1', 'Sub 2', 'Sub 3', 'Sub 4', 'Sub 5', 'Sub 6', 'Practical 1', 'Practical 2',
             'Practical 3',
             'Practical 4', 'Total'],
            ['S.No', 'R.No', 'S.Name', 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 50.0, 50.0, 50.0, 50.0, 70.0, 70.0, 70.0,
             70.0, 70.0, 70.0, 50.0, 50.0, 50.0, 50.0, 1000.0],
            [1.0, 1701.0, 'AAA', 29.0, 30.0, 30.0, 30.0, 28.0, 26.0, 49.0, 46.0, 48.0, 46.0, 44.0, 44.0, 48.0, 56.0,
             42.0, 48.0, 46.0, 46.0, 45.0, 44.0, 825.0],
            [2.0, 1702.0, 'BBB', 19.0, 22.0, 21.0, 'RI', 'RI', 30.0, 45.0, 42.0, 37.0, 45.0, 31.0, 19.0, 21.0, 38.0,
             44.0, 40.0, 40.0, 37.0, 42.0, 44.0, 691.0],
            [3.0, 1703.0, 'CCC', 25.0, 26.0, 23.0, 'AB', 22.0, 22.0, 'AB', 38.0, 35.0, 39.0, 32.0, 26.0, 7.0, 29.0,
             38.0, 36.0, 38.0, 35.0, 40.0, 42.0, 553.0],
            [4.0, 1704.0, 'DDD', 21.0, 28.0, 'AB', 29.0, 20.0, 19.0, 'D', 39.0, 37.0, 41.0, 24.0, 21.0, 7.0, 25.0,
             22.0, 22.0, 36.0, 37.0, 43.0, 39.0, 510.0],
            [5.0, 1705.0, 'EEE', 20.0, 27.0, 27.0, 24.0, 30.0, 28.0, 46.0, 39.0, 37.0, 46.0, 43.0, 49.0, 44.0, 41.0,
             40.0, 44.0, 42.0, 42.0, 46.0, 44.0, 759.0],
            [6.0, 1706.0, 'FFF', 29.0, 20.0, 'UFM', 24.0, 'AB', 28.0, 'RI', 39.0, 37.0, 46.0, 43.0, 49.0, 44.0, 41.0,
             40.0, 44.0, 42.0, 42.0, 46.0, 44.0, 658.0]]

   sec_b = [['College', 'Branch', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
             '', '', '', ''],
            ['Course', 'Year', 'Section', 'Session', 'Subject Wise Passing Marks', 'Internal Theory Passing Marks',
             'External Theory Passing Marks', 'Internal Practical Passing Marks', 'External Practical Passing Marks',
             '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            ['No. of Theory Subjects Internal', 'Subject Code', 'Subject Code', 'Subject Code', 'Subject Code',
             'Subject Code',
             'Subject Code', 'Subject Code', 'Passing Marks', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
             ''],
            ['No. of Lab Subjects Internal', 'Subject Code', 'Subject Code', 'Subject Code', 'Subject Code',
             'Passing Marks',
             '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            ['No. of Theory Subjects External', 'Subject Code', 'Subject Code', 'Subject Code', 'Subject Code',
             'Subject Code',
             'Subject Code', 'Subject Code', 'Passing Marks', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
             ''], ['No. of Lab Subjects External', 'Subject Code', 'Subject Code', 'Subject Code', 'Subject Code',
                   'Passing Marks',
                   '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            ['', '', '', 'Theory Subject Code', 'Theory Subject Code', 'Theory Subject Code', 'Theory Subject Code',
             'Theory Subject Code', 'Theory Subject Code', 'Practical Subject Code', 'Practical Subject Code',
             'Practical Subject Code',
             'Practical Subject Code', 'Theory Subject Code', 'Theory Subject Code', 'Theory Subject Code',
             'Theory Subject Code',
             'Theory Subject Code', 'Theory Subject Code', 'Practical Subject Code', 'Practical Subject Code',
             'Practical Subject Code',
             'Practical Subject Code', ''],
            ['No of Students(5)', '', '', 'Subject Name', 'Subject Name', 'Subject Name', 'Subject Name',
             'Subject Name',
             'Subject Name', 'Subject Name', 'Subject Name', 'Subject Name', 'Subject Name', 'Subject Name',
             'Subject Name',
             'Subject Name', 'Subject Name', 'Subject Name', 'Subject Name', 'Subject Name', 'Subject Name',
             'Subject Name',
             'Subject Name', 'Total'],
            ['S.No', 'R.No', 'S.Name', 'Internal Marks(30)', 'Internal Marks(30)', 'Internal Marks(30)',
             'Internal Marks(30)',
             'Internal Marks(30)', 'Internal Marks(30)', 'Internal Marks(50)', 'Internal Marks(50)',
             'Internal Marks(50)',
             'Internal Marks(50)', 'External Marks(70)', 'External Marks(70)', 'External Marks(70)',
             'External Marks(70)',
             'External Marks(70)', 'External Marks(70)', 'External Marks(50)', 'External Marks(50)',
             'External Marks(50)',
             'External Marks(50)', '(total on report-card(1000))'],
            [1.0, 1701.0, 'AAA', 29.0, 30.0, 30.0, 30.0, 28.0, 26.0, 49.0, 46.0, 48.0, 46.0, 44.0, 44.0, 48.0, 56.0,
             42.0, 48.0, 46.0, 46.0, 45.0, 44.0, 825.0],
            [2.0, 1702.0, 'BBB', 19.0, 22.0, 21.0, 21.0, 30.0, 30.0, 45.0, 42.0, 37.0, 45.0, 31.0, 42.0, 21.0, 38.0,
             44.0, 40.0, 40.0, 37.0, 42.0, 44.0, 691.0],
            [3.0, 1703.0, 'CCC', 25.0, 26.0, 27.0, 23.0, 22.0, 22.0, 35.0, 38.0, 35.0, 39.0, 32.0, 26.0, 41.0, 29.0,
             38.0, 36.0, 38.0, 35.0, 40.0, 42.0, 649.0],
            [4.0, 1704.0, 'DDD', 21.0, 28.0, 30.0, 29.0, 20.0, 19.0, 40.0, 39.0, 37.0, 41.0, 24.0, 21.0, 7.0, 25.0,
             22.0, 22.0, 36.0, 37.0, 43.0, 39.0, 580.0],
            [5.0, 1705.0, 'EEE', 20.0, 27.0, 27.0, 24.0, 30.0, 28.0, 46.0, 39.0, 37.0, 46.0, 43.0, 49.0, 44.0, 41.0,
             40.0, 44.0, 42.0, 42.0, 46.0, 44.0, 759.0]]

   wb = xlwt.Workbook()
   ws = wb.add_sheet('Section A')
   for i in range(len(sec_a)):
      for j in range(len(sec_a[i])):
         ws.write(i, j, sec_a[i][j])
   ws = wb.add_sheet('Section B')
   for i in range(len(sec_b)):
      for j in range(len(sec_b[i])):
         ws.write(i, j, sec_b[i][j])
   wb.save("SampleForAnalysis.xls")


def generateSampleFileAndDownload():
   try:
      for_analysis()
      for_prediction()
      print('Sample File Generated Successfully!!')
      return True, 'Sample File Generated Successfully!!'
   except:
      return False, 'Error occured in Generating Sample File..'