#coding=utf8
import pyhdfs
fs = pyhdfs.HdfsClient(hosts='localhost,50070',user_name='sheldonwong')
fs.get_home_directory()#返回这个用户的根目录
fs.get_active_namenode()#返回可用的namenode节点

resp = fs.listdir('/')
print(','.join(resp))
'''
path='/home/sheldonwong/workspace/hdfs/'
file='test.txt'
file_name=path+file
#在上传文件之前，请修改本地 host文件 192.168.226.142 localhost C:\WINDOWS\system32\drivers\etc\host
print('路径已经存在') if fs.exists(path) else fs.mkdirs(path)
print('文件已存在') if fs.exists(path+file) else fs.copy_from_local('/test.txt',path+file,) #上传本地文件到HDFS集群

fs.copy_to_local(path+file, 'zhanggen.txt')# 从HDFS集群上copy 文件到本地
fs.listdir(path) #以列表形式['a.out', 'a.txt']，返回指定目录下的所有文件
response=fs.open(path+file) #查看文件内容
print(response.read())

fs.append(file_name,'Thanks myself for fighting ',) #在HDFS集群的文件里面添加内容
response=fs.open(file_name) #查看文件内容
print(response.read())
print(fs.get_file_checksum(file_name)) #查看文件大小
print(fs.list_status(path))#查看单个路径的状态
print(fs.list_status(file_name))#查看单个文件状态
'''
