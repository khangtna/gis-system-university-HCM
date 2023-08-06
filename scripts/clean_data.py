import pandas as pd
import csv

file='D:\Study\PTIT\Intern  project\data_school.csv'

# with open(file,'r') as f:
#     lines=f.readlines()
#     # print(lines[0])
#     for line in lines:
#         if line == lines[0]:
#             # print(line)
#             continue
        # print(line)
        

        # line=line.split(',',6)
        # print(line)


data=[]
with open(file, 'w') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(data)

print(data)


# df = pd.DataFrame(list_uni, columns=['id','name','address', 'longitude', 'latitude','location_name','created_date','update_date','status'])
# df.to_csv('D:\Study\PTIT\Intern  project\scripts\data\data_clean.csv', index=False)