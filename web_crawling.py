Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from urllib import request as req
>>> from bs4 import BeautifulSoup as bs
>>> res = req.urlopen('https://flipkart.com')
>>> html = bs
>>> 
>>> html = bs(res)
>>> html

>>> type(html)
<class 'bs4.BeautifulSoup'>
>>> html.find('div', class_ = 'iUmrbN')
<div class="iUmrbN">Dress Materials</div>
>>> res = req.urlopen('https://flipkart.com')
>>> html = bs(res)
>>> html.find('div', class_ = 'iUmrbN')
<div class="iUmrbN">Top Selling Brands!</div>
>>> html.find('h2', class_ = 'puxlXr')
<h2 class="puxlXr">Deals of the Day</h2>
>>> html.find_all('h2', class_ = 'puxlXr')
[<h2 class="puxlXr">Deals of the Day</h2>, <h2 class="puxlXr">Fashion for Travel Lovers</h2>]
>>> html.find_all('h2', class_ = 'puxlXr')[1]
<h2 class="puxlXr">Fashion for Travel Lovers</h2>
>>> res = req.urlopen('https://flipkart.com')
>>> html = bs(res)
>>> html.find_all('h2', class_ = 'puxlXr')
[<h2 class="puxlXr">Deals of the Day</h2>, <h2 class="puxlXr">Best of Electronic Devices</h2>]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> res = req.urlopen('https://www.flipkart.com/watches/pr?sid=r18&marketplace=FLIPKART&p%5B%5D=facets.ideal_for%255B%255D%3DWomen&p%5B%5D=facets.ideal_for%255B%255D%3DMen&p%5B%5D=facets.ideal_for%255B%255D%3DMen%2B%2526%2BWomen&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&offer=nb:mp:097776b004&fm=neo%2Fmerchandising&iid=M_d6f2146b-2435-4347-86c6-3bf505d91bba_2.UZTZQGNM6QYN&ppt=hp&ppn=hp&ssid=2wageykb340000001570444188090&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_1_2.dealCard.OMU_UZTZQGNM6QYN_2&otracker1=hp_omu_SECTIONED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_1_NA_view-all_2&cid=UZTZQGNM6QYN')
>>> html = bs(res)
>>> html.find('div', class_ = '_2B_pmu')
<div class="_2B_pmu">Timebre</div>
>>> html.find('a', class_ = '_2mylT6')
<a class="_2mylT6" href="/timebre-blk765-apple-burst-analog-watch-men/p/itmf3zhbhzrzyrnu?pid=WATEX8CFGEVDG7RZ&amp;lid=LSTWATEX8CFGEVDG7RZARBXKO&amp;marketplace=FLIPKART&amp;srno=b_1_1&amp;otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_1_2.dealCard.OMU_UZTZQGNM6QYN_2&amp;otracker1=hp_omu_SECTIONED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_1_NA_view-all_2&amp;fm=organic&amp;iid=en_7BjHUE1HZbq%2FeB%2Faooc3woAQIWKtOw%2BIGdnWhrIJFEOzvEx89zNc1AoBggUrDMnaryXI1JfKTFB6a4a766MNOg%3D%3D&amp;ssid=4gwqku6dds0000001570444358098" rel="noopener noreferrer" target="_blank" title="BLK765 Apple Burst Analog Watch  - For Men">BLK765 Apple Burst Analog Watch  - For Men</a>
>>> html.find('a', class_ = '_2mylT6').text
'BLK765 Apple Burst Analog Watch  - For Men'
>>> html.find('div', class_ = '_1vC4OE')
<div class="_1vC4OE">₹189</div>
>>> 
>>> 
>>> 
>>> 
>>> watch = html.find('div', class_='IIdQZO')
>>> watch.find('div', class_ = '_2B_pmu').text
'Timebre'
>>> watch.find('a', class_ = '_2mylT6').text
'BLK765 Apple Burst Analog Watch  - For Men'
>>> watch.find('div', class_ = '_1vC4OE').text
'₹189'
>>> 
>>> 
>>> watches = html.find_all('div', class_='IIdQZO')
>>> len(watches)
40
>>> for watch in watches:
	print(watch.find('div', class_ = '_2B_pmu').text, watch.find('a', class_ = '_2mylT6').text, watch.find('div', class_ = '_1vC4OE').text)

	
