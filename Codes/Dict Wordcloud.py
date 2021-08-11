data= """ 
Maharashtra crisis: SC asks Centre to produce governor's letters inviting BJP to form govt, issues notice
India News: In the special hearing on a holiday, the SC also issued notices to the Centre, Maharashtra govt on the petition filed by Shiv Sena-NCP-Cong .
NCP Says 50 of Its 54 MLAs Back in Sharad Pawar's Camp after Nephew Ajit Takes over as Deputy CM
New Delhi: In a stunning turn of events in Maharashtra, BJP's Devendra Fadnavis on Saturday returned as chief minister propped up by Ajit Pawar 
Maharashtra Government formation: Here’s how BJP pulled it off
BJP sources said it was bitterness with the Shiv Sena that drove the party to reach out to Ajit, NCP's legislative party leader.
A softer Shiv Sena and other positives of the new politics in Maharashtra
We tend to see Sena as hankering for a share of power that is disproportionate to its earning in the latest Assembly election, which, of course, isn't far from truth.
Maharashtra 'Pawar' play: Game of Thrones in the age of BJP 2.0
While the BJP has managed to upset the momentum of Shiv Sena, Congress and NCP, how BJP's bet will play out is a known unknown and Saturday's events
Never had desire to enter politics: PM Modi in Mann ki Baat
India News: "I never had the desire to enter politics, but now that I am a part of it I give my best on how to work for the people," Prime Minister Narendra Modi.
Mann Ki Baat Highlights: Post Ayodhya Verdict, Indians Proved National Interest Biggest For Them, Says PM Modi
Prime Minister Narendra Modi is addressed the 59th edition of his monthly radio programme ''Mann Ki Baat''. The Prime Minister had asked people to share 
Increase in Wind Speed Improves Air Quality in Delhi, Pollution Expected to Rise from Monday
The overall air quality index in the city read at 254 at 9.45 am, down from 312 at 4 pm on Saturday.
In charts: Did Delhi’s odd-even vehicle plan help improve its air pollution problem?
Research shows that the scheme, along with suitable weather conditions, led to a marginal improvement in Delhi's air quality in 2016.
In 10 Steps, Here’s How Modi and Shah Managed the Murder of Democracy in Maharashtra
The two leaders knew they could not afford to let the Maharashtra government out of their hands and had prepared the ground, from day one, to ensure the BJP 
‘Jiska Governor Uski Sarkar’: Akhilesh Yadav on Ongoing Maharashtra Power Tussle
The Shiv Sena, NCP and Congress on Saturday filed a petition in the Supreme Court against the 'arbitrary and malafide actions/decisions' of Maharashtra 
Hong Kong votes in election seen as referendum on protests
HONG KONG : Long lines formed outside Hong Kong polling stations Sunday in elections that have become a barometer of public support for anti-government 
Maha tussle: Theories why nephew broke with uncle
India News: No one, except for Ajit Pawar himself and those in his innermost circle, can tell for sure why he revolted against his uncle Sharad and joined forces
15 Memes to Summarise the Collective Shock of Indians After Maharashtra’s Epic Political Twist
However, until last night we knew it would be Uddhav Thackeray who would be sworn in as the new CM of the State
"""
#String to generate wordcloud with

dic={}
tokens=data.split()
dic=dic.fromkeys(tokens,0)
for k in dic:
    dic[k]=tokens.count(k) #populating dictionary

stopwords="""a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,
because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,for,from,
get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,it,its,just,least,let,like,
likely,may,me,might,most,must,my,neither,no,nor,not,of,off,often,on,only,or,other,our,own,rather,
said,say,says,she,should,since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,
too,twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,
would,yet,you,your,min,mins,hour,hours,ago"""
sw=stopwords.split(",") #list for stopwords

dicc={}
import string
for k,v in dic.items():
    if k.lower() not in sw:
        if k.lower() not in string.punctuation:
            dicc.update({k:v}) #eliminating stopwords from dict

import matplotlib.pyplot as plt
from wordcloud import WordCloud

wc = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                min_font_size = 10).generate_from_frequencies(dicc) 
                      
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wc) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.show()
