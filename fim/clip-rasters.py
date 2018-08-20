import rasterio
import os 
import numpy as np
import geopandas as gpd 
from multiprocessing.dummy import Pool as ThreadPool

pathRowlist = ['012055']

def openTxt(fileTxt):

    with open(fileTxt) as item:
        listItems = item.read().splitlines()

    return listItems

def clipShape(shapeId,projRaster,rasterId):

    shape = gpd.read_file(shapeId)

    # print 'projShape \n'
    # print shape.crs
    reprojShape = shape.to_crs(epsg = projRaster)

    # print 'reprojShape \n'
    # print  reprojShape 
    boundsShape = reprojShape.bounds

    print 'type bounds \n'
    print type(boundsShape['maxx'][0])

    clipCommand = """rio clip """\
                  + str(rasterId) + ' ' + str(shapeId[:2]) + str(shapeId[3:9]) + '-clip-'\
                  + str(rasterId[44:]) + ' --bounds '+ str(boundsShape['minx'][0]) + ' ' + str(boundsShape['miny'][0])\
                  +  ' ' + str(boundsShape['maxx'][0]) + ' ' +  str(boundsShape['maxy'][0])

    print clipCommand

    os.system(clipCommand)

def listShapes(pathRow,projRaster,rasterId):
    
    listCommandSHP = """ls *"""\
                     + str(pathRow)+'.shp > '\
                     + str(pathRow)+ '.txt'

    os.system(listCommandSHP)
    open_txt = str(pathRow)+ '.txt'
    shapesIds =  openTxt(open_txt)
    map(lambda shapeId: clipShape(shapeId,projRaster,rasterId),shapesIds)

def processing(raterId):
    
    pathRow = raterId[10:16]
    raster = rasterio.open(raterId)
    projRaster = int(raster.crs['init'][5:])
    
    # print 'projRaster \n'
    # print projRaster

    listShapes(pathRow,projRaster,raterId)

for pr in pathRowlist:

	os.system('ls *'+pr+'*band5.tif > '+pr+'-B5.txt')
	os.system('ls *'+pr+'*band7.tif > '+pr+'-B7.txt')
	rasterId_b5 = openTxt(pr+'-B5.txt')
	rasterId_b7 = openTxt(pr+'-B7.txt')

	map(processing,rasterId_b5)
	map(processing,rasterId_b7)


# Estrtura dos arquivos #
# LC08_L1TP_012054_20160307_20170328_01_T1_sr_band1 #
