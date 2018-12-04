library(twitteR)
api_key <- "jF77AisWx3yItJRGxWJ7s7anw" #in the quotes, put your API key 
api_secret <- "unIQAzDqTE4kShlyYyDrJQtYLNpStTuh3Kd6a7gHhrivTKefYI" #in the quotes, put your API secret token
token <- "960655320589717508-66yKjwXLV5gY98a3eH9Y0QckKvBZ8lN" #in the quotes, put your token token_secret 
token_secret <- "0u54LEx7Q3m40rs5UF1vSHva7SlRSOycNcn0e6o115d4a" #in the quotes, put your token secret 
setup_twitter_oauth(api_key, api_secret, token, token_secret)
tweets2 <- searchTwitter("trump", n = 2500, lang = "en",since = "2018-03-25",until = "2018-03-30")
twdf <- twListToDF(tweets2)
tweets<-twdf$text
tweets_df<-as.data.frame(tweets)
write.table(tweets_df,"tweets_1_week.csv")