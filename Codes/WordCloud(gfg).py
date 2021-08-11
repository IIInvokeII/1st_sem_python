from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
  
data= """
Traffic arrangements for Modi-Xi Jinping summit in Mamallapuram
Chennai police have made changes in the traffic in view of the summit between the two leaders.
The Hindu
1 hour ago
To Chinese President Xi Jinping's Remark On Kashmir, India's Reply
Hours after Chinese President Xi Jinping told Pakistan Prime Minister Imran Khan that he was keenly watching the Kashmir situation, India reiterated on ...
NDTV News
3 hours ago
Xi Jinping Says He's Watching Kashmir, Will Back Pak On Core Interests: Report
Chinese President Xi Jinping said on Wednesday he was watching the situation in Kashmir and would support Pakistan in issues related to its core interests, the ...
NDTV News
Yesterday
Modi and Xi’s Informal Summits Can Only ‘Manage Ties’. What’s The Big Picture for India and China...
Informal summits have now become the preferred modus operandi when it comes to meetings between India and China. From Sabarmati to Wuhan and now ...
News18
30 minutes ago
Opinion
India-China summit: An opportunity to reset ties | HT editorial
There is little doubt that the strategic guidance which emerged from the first India-China informal summit at Wuhan last year was a key factor in putting bilateral ...
Hindustan Times
Yesterday
Opinion
Thousands of tourists and pilgrims from other states had to leave Jammu and Kashmir early August.
Jammu And Kashmir Reopens To Tourists After 2 Months, All Help Assured
Jammu and Kashmir has been reopened to tourists from today, more than two months after the government asked tourists and pilgrims to leave the state before it ...
NDTV News
2 hours ago
""" 
  
comment_words = ' '
stopwords = set(STOPWORDS) 
tokens = data.split() 
for words in tokens: 
        comment_words = comment_words + words + ' '

wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(comment_words) 
  
# plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.show()
