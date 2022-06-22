from datetime import datetime

str_data = "31/05/2022"
str_data2 = "31/05/2022 19:00"

dt = datetime.strptime(str_data, '%d/%m/%Y')
dt2 = datetime.strptime(str_data2, '%d/%m/%Y %H:%M')#H -> i = hora 12

print(type(dt))
print(dt)
print(dt2)