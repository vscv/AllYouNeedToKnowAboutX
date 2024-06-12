"""Python

#讀取excel，將重複的名稱由主要sheet中移除。


import pandas as pd
#from tqdm import tqdm
import time


# 三月中獎同仁名單
df_3 = pd.read_excel('113年6月在職編制非編制員工.xlsx', sheet_name='3月中獎名單')
month_3_name = df_3['姓名'].to_list()[27:47]
print(f"\n[check] 3月中獎同仁 共{len(month_3_name)}位：\n\n{month_3_name}\n")


# 六月在職同仁(已減去借調、派外、委外人員) PD way
df_in6 = pd.read_excel('113年6月在職編制非編制員工.xlsx', sheet_name='113年6月在職_編制、非編_扣除3月中獎者', converters={'工號':str})
df_in6_dnid = pd.DataFrame([df_in6.部門, df_in6.中文姓名, df_in6.工號]).transpose()
print(f"\n[check] 現職人數(未扣除前): {len(df_in6_dnid)}", )


# 將已得獎人排除現職名單
count=0
drop_ind_list=[]
print('\n\n[check] 交叉比對現有員工中以中獎者並刪除該列資訊：\n')
for i in range(len(df_in6_dnid['中文姓名'])):
    time.sleep(0.01)
    for name in month_3_name:
        if df_in6_dnid['中文姓名'][i] == name:
            count += 1
            print(count, df_in6_dnid['中文姓名'][i])
            drop_ind_list.append(i)

# Drop out the 3_name by list
df_clear=df_in6_dnid.drop(drop_ind_list)
print(f"\n[check] 現職人數 {len(df_in6_dnid['中文姓名'])} - 已獎人數 {len(drop_ind_list)}: 本次抽獎  {len(df_clear)} 人" )


# 六月可抽獎名單
df_clear.to_csv("六月現職同仁名單_without_comma_header.csv", index=False, header=False, sep=' ')
#df_clear.to_csv("六月現職同仁名單.csv", index=False)
#df_clear.to_string("六月現職同仁名單.txt", index=False)

"""



