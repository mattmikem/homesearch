#HS_parse.R
#Matt Miller, Oct 2016

#Parse through OA (OpenAddresses) alongside HS.py module, map locations

#install.packages('reshape2')
#install.packages('ggmap')
#install.packages('ggplot2')
#install.packages('doBy')
#install.packages('taRifx')
#install.packages('geosphere')
#install.packages('fields')
#install.packages('e1071')

library(reshape2)
library(ggmap)
library(ggplot2)
library(doBy)
library(taRifx)
library(geosphere)
library(fields)
library(e1071)

#Theta function, keep consistent camera alignment (changes 'heading' in GSV API)

#Current method uses heading aligned with orthongonal vector to vector between an address and its
#nearest neighbor, and is subject to small pertubations (still, it does rather well).
#Options less sensitive: moving, within street odd/even-address linear regression, or moving
#within street SVM (approximating road between odd and even addresses).

#Note - addresses have (lon,lat) coordinates, so every address is a 2x1 vector

norm <- function(x) sqrt(sum(x^2))

theta <- function(add0, add1) {
  add_vector  <- add1 - add0
  orth_vector <-  c(-1*add_vector[2], add_vector[1])
  north_vector <- c(orth_vector[1],0)
  theta <- 180*acos((north_vector %*% orth_vector)/(norm(orth_vector)*norm(north_vector)))/pi
  return(theta)
}

#Test on LA addresses

setwd('/Users/matthewmiller/Dropbox/Research/Urban/Projects/HomeSearch/Working')

ca_path <- "/Users/matthewmiller/Dropbox/Data/OpenAddresses/openaddr-collected-us_west/us/ca"

la_add <- read.csv(paste(ca_path, "los_angeles.csv", sep="/"), header=TRUE, sep=",");

num_split <- colsplit(la_add$NUMBER, " ", c('NUM1','NUM2'))
la_add <- cbind(la_add, num_split)
la_add$NUM1 <- destring(la_add$NUM1)
la_add$ODD <- la_add$NUM1 %% 2

#Limit within four LA streets

#streets <- c('East 6th Street', 'East 3rd Street', 'South Central Avenue', 'South Spring Street')
streets <- c('East 4th Street')

la_test <- la_add[la_add$STREET %in% streets & la_add$CITY == 'Los Angeles' & la_add$NUM1<1400 & la_add$NUM2 == "" & la_add$ODD == 1,]

#Flag closest address on same street side

la_test <- la_test[order(la_test$ODD, la_test$STREET, la_test$NUM1),]

la_test$LAG  <- rep(0,nrow(la_test))
la_test$LEAD <- rep(0,nrow(la_test))
la_test$LOOK <- rep(0,nrow(la_test))
la_test$THETA <- rep(0,nrow(la_test))


for(i in 2:(nrow(la_test)-1)) {
  la_test$LAG[i]  <- dist(t(cbind(c(la_test$LAT[i],la_test$LON[i]),c(la_test$LAT[i-1],la_test$LON[i-1]))), method = 'euclidean')
  la_test$LEAD[i] <- dist(t(cbind(c(la_test$LAT[i],la_test$LON[i]),c(la_test$LAT[i+1],la_test$LON[i+1]))), method = 'euclidean')
  if (la_test$LEAD[i] > la_test$LAG[i] & la_test$STREET[i] == la_test$STREET[i-1]) {
    la_test$LOOK[i] <- -1
  }
  else if (la_test$LEAD[i] < la_test$LAG[i] & la_test$STREET[i]==la_test$STREET[i+1]) {
    la_test$LOOK[i] <- 1  
  }
  look <- i + la_test$LOOK[i]
  la_test$THETA[i] <- round(theta(c(la_test$LAT[i],la_test$LON[i]),c(la_test$LAT[look],la_test$LON[look])))
}

##To keep

la_test <- la_test[,c("LAT", "LON", "STREET", "CITY", "POSTCODE", "NUM1", "THETA")]
la_test <- la_test[order(la_test$STREET, la_test$NUM1),]

write.csv(la_test, 'la_test.csv')

##Map Addresses selected

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

