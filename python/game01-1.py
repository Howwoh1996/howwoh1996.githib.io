# 遊戲規則:吹氣球 每吹一次有不同的機率會爆炸 把氣球綁起來 會獲得關於氣球大小的積分
# 爆炸獲得 30%分數
# 吹氣球 破掉機率 0 , 0.02 , 0.04 , 0.07 , 0.1 ,0.15 , 0.2 , 0.25 , 0.3 , 0.4 , 0.5
# 積分增加 2000 2800 3600 4400 5200 6000 6800 7600 8400 9200
# 積分累加 2000 4800 8400 12800 18000 24000 30800 38200 46800 
import random


blow_posibilitly=[0 , 0.02 , 0.04 , 0.07 , 0.1 ,0.15 , 0.2 , 0.25 , 0.3 , 0.4 , 0.5]
blow_point=[2000+800*x for x in range(15)]
blow_total_point=[sum(blow_point[:x+1]) for x in range(14)]

times=8
times_arr=[5,6,7,8,9]

def point_count(times_in_function):
    # total_times=(90+144)*3+60-12
    total_times=1000000
    blow_times=0
    point=0
    otherbloom=0
    for i in range(total_times):
        
        if otherbloom%3!=0:
            otherbloom+=1
            point+=2000
            continue

        blow_times+=1
        # 判定有沒有吹破
        if(random.random()<blow_posibilitly[blow_times-1]):
            point+=blow_total_point[blow_times-2]*0.3
            otherbloom+=1
            blow_times=0
        elif(blow_times>=times_in_function):
            point+=blow_total_point[blow_times-1]
            otherbloom+=1
            blow_times=0

    return point/total_times

rank=[(x,point_count(x)) for x in times_arr]
# print(rank)
print(sorted(rank, key=lambda r:r[1],reverse=True))
 

