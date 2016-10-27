#Pull of test set for HomeSearch procedure:

#M. Miller, 2016

#Following borrowed from: https://andrewpwheeler.wordpress.com/2015/12/28/using-python-to-grab-google-street-view-imagery/

#Key 1: 
key1 = "AIzaSyCr9tXJARt5KW7nUC3B03lHip_9P9Z0F44"

import urllib, os

myloc = r"/Users/matthewmiller/Dropbox/Research/Urban/Projects/HomeSearch/Images" #replace with your own location
key  = "&key=" + key1 #got banned after ~100 requests with no key
add  = "/Users/matthewmiller/Dropbox/Data/OpenAddresses/openaddr-collected-us_west/us/ca"
work = "/Users/matthewmiller/Dropbox/Research/Urban/Projects/HomeSearch/Working"
st   = "ca"
city = "los angeles"

#Head refers to direction facing

#Import Addresses----------------------------------------------------

f = open(work+'/'+'la_test.csv', 'r')

add_list = []

for lines in f:
		add_list = add_list + [lines.replace("\n","")]
        
f.close()
#------------------------------------------------------------------------

print add_list[1]

add_tuple = []
add_feed  = []


aa = 0

for a in add_list:
    add_tuple = add_tuple + [tuple(a.split(','))]
    atemp = str(add_tuple[aa][6]) + " " +add_tuple[aa][3]+", "+add_tuple[aa][4]+", CA"+" "+str(add_tuple[aa][5])
    add_feed = add_feed + [atemp.replace('"','')]
    aa += 1

#Use address list into GSV API
    
def GetStreet(Add,SaveLoc):
  base = "https://maps.googleapis.com/maps/api/streetview?size=1200x800&location="
  #face = "&heading="+str(Head)
  MyUrl = base + Add + key
  fi = Add + ".jpg"
  urllib.urlretrieve(MyUrl, os.path.join(SaveLoc,fi))

#Numbers for range of street addresses on 6th street from Main St to LA River
          
for j in add_feed:
    GetStreet(Add=j,SaveLoc=myloc)
    
    
    
    
    
    
#Tests = ["457 West Robinwood Street, Detroit, Michigan 48203",
#         "1520 West Philadelphia, Detroit, Michigan 48206",
#         "2292 Grand, Detroit, Michigan 48238",
#         "15414 Wabash Street, Detroit, Michigan 48238",
#         "15867 Log Cabin, Detroit, Michigan 48238",
#         "3317 Cody Street, Detroit, Michigan 48212",
#         "14214 Arlington Street, Detroit, Michigan 48212"]

#for i in Tests:
  