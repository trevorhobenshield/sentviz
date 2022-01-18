# Sentiment Visualization

## Query-Based Sentiment Visualization of Tweets Over Time
The examples use a RoBERTa-based sentiment classification model trained on twitter. Inference is done on data collected from the `tweepy` api.

![histogram](images/img_iamjhud_hist.png?raw=true "Histogram")
![Sentiment-coloured dataframe](images/img_iamjhud_df.png?raw=true "Sentiment-coloured dataframe")
![line plot (cumulative)](images/img_iamjhud_line.png?raw=true "Cumulative line plot")

## Query-Based Sentiment Visualization of Aggregated Youtube Transcripts
The examples use a RoBERTa-based sentiment classification model. Inference is done on data collected from `youtube-transcript-api`. The user provides a list of youtube URLs, and the transcripts are combined and saved. The user can then query the transcripts for keywords and view the sentiment associated with that keyword. It is also possible to adjust the text-segments window size within the transcript to allow for more context.

