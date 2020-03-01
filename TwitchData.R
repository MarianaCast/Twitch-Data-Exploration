#Data was found at http://dash.ipv6.enstb.fr/dataset/live-sessions/#downloads
library(tidyverse)
twitch <- read.csv("/home/mariana/Documents/Machine Learning/Project 2/Twitch.csv", header=TRUE)
tb <- tbl_df(twitch)
tb
rm(twitch)
glimpse(tb)
select(tb, language, viewer_count, user_name) %>% glimpse

#Arrange in ascending order
tb <- arrange(tb, desc(viewer_count))

# Remove rows that contain unecessary info from the API request
tb <- subset(tb, language!="language")

#Convert from factor to double
tb$viewer_count <- as.numeric(as.character(tb$viewer_count))
#Display the lowest and highest viewer count
tb %>%
  summarize(min=min(viewer_count), max=max(viewer_count),median=median(viewer_count), sd=sd(viewer_count))

#Maximum = LCS game 