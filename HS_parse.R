#HS_parse.R
#Parse through OA (OpenAddresses) alongside .py module

install.packages('reshape2')

library(reshape2)

#Test on LA addresses

ca_path <- "/Users/matthewmiller/Dropbox/Data/OpenAddresses/openaddr-collected-us_west/us/ca"

la_add <- read.csv(paste(ca_path, "los_angeles.csv", sep="/"), header=TRUE, sep=",");

num_split <- colsplit(la_add$NUMBER, " ", c('NUM1','NUM2'))
la_add <- cbind(la_add, num_split)

#Limit within four LA streets

streets <- c('East 6th Street', 'East 3rd Street', 'South Central Ave', 'South Spring Street')

la_test <- la_add[STREET %in% streets & CITY == 'Los Angeles',]


