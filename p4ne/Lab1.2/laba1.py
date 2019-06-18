from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']
aСolumn = sheet['A'][1:]
dСolumn = sheet['D'][1:]
cСolumn = sheet['C'][1:]


def getvalue(x): return x.value
list1 = list(map(getvalue, aСolumn))
list2 = list(map(getvalue, cСolumn))
list3 = list(map(getvalue, dСolumn))

pyplot.plot(list1, list3)
pyplot.plot(list1, list2)
pyplot.show()
