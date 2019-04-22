import csv


def write_city(info_city):
    csv_file = open('city.csv', 'a+')
    fileNames = ['city_id', 'city', 'city_num']
    # 创建csv文件句柄
    writer = csv.DictWriter(csv_file, fieldnames=fileNames)
    # 写入csv文件头部
    writer.writeheader()
    writer.writerow(info_city)


import xlsxwriter,json


def write_scenic():
    # 这里定义你要存入的文件名称
    workbook = xlsxwriter.Workbook('scenic.xls')  # 新建excel表
    worksheet = workbook.add_worksheet('sheet1')
    headings = ['scenic_id', 'scenic', 'branch', 'comment', 'rank', 'local', 'grade', 'phone', 'come_time', 'introduce',
                'traffic', 'scenic_score', 'interest_score', 'cost_score', 'feel_cmt', 'family_cmt', 'friend_cmt',
                'shop_cmt', 'alone_cmt', 'very_good_cmt', 'good_cmt', 'commonly_cmt', 'wrong_cmt', 'very_wrong_cmt']
    worksheet.write_row('A1', headings)
    # workbook.close()
    # 从json文件导入数据
    with open('scenic.json', 'r+') as file1:
        scenic_json = file1.readlines()
    a = 1

    for li in scenic_json:
        a = a + 1
        li = li.replace('\n', '')
        # print(json.loads(li))
        ss = json.loads(li)
        lists = []
        for content in headings:
            # print(ss[content])
            lists.append(ss[content])
        print('存入的数据', a)
        worksheet.write_row('A' + str(a), lists)
    workbook.close()

if __name__ == '__main__':
    write_scenic()
