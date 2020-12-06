# find number of 6-digit passwords that pass given rules "

def count_passwords(start,end):
    count = 0
    for pswd in range(start,end+1):
        flag_double = False
        flag_decrease = False
        pstring = str(pswd)
        for i in range(len(pstring)-1):
            if int(pstring[i]) > int(pstring[i+1]):
                flag_decrease = True
            if pstring[i] == pstring[i+1]:
                flag_double = True

        if flag_double and not flag_decrease:
            count += 1
    return count

def count_passwords2(start,end):
    count = 0
    for pswd in range(start,end+1):
        flag_double = False
        flag_decrease = False
        dict_double = dict()
        pstring = str(pswd)
        for i in range(len(pstring)-1):
            if int(pstring[i]) > int(pstring[i+1]):
                flag_decrease = True
        for i in range(len(pstring)):
            if pstring[i] not in dict_double.keys():
                dict_double[pstring[i]] = 1
            else:
                dict_double[pstring[i]] += 1
        for k,v in dict_double.items():
            if v == 2:
                flag_double = True
        if flag_double and not flag_decrease:
            count += 1
    return count


print(count_passwords2(111111,111111))
print(count_passwords2(223450,223450))
print(count_passwords2(123789,123789))
print(count_passwords2(112233,112233))
print(count_passwords2(123444,123444))
print(count_passwords2(111122,111122))
#
#
print(count_passwords2(153517,630395))

