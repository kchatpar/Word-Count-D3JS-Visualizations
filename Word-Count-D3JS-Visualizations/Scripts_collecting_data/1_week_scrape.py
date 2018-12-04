import bs4 as bs
import urllib.request
f = open('data2.txt','w')
urls = ['https://www.nytimes.com/2018/03/26/us/politics/trump-silent-stormy-daniels.html',
 'https://www.nytimes.com/2018/03/26/books/review/semitism-jonathan-weisman.html',
'https://www.nytimes.com/2018/03/25/opinion/donald-trump-war.html',
'https://www.nytimes.com/2018/03/26/opinion/bolton-trump-mustache.html',
'https://www.nytimes.com/2018/03/26/arts/television/stormy-daniels-interview-trump.html',
'https://www.nytimes.com/2018/03/25/us/politics/elliott-broidy-trump-access-circinus-lobbying.html',
'https://www.nytimes.com/2018/03/26/us/politics/trump-rob-porter.html',
'https://www.nytimes.com/2018/03/26/world/middleeast/iran-nuclear-letter.html',
'https://www.nytimes.com/2018/03/26/world/europe/trump-russia-diplomats-expulsion.html',
'https://www.nytimes.com/reuters/2018/03/26/us/politics/26reuters-usa-trump-tweet-factbox.html',
'https://www.nytimes.com/2018/03/27/us/politics/trump-giuseppe-cecchi-donors.html',
'https://www.nytimes.com/2018/03/28/us/politics/rick-gates-trump-campaign-russian-intelligence.html',
'https://www.nytimes.com/2018/03/28/us/politics/justice-department-carter-page-surveillance.html',
'https://www.nytimes.com/2018/03/28/us/politics/trump-second-amendment.html',
'https://www.nytimes.com/2018/03/28/opinion/trump-singapore.html',
'https://www.nytimes.com/2018/03/27/us/politics/trump-south-korea-trade-deal.html',
'https://www.nytimes.com/2018/03/27/opinion/trump-census-2020-citizenship.html',
'https://www.nytimes.com/2018/03/28/business/trump-china-world-trade.html'
'https://www.nytimes.com/2018/03/26/opinion/stormy-daniels-trump-60-minutes.html',
'https://www.nytimes.com/2018/03/27/opinion/congress-trump-omnibus.html',
'https://www.nytimes.com/2018/03/29/us/politics/trump-infrastructure-trade-deal-south-korea.html',
'https://www.nytimes.com/2018/03/28/us/politics/trump-roseanne-barr-ratings.html',
'https://www.nytimes.com/2018/03/29/us/politics/trump-amazon-taxes.html',
'https://www.nytimes.com/reuters/2018/03/29/business/29reuters-amazon-com-trump-whitehouse.html',
'https://www.nytimes.com/aponline/2018/03/29/us/ap-us-trump-businesses-lawsuit-lepage.html',
'https://www.nytimes.com/reuters/2018/03/29/arts/29reuters-television-roseanne.html',
'https://www.nytimes.com/aponline/2018/03/29/us/politics/ap-us-trump-biden.html',
'https://www.nytimes.com/aponline/2018/03/29/us/politics/ap-us-trump-medal-of-honor.html',
'https://www.nytimes.com/aponline/2018/03/29/us/politics/ap-us-trump-amazon.html',
'https://www.nytimes.com/aponline/2018/03/29/us/politics/ap-us-pentagon-the-wall.html',
'https://www.nytimes.com/2018/03/30/world/europe/russia-expels-diplomacy.html',
'https://www.nytimes.com/video/opinion/columnists/100000005824758/ann-coulter-says-president-trump-is-failing.html',
'https://www.nytimes.com/2018/03/30/world/middleeast/syria-us-coalition-deaths.html',
'https://www.nytimes.com/2018/03/30/technology/silicon-valley-trump.html',
'https://www.nytimes.com/2018/03/29/business/media/david-pecker-trump-saudi-arabia.html',
'https://www.nytimes.com/2018/03/30/opinion/ann-coulter-trump-former-trumpers.html',
'https://www.nytimes.com/2018/03/30/world/asia/donald-trump-north-korea-south.html',
'https://www.nytimes.com/2018/03/29/us/politics/trump-national-enquirer-david-pecker.html',
'https://www.nytimes.com/2018/03/30/business/economy/trade-nafta-union-pacific.html',
'https://www.nytimes.com/2018/03/29/business/media/roseanne-ratings-trump.html']


f = open('data2.txt','w')
for i in range(0,len(urls)):
    sauce = urllib.request.urlopen(urls[i]).read()
    soup = bs.BeautifulSoup(sauce,'lxml')
    for paragraph in soup.find_all('p'):
        f.write(paragraph.text)
f.close()

f = open('data2.txt','r')
d = f.read()
print(d)
