"""
equake_data2.py
analyze and plot earthquake data
Author: Saud Aljandal
"""
import math
import random
import turtle
import urllib.request




def euclid_distance(point1, point2):
    '''(list,list)->float'''
    """
    computes the euclidean distance between two points
        point1: list of floats, index 0 is longitude, index 1 is latitude
        point2: list of floats, index 0 is longitude, index 1 is latitude
    Returns float, sqrt((x1-x2)**2 + (y1-y2)**2)
    """

    total = 0
    for index in range(len(point1)):
        diff = (point1[index] - point2[index])**2
        total += diff * diff

    return math.sqrt(total)

def createCentroids(k, datadict):
    '''(int,list)->(list)'''
    """
    randomly selects 'k' points from 'datadict' as the starting
        centroids for the k-means clustering algorithm
        k: int, number of clusters desired
        datadict: list of lists, each contained list represents an EQ event
    Return list of lists, each contained list is an event to act as the centroid
    """
    centroids = []
    count = 0
    centroid_keys = []

    while count < k:
        rkey = random.randint(1, len(datadict))
        if rkey not in centroid_keys:
            centroids.append(datadict[rkey])
            centroid_keys.append(rkey)
            count =count+ 1

    return centroids



def createClusters(k, centroids, datadict, iterations):
    '''(int,list,dict,int)->(list)'''
    """
    k-means clustering algorithm - implementation taken from page 249 of
    ranum and miller text, with some modifications.
    k: integer, number of clusters
    centroids: list of events, each event is the centroid of its cluster
    datadict: dictionary of all EQ events
    iterations: int, number of clustering iterations to perform
    Returns list of lists: each contained list is the set of indices into 'datadict'
    for events that belong to that cluster
    """
    for iteration in range(iterations):
        clusters = []
        for i in range(k):
            clusters.append([])

        for key in datadict:
            distances = []
            for cl_index in range(k):
                dist = euclid_distance(datadict[key], centroids[cl_index])
                distances.append(dist)
            min_dist = min(distances)
            index = distances.index(min_dist)
            clusters[index].append(key)

        dimensions = len(datadict[1])
        for cl_index in range(k):
            sums = [0]*dimensions
            for key in clusters[cl_index]:
                data_points = datadict[key]
                for ind in range(len(data_points)):
                    sums[ind] = sums[ind] + data_points[ind]
            for ind in range(len(sums)):
                cl_len = len(clusters[cl_index])
                if cl_len != 0:
                    sums[ind] /= cl_len
            centroids[cl_index] = sums
    return clusters


def readeqf():
   '''() -> list of lists of equake longitudes, latitudes
   called by:visualizeQuakes(k, r)
   Use USGS API to get data about earthquake
   events of magnitude >= 5 for past month;
   store earthquake longitude and latitudes
   in a list, which is returned.

   Called by: visualizeQuakes (and clusterAnalysis)

   For example,
   >>> readeqf()
   {1: [-122.75, 45.68], 2: [-121.73, 43.53]} 
   '''
   with urllib.request.urlopen(
   'http://earthquake.usgs.gov/fdsnws/event/1/\
query?format=csv\
&starttime=2016-02-01\
&minmagnitude=5'
) as eqf:
      
      eqdict = {}
      key = 0
      eqf.readline() # move past header
      for line in eqf:
         line = line.decode()
         line = line.strip().split(',')
         latitude = round(float(line[1]), 2)
         longitude = round(float(line[2]), 2)
         key += 1
         eqdict[key] = [longitude, latitude]

   return eqdict


def clusterAnaysis():
    '''()->(None)'''
    """
    creating a dictionary by calling readeqf,
    which will access the web query.

    >>>example
    clusterAnaysis()
    >>>
    """
    
    examDict = readeqf()
    examCentroids = createCentroids(5, examDict)
    examClusters = createClusters(5, examCentroids , examDict, 6)


def visualizeQuakes(k,r):
    '''(int,int)->turtle'''
    """
    visualizing data from createClusters and createCentroids.k=numbers of clusters
    wanted, r= number of iterations. a photo "worldmap" and turtle
    will points the cluster, whick are taken from the query link in the assignment page.

    >>>visualizeQuakes(6,2)
    turtle
    """
    # it should be:
    # datadict= readeqf() instead of:
    datadict ={1: [49.568742,26.959771]}
    quakeCentroids = createCentroids(k, datadict)
    clusters = createClusters(k, quakeCentroids,datadict, r)
    
    quakeT = turtle.Turtle()
    quakeWin = turtle.Screen()
    quakeWin.bgpic("worldmap.gif")
    quakeWin.screensize(1800,900)
    wFactor = (quakeWin.screensize()[0]/2)/180
    hFactor = (quakeWin.screensize()[1]/2)/90
    quakeT.hideturtle()
    quakeT.up()
    quakeT.speed(0)
    colorlist =["red","green","blue","orange","cyan","yellow"]
    for clusterIndex in range(k):
        quakeT.color(colorlist[clusterIndex])
        for akey in clusters[clusterIndex]:
            lon = datadict[akey][0]
            lat = datadict[akey][1]
            quakeT.goto(lon*wFactor,lat*hFactor)
            quakeT.dot()
    quakeWin.exitonclick()









visualizeQuakes(1,1)




