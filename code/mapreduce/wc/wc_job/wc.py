#!/usr/bin/python
# -*- coding: utf-8 -*-
from mrjob.job import MRJob
import re


class MRwordCount(MRJob):
    '''
        line:一行数据
        (a,1)(b,1)(c,1)
        (a,1)(c1)
        (a1)
    '''
    def mapper(self, _, line):
        pattern=re.compile(r'(\W+)')
        for word in re.split(pattern=pattern,string=line):
            if word.isalpha():
                yield (word.lower(),1)


    def reducer(self, word, count):
        #shuff and sort 之后
        '''
        (a,[1,1,1])
        (b,[1])
        (c,[1])
        '''
        count_list=list(count)
        yield (word,sum(count_list))

if __name__ == '__main__':
    MRwordCount.run() #run()方法，开始执行MapReduce任务。

