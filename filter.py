__author__ = 'Dinesh'
''' FIle Filter. Day represents the day name  '''

for day in range(1, 4):
    read_file_path = 'C:\\Users\\Dinesh\\Desktop\\Files\\bmcl0'+ str(day).zfill(2)+'-2008-01-' + str(day).zfill(2)+'.Std';
    new_file_path='C:\\Users\\Dinesh\\Desktop\\NewFiles\\bmcl001'+ str(day).zfill(2)+'-2008-01-' + str(day).zfill(2)+'.txt';
    new_file=open(new_file_path, 'w')
    with open(read_file_path, 'r') as f:
        lines = f.readlines()
        for x in range(0, 1440, 60):
            new_file.write(lines[x])
