import csv
from typing import Dict
def sort_site(filename: str)->list:
    with open(filename,'r',encoding = 'utf-8') as f:
        read = csv.reader(f)
        read_next = next(read)
        dict1: Dict = {}
        sites = []
        for row in read:
            if ensure_num(row[5]):
                visit = int (row[5])
                dict1[visit] = row[2]
            else:
                continue

        for key in sorted(dict1,reverse = True):
            sites.append(dict1[key])
        print ("排名前20的网站：\n")
        for k in sites[:20]:
            print(k)
            
        


def ensure_num(str1: str) -> bool:
    flag = 1
    for i in str1:
        if  '0' <= i <='9':
            continue
        else:
            flag = 0
    if flag == 0:
        return False
    else:
        return True

#你需要替换csv文件的具体位置
if __name__ =='__main__':
    sort_site(r'your csv location')
    
