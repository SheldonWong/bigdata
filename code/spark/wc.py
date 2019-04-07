#coding=utf8
import os
from pyspark import SparkConf,SparkContext

conf = SparkConf().setMaster('local').setAppName('word count')
sc = SparkContext(conf = conf)

#注意将这里改成自己的路径 
text_file = sc.textFile('hdfs:///datawhale/The_Man_of_Property.txt')
 
count = text_file.flatMap(lambda line:line.split(" ")) \
                    .map(lambda word:(word.encode("utf-8"),1)) \
                    .reduceByKey(lambda a,b:a+b)
print(count.take(50))
