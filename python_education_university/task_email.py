f = open('C:/Users/admin/PycharmProjects/repos/task.txt')
s = []
z = []
list = []
for line in f:
    z = []
    s = line.split(",")
    z.append(s[1].strip())
    z.append(s[2].strip())
    list.append(z)


def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter += 1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails


print(email_gen(list))
