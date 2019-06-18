"""
equake_data1.py
analyzing magnitudes imported from USGS website and making a report.
Author:Saud Aljandal
"""

import data_analysis_more as d
import urllib.request

 

def readeqf():
    '''()->(list)
    called by:equake_main()
    Importing information from USGS website about earthquake events of magnitude 5 or higher,
    in the 250 km radius centered around Eugene, OR, over the past 100 years.
    A list of them will be returned.

    >>>readeqf()
    [5.2, 5.1, 5.0, 5.7, 5.8, 5.4, 5.3, 5.4, 5.2, 5.6]"at the time of typing this code"
     '''
    url=urllib.request.urlopen('http://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=1916-02-01&latitude=44.0519&longitude=-123.0867&maxradiuskm=250&minmagnitude=5')

    result=[]
    mags=[]
    for line in url:
        result=line.decode()
        result=result.rstrip().split(',')

        if len(result)>1:
            mags.append(result[4])
    del mags[0]
    mags=[float(i) for i in mags]
    
    return mags
    
def equake_analysis(mags):
    '''(list)->(report)
    called by: equake_main()
    alist of earthquake magnitutes(mags) will go through analyzing
    functions mean, median , mode.
    And a report will be ready.

    >>>equake_analysis(mags)
    report is ready 
    '''
    freqD  = d.genFrequencyTable(mags)
    print("The mode is:",d.mode(mags))
    print("The mean is:",d.mean(mags))
    print("The median is:",d.median(mags),"\n")
    print("FREQUENCY TABLE:")
    d.freqTable(mags)
    return None

def equake_main():
    '''() -> None

    Calls:  readeqf, equake_analysis

    Top level function for analysis of
    earthquake data from USGS website.

    Returns None.

    >>> equake_main()
        The mode is: [5.4, 5.2]
    The mean is: 5.37
    The median is: 5.35 

    FREQUENCY TABLE:
    5.0    1        
    5.1    1        
    5.2    2        
    5.3    1        
    5.4    2        
    5.6    1        
    5.7    1        
    5.8    1 
    '''
    emags = readeqf()
    equake_analysis(emags)

    return None
