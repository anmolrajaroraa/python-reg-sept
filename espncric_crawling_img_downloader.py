Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from urllib.request as *
SyntaxError: invalid syntax
>>> from urllib.request import *
>>> from bs4 import BeautifulSoup as bs
>>> res = urlopen('https://www.espncricinfo.com/')
>>> html = bs(res)
>>> images = html.find_all('img')
>>> len(images)
65
>>> imgSrcs = []
>>> for i in range(len(images)):
	if str(images[i]).count(' src') == 1:
		imgSrcs.append(images[i]['src'])
	elif str(images[i]).count('data-default-src') == 1:
		imgSrcs.append(images[i]['data-default-src'])

		
>>> len(imgSrcs)
64
>>> imgSrcs[0]
'https://a2.espncdn.com/combiner/i?img=%2Fredesign%2Fassets%2Fimg%2Ficons%2FESPN%2Dicon%2Dcricinfo%2Dapp.png&w=80&h=80&scale=crop&cquality=40&location=origin'
>>> type(imgSrcs[0])
<class 'str'>
>>> 
>>> for i in range(len(imgSrcs)):
	urlretrieve(imgSrcs[i], 'espncric/img_{}.{}'.format(i+1, imgSrcs[i].rpartition('.')[-1][0:3]))

	
('espncric/img_1.png', <http.client.HTTPMessage object at 0x108cc1c50>)
('espncric/img_2.png', <http.client.HTTPMessage object at 0x108cc1e48>)
('espncric/img_3.png', <http.client.HTTPMessage object at 0x108cc1b38>)
('espncric/img_4.png', <http.client.HTTPMessage object at 0x108cc1978>)
('espncric/img_5.png', <http.client.HTTPMessage object at 0x108cc1cc0>)
('espncric/img_6.png', <http.client.HTTPMessage object at 0x108cc1eb8>)
('espncric/img_7.png', <http.client.HTTPMessage object at 0x108cc1f28>)
('espncric/img_8.png', <http.client.HTTPMessage object at 0x108cc1d68>)
('espncric/img_9.png', <http.client.HTTPMessage object at 0x108cc18d0>)
('espncric/img_10.png', <http.client.HTTPMessage object at 0x108cc1780>)
('espncric/img_11.png', <http.client.HTTPMessage object at 0x108cc1eb8>)
('espncric/img_12.png', <http.client.HTTPMessage object at 0x108cc1b00>)
('espncric/img_13.png', <http.client.HTTPMessage object at 0x108cc1e80>)
('espncric/img_14.png', <http.client.HTTPMessage object at 0x108cc1a20>)
('espncric/img_15.png', <http.client.HTTPMessage object at 0x108cc1278>)
('espncric/img_16.jpg', <http.client.HTTPMessage object at 0x108cc1da0>)
('espncric/img_17.jpg', <http.client.HTTPMessage object at 0x108cc1eb8>)
('espncric/img_18.jpg', <http.client.HTTPMessage object at 0x108cc1cf8>)
('espncric/img_19.jpg', <http.client.HTTPMessage object at 0x108cc1908>)
('espncric/img_20.jpg', <http.client.HTTPMessage object at 0x108cc1b38>)
('espncric/img_21.jpg', <http.client.HTTPMessage object at 0x108cc1c18>)
('espncric/img_22.jpg', <http.client.HTTPMessage object at 0x108cc1c88>)
('espncric/img_23.jpg', <http.client.HTTPMessage object at 0x108cc1b00>)
('espncric/img_24.jpg', <http.client.HTTPMessage object at 0x108cc1a20>)
('espncric/img_25.jpg', <http.client.HTTPMessage object at 0x108aa0128>)
('espncric/img_26.jpg', <http.client.HTTPMessage object at 0x108aa0080>)
('espncric/img_27.jpg', <http.client.HTTPMessage object at 0x108cc1978>)
('espncric/img_28.jpg', <http.client.HTTPMessage object at 0x108cc1cc0>)
('espncric/img_29.jpg', <http.client.HTTPMessage object at 0x108cc1780>)
('espncric/img_30.jpg', <http.client.HTTPMessage object at 0x108cc1c88>)
('espncric/img_31.jpg', <http.client.HTTPMessage object at 0x108cc1eb8>)
('espncric/img_32.jpg', <http.client.HTTPMessage object at 0x108cc1da0>)
('espncric/img_33.jpg', <http.client.HTTPMessage object at 0x108cc1b00>)
('espncric/img_34.jpg', <http.client.HTTPMessage object at 0x108cc1ba8>)
('espncric/img_35.jpg', <http.client.HTTPMessage object at 0x108cc1c88>)
('espncric/img_36.jpg', <http.client.HTTPMessage object at 0x108cc1e80>)
('espncric/img_37.jpg', <http.client.HTTPMessage object at 0x108cc18d0>)
('espncric/img_38.jpg', <http.client.HTTPMessage object at 0x108cc1978>)
('espncric/img_39.jpg', <http.client.HTTPMessage object at 0x108cc1ac8>)
('espncric/img_40.jpg', <http.client.HTTPMessage object at 0x108cc1ba8>)
('espncric/img_41.png', <http.client.HTTPMessage object at 0x108cc1780>)
('espncric/img_42.jpg', <http.client.HTTPMessage object at 0x108cc1fd0>)
('espncric/img_43.jpg', <http.client.HTTPMessage object at 0x108cc1b70>)
('espncric/img_44.jpg', <http.client.HTTPMessage object at 0x108cc1b00>)
('espncric/img_45.jpg', <http.client.HTTPMessage object at 0x108aa0198>)
('espncric/img_46.jpg', <http.client.HTTPMessage object at 0x108aa0390>)
('espncric/img_47.jpg', <http.client.HTTPMessage object at 0x108cc1908>)
('espncric/img_48.jpg', <http.client.HTTPMessage object at 0x108cc1c18>)
('espncric/img_49.png', <http.client.HTTPMessage object at 0x108cc1940>)
('espncric/img_50.png', <http.client.HTTPMessage object at 0x108cc1c88>)
('espncric/img_51.png', <http.client.HTTPMessage object at 0x108cc1eb8>)
('espncric/img_52.png', <http.client.HTTPMessage object at 0x108cc18d0>)
('espncric/img_53.png', <http.client.HTTPMessage object at 0x108cc1c50>)
('espncric/img_54.png', <http.client.HTTPMessage object at 0x108cc1ac8>)
('espncric/img_55.png', <http.client.HTTPMessage object at 0x108cc1b00>)
('espncric/img_56.png', <http.client.HTTPMessage object at 0x108cc1cc0>)
('espncric/img_57.png', <http.client.HTTPMessage object at 0x108cc1828>)
('espncric/img_58.png', <http.client.HTTPMessage object at 0x108cc1780>)
('espncric/img_59.png', <http.client.HTTPMessage object at 0x108cc1d30>)
('espncric/img_60.png', <http.client.HTTPMessage object at 0x108cc1be0>)
('espncric/img_61.png', <http.client.HTTPMessage object at 0x108cc1d68>)
('espncric/img_62.png', <http.client.HTTPMessage object at 0x108cc19e8>)
('espncric/img_63.png', <http.client.HTTPMessage object at 0x108cc1780>)
('espncric/img_64.png', <http.client.HTTPMessage object at 0x108cc1f60>)
>>> 
