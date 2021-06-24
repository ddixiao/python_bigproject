import matplotlib.pyplot as plt
from datetime import datetime
import csv
import time
def read_data(filename: str) -> dict:
    with open(filename,'r',encoding = 'utf-8') as f:
        read = csv.reader(f)
        read_next = next(read)
        #print(read_next)
        #define:
        part_dict = {}
        new_dict = {}
        
        begin_time = datetime.strptime('2018/5/15','%Y/%m/%d')
        end_time = datetime.strptime('2018/5/31','%Y/%m/%d')
        int_btime = time.mktime(begin_time.timetuple())
        int_etime = time.mktime(end_time.timetuple())
        
        #exe
        for row in read:
            tmp = datetime.strptime(row[0],'%Y/%m/%d')
            tmp1 = time.mktime(tmp.timetuple())
            if  int_btime <= tmp1 <= int_etime:
                part_dict[int(row[5])] = row[1]
        for key,value in part_dict.items():
            int_key = int(key)
            if value in new_dict.keys():
                new_dict[value] += int_key
            else:
                new_dict[value] = int_key

        return new_dict

#draw img
def draw_img(new_dict: dict):
    source = []
    visit = []
    for key,value in new_dict.items():
        source.append(key)
        visit.append(value)

    plt.style.use('seaborn')
    fig ,ax = plt.subplots(figsize = (11,16))
    
    ax.bar(source,visit)

    ax.set_title('5月15日到5月31日的访问总量',fontsize = 26 ,fontproperties = 'SimSun')
    ax.set_xlabel('source',fontsize = 16,fontproperties = 'SimSun')
    ax.set_ylabel('visit',fontsize = 16,fontproperties = 'SimSun')
    ax.tick_params(axis = 'both',which = 'major',labelsize = 16)

    plt.xticks(source,rotation = 45,fontproperties = 'SimSun')
    plt.show()
    
    #print(new_dict)
    print(source)
    print(visit)

    
        

if __name__ == '__main__':
    new_dict = read_data(r'your csv location')
    draw_img(new_dict)