Timebre BLK765 Apple Burst Analog Watch  - For Men ₹189
Fogg 2097-BK Black Day and Date Unique New Analog Watch  - F... ₹329
Lois Caron LCS-8075 BLUE DIAL DAY & DATE FUNCTIONING Analog Watch ... ₹312
Foxter Perfect Multicolor Leather Strap Combo Pack of 4 Analog... ₹399
LimeStone LS2804 All Black Mesh Strap Day and Date Functioning Qu... ₹331
Fogg 2038-WH Day and Date Analog Watch  - For Men ₹322
Fogg 1164-BR Brown Day and Date Unique New Analog Watch  - F... ₹322
Lois Caron LCS-8049 BLACK DIAL DAY & DATE FUNCTIONING Analog Watch... ₹331
Fogg 2038-BL Day and Date Analog Watch  - For Men ₹322
Buccachi B-GR5046-BWH-CH White & Blue Dial Day & Date Functionin... ₹312
LimeStone LS2745 Wood Coat Avatar~ Day and Date Display Analog Wa... ₹312
LimeStone LS2727 Avatar Day and Date Functioning Crocodile Strap ... ₹312
Carson CR8063 DayAndDate Functioning Analog Watch  - For Men ₹312
Fogg 1186-BK Black Day and Date Unique New Analog Watch  - F... ₹329
Rizzly Festive Way Farer Combo Designer Series Analog Watch  -... ₹474
Fogg 2104-GL ION Gold Platted Day & Date Analog Watch  - For... ₹499
LimeStone LS2845 Day and Date Functioning Tan Strap Quartz Analog... ₹312
Fogg 4054-PK Pink Day and Date Analog Watch  - For Women ₹331
Foxter 428-429-438 New Best Artist Designer Combo Watch For me... ₹499
Armado AR-A1 A2 A3 STYLISH COMBO OF 3 Analog Watch  - For Men ₹379
Fogg 2058-BK Printed Black Day and Date Analog Watch  - For ... ₹322
Fogg 2058-WH Printed White Day and Date Analog Watch  - For ... ₹322
LimeStone LS2803 All Black Mesh Strap Day and Date Functioning Qu... ₹331
ACNOS Slim And White Dial Blue&White Strep Stylish New Profes... ₹277
Rizzly Exclusive Smoky Grey Analog Watch  - For Men ₹284
Daniel Jubile Designer New Collection Black 21st century RADOO Analog... ₹236
LimeStone LS2842 All Black Mesh Strap Day and Date Functioning Wa... ₹331
Lois Caron LCS-8404 ORIGINAL GOLD PLATED DAY & DATE FUNCTIONING An... ₹569
Lois Caron LCS-8074 WHITE DIAL DAY & DATE FUNCTIONING Analog Watch... ₹331
Xtreme XM-GR037-BKBK AWESOME BLACK DIAL Analog Watch  - For Me... ₹331
Abrexo Abx8010-Gents Exclusive (Casual+PartyWear+Formal) Desig... ₹398
Daniel Jubile Design Steel Silver Black 21st century 2019 Unique Desi... ₹217
Skmei blue22557 SKMEI 1155 LED And Pointer Display 50M Multif... ₹408
Buccachi B-G5045-BK-BK Black Dial Special Diamond Cute Glass Wri... ₹206
Daniel Jubile Designer New Collection Silver 21st century RADOO Analo... ₹236
Buccachi B-GR5046-SLBL-CH Silver & Blue Dial Day & Date Function... ₹293
Fogg 4049-BK Elegant Analog Watch  - For Women ₹312
Fogg 2074-BK Black Day And Date Analog Watch  - For Men ₹296
LimeStone LS2741 The Stud Day and Date Tan Strap Analog Analog Wa... ₹312
Lois Caron LCS-8163 BLACK DIAL DAY & DATE FUNCTIONING Analog Watch... ₹314
>>> res = req.urlopen('https://www.flipkart.com/bags-wallets-belts/pr?sid=reh&marketplace=FLIPKART&p%5B%5D=facets.ideal_for%255B%255D%3DMen%2B%2526%2BWomen&sort=popularity&p%5B%5D=facets.ideal_for%255B%255D%3DMen&p%5B%5D=facets.ideal_for%255B%255D%3DBoys&p%5B%5D=facets.ideal_for%255B%255D%3DMen%2527s&p%5B%5D=facets.ideal_for%255B%255D%3DBoys%2B%2526%2BGirls&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&offer=nb:mp:09b65b7d05&fm=neo%2Fmerchandising&iid=M_2375efe8-a544-4418-94cd-c9600809d4c4_2.VMQCRRZPKRYR&ppt=hp&ppn=hp&ssid=mjn4gfk8cg0000001570444218321&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_4_2.dealCard.OMU_VMQCRRZPKRYR_2&otracker1=hp_omu_SECTIONED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_4_NA_view-all_2&cid=VMQCRRZPKRYR')
>>> html = bs(res)
>>> watches = html.find_all('div', class_='IIdQZO')
>>> bags = html.find_all('div', class_='IIdQZO')
>>> for bag in bags:
	print(bag.find('div', class_ = '_2B_pmu').text, bag.find('a', class_ = '_2mylT6').text, bag.find('div', class_ = '_1vC4OE').text)

	
