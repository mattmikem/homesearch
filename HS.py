#Pull of test set for HomeSearch procedure:

#M. Miller, 2016

#Following borrowed from: https://andrewpwheeler.wordpress.com/2015/12/28/using-python-to-grab-google-street-view-imagery/

#example url:https://maps.googleapis.com/maps/api/streetview?size=600x300&location=46.414382,10.013988&heading=151.78&pitch=-0.76&key=YOUR_API_KEY


#Key 1: 
key1 = "AIzaSyCr9tXJARt5KW7nUC3B03lHip_9P9Z0F44"

import urllib, os
import sys

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
head_feed = []


aa = 0

for a in add_list:
    add_tuple = add_tuple + [tuple(a.split(','))]
    #This allows the (x,y) coords or address location
    #atemp = str(add_tuple[aa][1])+","+str(add_tuple[aa][2])+"&heading="+str(add_tuple[aa][6])
    #add_feed = add_feed + [atemp]
    #head_feed = head_feed + [add_tuple[aa][6]]
    atemp = str(add_tuple[aa][6]) + " " +add_tuple[aa][3]+", "+add_tuple[aa][4]+", CA"+" "+str(add_tuple[aa][5])
    htemp = "&heading="+str(add_tuple[aa][7])
    add_feed = add_feed + [atemp.replace('"','')+htemp]
    aa += 1

#print add_feed[1:5]
#sys.exit(0)
    
#Use address list into GSV API
    
def GetStreet(Add,SaveLoc):
  base = "https://maps.googleapis.com/maps/api/streetview?size=1200x800&location="
  #face = "&heading="+str(head)
  MyUrl = base + Add + key
  fi = Add + ".jpg"
  urllib.urlretrieve(MyUrl, os.path.join(SaveLoc,fi))

#Numbers for range of street addresses on 6th street from Main St to LA River
          
#jj = 0    
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
  
#HomeSearch notes

#- Prop HHH on docket in LA for raising $1.2 billion to create 10,000 units of housing for the homeless
#- Focus on women and children affected by homelessness.
#- Concern: they say homelessness is increasing (11%), is this due to more people in LA actually losing homes, or more homeless people seeking out LA as a place where homelessness is most tolerable (given the existing level of services). 
#- Concern: Where will these units be built? 