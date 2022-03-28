f = open('C:/Users/admin/PycharmProjects/repos/task_file.txt') #read info from file
s = []
q = []
list = []
valid_list = []
work_list = []
for line in f: #parsing file in new list
    z = []
    s = line.split(",")
    for i in s:
        z.append(i)
    list.append(z)
#list.pop(0)
#print(list)
f.close()

for i in list[1:]: #loop for get list of value without empty field and wrong phone number
    for k in range(1,5):
        if (len(i[k].strip()) == 0) or (len(i[3].strip()) != 7 ):
            #print(i)
            list.remove(i)
            break
        else:
            #valid_list.append(i)
            continue
#print(list)

for k in list[1:]: #get valid list of Name + Last_Name
    work_list = []
    work_list.append(k[1].strip())
    work_list.append(k[2].strip())
    q.append(work_list)
#print(q)

def email_gen(list_of_names): # function generation email address for valid list
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter += 1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails

#print(email_gen(q))

c = 0
for y in list[1:]: # loop to paste email in result list
    y[0] = email_gen(q)[c]
    c = c + 1

print(list)

w = open('C:/Users/admin/PycharmProjects/repos/task.txt', 'w') #open for write to file

for line in list: # loop-write to file
    #print(",".join(line))
    w.write(",".join(line))

w.close()