Novex 15.6 Laptop Overnighter Cabin Luggage - 16 inch ₹2,469
Nasher Miles Rome Expander| Hard-Side| Luggage Set of 3|Maroon Troll... ₹9,974
ZORO Men Evening, Party, Formal, Casual Black Artificial Lea... ₹299
TnW Men Casual, Formal Tan Artificial Leather Wallet ₹230
Wildcraft Daredevil 43 L Laptop Backpack ₹1,303
Hidelink Men Casual Tan Genuine Leather Wallet ₹512
Safari Mosaic Check-in Luggage - 26 inch ₹2,659
SnW Enterprises Men Casual Tan Artificial Leather Wallet ₹227
Safari STAR 65 4W BLACK Expandable Check-in Luggage - 26 inch ₹2,741
Wildcraft Spacy_Mel 30 L Backpack ₹1,099
Safari Mosaic Cabin Luggage - 22 inch ₹2,089
American Tourister TURF CASUAL BACKPACK 02-NAVY 33 L Backpack ₹1,502
Hidelink Men Formal Brown Genuine Leather Wallet ₹513
Nasher Miles Texas soft-sided Polyester Cabin Luggage Purple 20 inch... ₹2,849
Variety Men Casual Brown Artificial Leather Belt ₹219
Wildcraft Daredevil 43 L Laptop Backpack ₹1,448
Safari Mosaic Check-in Luggage - 26 inch ₹2,659
Safari Mosaic Cabin Luggage - 22 inch ₹2,089
Skybags 26 L Laptop Backpack ₹899
Hidelink Men Brown Genuine Leather Wallet ₹531
Safari Mosaic Cabin Luggage - 22 inch ₹2,089
Aristocrat PHOTON STROLLY 55 360 MAB Cabin Luggage - 22 inch ₹1,994
Safari Mosaic Cabin Luggage - 22 inch ₹2,089
Tommy Hilfiger TYSON 23.552 L Laptop Backpack ₹1,069
Metronaut Basic 23 L Laptop Backpack ₹458
American Tourister TURF CASUAL BACKPACK 03-GREY 33 L Backpack ₹1,376
Aristocrat PHOTON STROLLY 55 360 JBK Cabin Luggage - 22 inch ₹1,994
American Tourister EDEN BACKPACK 01 - TEAL 31 L Backpack ₹1,199
Safari STAR 55 4W BLACK Expandable Cabin Luggage - 22 inch ₹2,089
Ox Men Casual Black Genuine Leather Wallet ₹490
American Tourister TURF CASUAL BACKPACK 02-BLACK 33 L Backpack ₹1,376
Hidelink Men Formal Brown Genuine Leather Wallet ₹513
American Tourister JET BACKPACK 02-BLUE 30 L Backpack ₹1,329
ox Men Black Genuine Leather Wallet ₹425
Hidelink Men Casual Brown Genuine Leather Wallet ₹531
Gear VINTAGE2 ANTI THEFT FAUX LEATHER 28 L Laptop Backpack ₹1,045
Safari Moove USB Backpack 30 L Medium Backpack ₹849
American Tourister Mist Sch Bag 32.5 L Backpack ₹988
Skybags Teckie 01 Laptop Backpack Grey 42 L Laptop Backpack ₹1,804
Nasher Miles Zurich Black Abs Hardsided Set Of 2 Luggage Set(55 & 65... ₹6,126
>>> 
>>> 
>>> 
>>> 
