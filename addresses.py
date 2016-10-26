##Address index build, from OpenAddresses
#M. Miller, 10/2016

add = "/Users/matthewmiller/Dropbox/Data/OpenAddresses/openaddr-collected-us_west/us"
st   = "ca"
city = "los_angeles"

#Import Addresses----------------------------------------------------

f = open(add+'/'+st+'/'+city+'.csv', 'r')

add_list = []

for lines in f:
		add_list = add_list + [lines.replace("\n","")]
        
f.close()
#------------------------------------------------------------------------

print add_list[1:5]