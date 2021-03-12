from rarfile import RarFile
path = '/Users/username/Downloads/'
filename = 'py_20200326_174202.rar'
filepath = 'temp/'

rf = RarFile(path+filename, mode='r') # mode的值只能为'r'
rf_list = rf.namelist() # 得到压缩包里所有的文件
print('rar文件内容', rf_list)

for f in rf_list:
    rf.extract(f, path + filepath)  # 循环解压，将文件解压到指定路径
# 一次性解压所有文件到指定目录
# rf.extractall(path) # 不传path，默认为当前目录
