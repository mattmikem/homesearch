#Pull of test set for HomeSearch procedure:

#M. Miller, 2016

#Following borrowed from: https://andrewpwheeler.wordpress.com/2015/12/28/using-python-to-grab-google-street-view-imagery/

#Key 1: 
key1 = "AIzaSyCr9tXJARt5KW7nUC3B03lHip_9P9Z0F44"

import urllib, os

myloc = r"/Users/matthewmiller/Dropbox/Research/Urban/Projects/HomeSearch/Images" #replace with your own location
key = "&key=" + key1 #got banned after ~100 requests with no key

#Head refers to direction facing

def GetStreet(Add,SaveLoc,Head):
  base = "https://maps.googleapis.com/maps/api/streetview?size=1200x800&location="
  face = "&heading="+str(Head)
  MyUrl = base + Add + face + key
  fi = Add + " " + str(Head) + ".jpg"
  urllib.urlretrieve(MyUrl, os.path.join(SaveLoc,fi))

#Numbers for range of street addresses on 6th street from Main St to LA River
    
e_u = 1599
      
for i in range(100,e_u,15):
    j = str(i) + " East 6th Street, Los Angeles, CA"
    GetStreet(Add=j,SaveLoc=myloc,Head=0)
    GetStreet(Add=j,SaveLoc=myloc,Head=180)
    
    
    
    
    
#Tests = ["457 West Robinwood Street, Detroit, Michigan 48203",
#         "1520 West Philadelphia, Detroit, Michigan 48206",
#         "2292 Grand, Detroit, Michigan 48238",
#         "15414 Wabash Street, Detroit, Michigan 48238",
#         "15867 Log Cabin, Detroit, Michigan 48238",
#         "3317 Cody Street, Detroit, Michigan 48212",
#         "14214 Arlington Street, Detroit, Michigan 48212"]

#for i in Tests:
  