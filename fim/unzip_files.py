import os
import requests
from multiprocessing.dummy import Pool as ThreadPool
import time
import timeit

inicio = timeit.default_timer()

def unpack(fileid):

    print 'descompressing file ' + fileid + '\n'
    os.system('tar -vzxf ' + fileid)

def delete_compacted(fileid):

    print 'deleting file ' + fileid + '\n'
    os.system('rm ' + fileid)

    

os.system('ls > files.txt')

with open('files.txt') as item:
    
    fileids = item.read().splitlines()


# parallelism = 4
# thread_pool = ThreadPool(parallelism)
# thread_pool.map(unpack, fileids)
# thread_pool.map(delete_compacted, fileids)
map(unpack, fileids)
map(delete_compacted, fileids)
fim = timeit.default_timer()

print 'duracao: %f' % (fim - inicio)