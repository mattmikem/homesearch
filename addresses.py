##Address index build, from OpenAddresses
#M. Miller, 10/2016

add = "/Users/matthewmiller/Dropbox/Data/OpenAddresses/openaddr-collected-us_west/us"
work = "/Users/matthewmiller/Dropbox/Research/Urban/Projects/HomeSearch/Working"
st   = "ca"
city = "los_angeles"

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
    atemp = str(add_tuple[aa][6]) + " " +add_tuple[aa][3]+", "+add_tuple[aa][4]+",CA"+" "+str(add_tuple[aa][5])
    add_feed = add_feed + [atemp.replace('"','')]
    aa = aa + 1
    
print add_tuple[1]
print add_feed[1]