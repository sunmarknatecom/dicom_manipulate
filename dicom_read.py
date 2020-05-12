import numpy as np

f = open('filename.dcm', 'rb')

lines = f.readlines()

ls_lines = []

for line in lines:
    ls_lines.append(line)

# for i in range(len(ls_lines[0])):
#     print(ls_lines[0][i], end=' ')
# print("")

for i in range(len(ls_lines[-1])):
    print(lines[-1][i], end=' ')
print("")
