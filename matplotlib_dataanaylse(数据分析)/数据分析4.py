import csv

def read_data(filename: str):
    with open(filename,'r',encoding = 'utf-8') as f:
        read = csv.reader(f)
        read_next = next(read)

        channel_visit = {}
        
        for row in read:
            if ensure_num(row[5]):
                channel_visit[int(row[5])] = row[3]
                

        channel_number = {}
        for key,value in channel_visit.items():
            if value in channel_number.keys():
                channel_number[value] += key
            else:
                channel_number[value] = key
        new_dict = {}
        for value,key in channel_number.items():
            new_dict[key] = value

        channel_number.clear()
        for key in sorted(new_dict.keys(),reverse = True):
            channel_number[new_dict[key]] = key
    #'找出前五的播放频道'
        fivevisit_channel = []
        i = 0
        for key in channel_number.keys():
            if i == 5:
                break
            fivevisit_channel.append(key)
            i += 1
    return fivevisit_channel

    #
def analyse(fivevisit_channel: list,filename: str):
    visit_source = {}
    tmp_source_visit = {}
    visit_site = {}
    tmp_site_visit = {}
    i = 1
    for channel in fivevisit_channel:
        with open(filename,'r',encoding = 'utf-8') as f:
            read = csv.reader(f)
            for row in read:
                if row[3] == channel and ensure_num(row[5]):
                    visit_source[int(row[5])] = row[1]
                    visit_site[int(row[5])] = row[2]
            #'将相同的来源的访问量叠加'
            for key ,value in visit_source.items():
                if value in tmp_source_visit.keys():
                    tmp_source_visit[value] += key
                else:
                    tmp_source_visit[value] = key

            for key ,value in visit_site.items():
                if value in tmp_site_visit.keys():
                    tmp_site_visit[value] += key
                else:
                    tmp_site_visit[value] = key

            #print(tmp_site_visit)
            #print('ok')
            #print(tmp_source_visit)
            #'将叠加后的字典的键和值对调'
            visit_source = {}
            visit_site = {}
            for key,value in tmp_source_visit.items():
                visit_source[value] = key

            for key,value in tmp_site_visit.items():
                visit_site[value] = key
                
            num = 0
            print('{}. 访问量排名第{}的频道是  --> {}'.format(i,i,channel))
            print('\n')
            print('''在频道   {}   下排名前五的广告的来源是: '''.format(channel))
            
            for key in sorted(visit_source.keys(),reverse = True):
                if num == 5:
                    break
                print(visit_source[key],end = '  ')
            print('\n')
            num = 0
            print('在频道   {}   下排名前五的网站是: '.format(channel))
            for key in sorted(visit_site.keys(),reverse = True):
                if num == 5:
                    break
                print(visit_site[key],end = '  ')
                num += 1
            
            tmp_source_visit.clear()
            visit_source.clear()
            tmp_site_visit.clear()
            visit_site.clear()
            i += 1
            
            print('\n')
            print('\n')

        #print(fivevisit_channel)
            
def ensure_num(string):
    flag = 1
    for i in string:
        if '0' <= i <= '9':
            continue
        else:
            flag = 0

    return flag == 1
        
    


if __name__ == "__main__":
    list1 = read_data(ryour csv location)
    analyse(list1 ,r'your csv location)
