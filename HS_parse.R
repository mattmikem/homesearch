#HS_parse.R
#Parse through OA (OpenAddresses) alongside .py module

#install.packages('reshape2')
#install.packages('ggmap')
#install.packages('ggplot2')
#install.packages('doBy')
#install.packages('taRifx')

library(reshape2)
library(ggmap)
library(ggplot2)
library(doBy)
library(taRifx)

#Test on LA addresses

ca_path <- "/Users/matthewmiller/Dropbox/Data/OpenAddresses/openaddr-collected-us_west/us/ca"

la_add <- read.csv(paste(ca_path, "los_angeles.csv", sep="/"), header=TRUE, sep=",");

num_split <- colsplit(la_add$NUMBER, " ", c('NUM1','NUM2'))
la_add <- cbind(la_add, num_split)
la_add$NUM1 <- destring(la_add$NUM1)

#Limit within four LA streets

streets <- c('East 6th Street', 'East 3rd Street', 'South Central Avenue', 'South Spring Street')

la_test <- la_add[la_add$STREET %in% streets & la_add$CITY == 'Los Angeles' & la_add$NUM1<1400,]

##Map Addreses selected

#attach(la_test)

act_city = "los angeles"

max_lat <- max(la_test$LAT)
min_lat <- min(la_test$LAT)
max_lon <- max(la_test$LON)
min_lon <- min(la_test$LON)

mean_lat <- (max_lat+min_lat)/2
mean_lon <- (max_lon+min_lon)/2

c_point <- c(lon = mean_lon, lat = mean_lat)

city_map <- qmap(c_point, zoom = 14)

city_map + geom_point(aes(x = la_test$LON, y = la_test$LAT, color = la_test$STREET), data = la_test)

