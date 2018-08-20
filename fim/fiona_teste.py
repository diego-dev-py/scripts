#!/usr/bin/python
# -*- coding: utf-8 -*-
import fiona

import os 



lista = []
path = \
    '/mnt/auxiliar/BASE_DADOS/FIM-PANAMA/fincas-validas/novo-shape-unico-2/shape-unico-fincas-panama.shp'

os.system('fio info --indent 2 ' + path)
# shape = fiona.open(path,'r')
# shape_dic = shape.meta

# print shape_dic

with fiona.open(path,'r') as shape:

    metadata = shape.meta
    f = next(shape)

with fiona.open('/tmp/foo', 'w', layer='bar', **metadata) as dst:
    dst.write(f)
    lista.append(dst)

    
# print(fiona.listlayers('/tmp/foo'))

with fiona.open('/tmp/foo', layer='bar') as src:
    print(len(src))
    f = next(src)
    print(f['geometry']['type'])
    print(f['properties']['Name'])

print lista

# with fiona.drivers():

#     with open(path) as src:

#         print 'oi'
#         metadata = src.meta
#         f = next(src)

#     with fiona.open('/tmp/foo', 'w', layer='bar', **meta) as dst:

#         dst.write(f)
#         print fiona.listlayers('/tmp/foo')

#     with fiona.open('/tmp/foo', layer='bar') as src:

#         print len(src)
#         f = next(src)

#         print f['geometry']['type']
#         print f['properties']