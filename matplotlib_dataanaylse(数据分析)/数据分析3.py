
import csv
from datetime import datetime
import time
import matplotlib.pyplot as plt

def read_data(filename: str):
    with open(filename,'r',encoding = 'utf-8') as f:
        read = csv.reader(f)
        next_read = next(read)
        may_dict = {}
        june_dict = {}
        #may
        may_time1 = datetime.strptime('2018/5/1','%Y/%m/%d')
        may_time2 = datetime.strptime('2018/5/31','%Y/%m/%d')

        int_may_time1 = time.mktime(may_time1.timetuple())
        int_may_time2 = time.mktime(may_time2.timetuple())

        #june
        
        june_time1 = datetime.strptime('2018/6/1','%Y/%m/%d')
        june_time2 = datetime.strptime('2018/6/30','%Y/%m/%d')

        int_june_time1 = time.mktime(june_time1.timetuple())
        int_june_time2 = time.mktime(june_time2.timetuple())

        #
        for row in read:
            if row[4] != '-' and row[5] != '-':   #剔除media为空的数据
                tmp_time = datetime.strptime(row[0],'%Y/%m/%d')
                tmpint_time = time.mktime(tmp_time.timetuple())
                
                if int_may_time1 <= tmpint_time <= int_may_time2:
                    may_dict[int(row[5])] = row[1]
                elif int_june_time1 <= tmpint_time <= int_june_time2:
                    june_dict[int(row[5])] = row[1]
        
        #'将重复的source整理到一起，并计算访问量'
        new5_dict = {}
        new6_dict = {}
        for key ,value in may_dict.items():
            if value in new5_dict.keys():
                new5_dict[value] += key
            else:
                new5_dict[value] = key

        for key,value in june_dict.items():
            if value in new6_dict.keys():
                new6_dict[value] += key
            else:
                new6_dict[value] = key
        print('may\n')
        for key,value in new5_dict.items():
            print(key ,':' ,value)
        print('\n')
        print('june\n')
        for key,value in new6_dict.items():
            print(key ,':' ,value)

        return new5_dict, new6_dict

def analysize(may_dict: dict,june_dict: dict):
    may_visits = []
    june_visits = []
    
    
    source = []
    
    for key,value in may_dict.items():
        for key1,value1 in june_dict.items():
            if key == key1:
                source.append(key)
                may_visits.append(value)
                june_visits.append(value1)
    # '5月里有的而6月没有的souce'           
    for key,value in may_dict.items():
        if key not in source:    
            source.append(key)   
            june_visits.append(0)     #'6月置零'
            may_visits.append(value)  
               
    #'6月里有的而5月没有的souce'
    for key ,value in june_dict.items():
        if key not in source:
            source.append(key)
            june_visits.append(value)
            may_visits.append(0)
         
    plt.style.use('seaborn')
    fig,ax = plt.subplots(figsize=(11, 7.5))
 
    ax.plot(source, may_visits, c = 'red',alpha = 0.5)
    ax.plot(source, june_visits,c = 'blue', alpha = 0.5)
    ax.fill_between(source,may_visits,june_visits,facecolor = 'blue',alpha = 0.1)
  
    ax.set_title('5月和6月visit的对比(红色5月，蓝色6月)',fontsize = 24,fontproperties="SimSun")
    ax.set_xlabel('source',fontsize = 16,fontproperties="SimSun")
    ax.set_ylabel('visit',fontsize = 16,fontproperties="SimSun")
    ax.tick_params(axis = 'both',which = 'major',labelsize = 16)

    plt.xticks(source,rotation=45,fontproperties='SimSun')
    plt.show()

    


if __name__ == '__main__':
    may_dict,june_dict = read_data(r'your csv location')
    analysize(may_dict,june_dict)


    
