Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from urllib.request import *
>>> from bs4 import BeautifulSoup as bs
>>> response = urlopen('https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=0&as-type=HISTORY')
>>> html = bs(response)
>>> images = html.find_all('img')
>>> len(images)
101
>>> type(images)
<class 'bs4.element.ResultSet'>
>>> type(images[0])
<class 'bs4.element.Tag'>
>>> for image in images:
	print(image)

	
<img alt="Flipkart" class="_1e_EAo" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/flipkart-plus_4ee2f9.png" title="Flipkart" width="75"/>
<img src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/plus_b13a8b.png" width="10"/>
<img alt="BDS 2019" class="_232NW7 _2MPLm_"/>
<img alt="BDS 2019" class="_2VeolH _3I5S6S _20er9E" src="https://rukminim1.flixcart.com/flap/100/54/image/e2a2c4d6799e2709.jpg?q=50"/>
<img class="_2rIV_l" height="21" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/fa_8b4b59.png"/>
<img alt="Buying Guide" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/buying-guide-illustration_48642c.png"/>
<img alt="Redmi 8 (Onyx Black, 64 GB)" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img height="21" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/fa_8b4b59.png"/>
<img alt="Redmi Note 7S (Sapphire Blue, 64 GB)" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img height="21" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/fa_8b4b59.png"/>
<img alt="Redmi Note 7 Pro (Neptune Blue, 64 GB)" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img height="21" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/fa_8b4b59.png"/>
<img alt="Detel D1 Guru" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img height="21" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/fa_8b4b59.png"/>
<img alt="Redmi Note 7S (Sapphire Blue, 32 GB)" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img height="21" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/fa_8b4b59.png"/>
<img alt="Redmi 8 (Ruby Red, 64 GB)" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img height="21" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/fa_8b4b59.png"/>
<img alt="Redmi Note 7S (Onyx Black, 64 GB)" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img height="21" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/fa_8b4b59.png"/>
<img alt="Realme C2 (Diamond Ruby, 32 GB)" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img height="21" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/fa_8b4b59.png"/>
<img alt="Realme C2 (Diamond Sapphire, 32 GB)" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img height="21" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/fa_8b4b59.png"/>
<img alt="Realme C2 (Diamond Blue, 32 GB)" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img height="21" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/fa_8b4b59.png"/>
<img alt="Realme C2 (Diamond Black, 32 GB)" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img height="21" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/fa_8b4b59.png"/>
<img alt="Realme 5 (Crystal Purple, 128 GB)" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img height="21" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/fa_8b4b59.png"/>
<img alt="Realme 5 (Crystal Blue, 128 GB)" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img height="21" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/fa_8b4b59.png"/>
<img alt="GreenBerry Music G212" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img alt="Realme 5 (Crystal Purple, 32 GB)" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img height="21" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/fa_8b4b59.png"/>
<img alt="Realme 5 (Crystal Blue, 32 GB)" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img height="21" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/fa_8b4b59.png"/>
<img alt="Realme 5 (Crystal Blue, 64 GB)" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img height="21" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/fa_8b4b59.png"/>
<img alt="Realme 5 (Crystal Purple, 64 GB)" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img height="21" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/fa_8b4b59.png"/>
<img alt="Redmi Note 7 Pro (Space Black, 64 GB)" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img height="21" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/fa_8b4b59.png"/>
<img alt="Mymax M41" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img alt="Redmi 7A (Matte Blue, 16 GB)" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img height="21" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/fa_8b4b59.png"/>
<img alt="Realme C2 (Diamond Blue, 32 GB)" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img height="21" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/fa_8b4b59.png"/>
<img alt="Realme C2 (Diamond Black, 32 GB)" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img height="21" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/fa_8b4b59.png"/>
<img alt="Niamia Cad V" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img height="21" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/fa_8b4b59.png"/>
<img alt="Detel D1 Guru" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img alt="Redmi Note 7S (Sapphire Blue, 64 GB)" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img alt="Realme C2 (Diamond Blue, 32 GB)" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img alt="GreenBerry Music G212" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img alt="Realme C2 (Diamond Black, 32 GB)" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/>
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNSIgdmlld0JveD0iMCAwIDE2IDE1Ij4KICAgIDxkZWZzPgogICAgICAgIDxsaW5lYXJHcmFkaWVudCBpZD0iYSIgeDE9IjAlIiB4Mj0iODYuODc2JSIgeTE9IjAlIiB5Mj0iODAuMjAyJSI+CiAgICAgICAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiNGRkQ4MDAiLz4KICAgICAgICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjRkZBRjAwIi8+CiAgICAgICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDwvZGVmcz4KICAgIDxnIGZpbGw9Im5vbmUiIGZpbGwtcnVsZT0iZXZlbm9kZCI+CiAgICAgICAgPHBhdGggZD0iTS0yLTJoMjB2MjBILTJ6Ii8+CiAgICAgICAgPHBhdGggZmlsbD0idXJsKCNhKSIgZmlsbC1ydWxlPSJub256ZXJvIiBkPSJNMTUuOTMgNS42MTRoLTIuOTQ4VjQuMTRjMC0uODE4LS42NTUtMS40NzMtMS40NzMtMS40NzNIOC41NmMtLjgxNyAwLTEuNDczLjY1NS0xLjQ3MyAxLjQ3M3YxLjQ3NEg0LjE0Yy0uODE4IDAtMS40NjYuNjU2LTEuNDY2IDEuNDc0bC0uMDA3IDguMTA1YzAgLjgxOC42NTUgMS40NzQgMS40NzMgMS40NzRoMTEuNzljLjgxOCAwIDEuNDc0LS42NTYgMS40NzQtMS40NzRWNy4wODhjMC0uODE4LS42NTYtMS40NzQtMS40NzQtMS40NzR6bS00LjQyMSAwSDguNTZWNC4xNGgyLjk0OHYxLjQ3NHoiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0yIC0yKSIvPgogICAgPC9nPgo8L3N2Zz4K"/>
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNSIgaGVpZ2h0PSIxNSIgdmlld0JveD0iMCAwIDE1IDE1Ij4KICAgIDxkZWZzPgogICAgICAgIDxsaW5lYXJHcmFkaWVudCBpZD0iYSIgeDE9IjAlIiB4Mj0iODYuODc2JSIgeTE9IjAlIiB5Mj0iODAuMjAyJSI+CiAgICAgICAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiNGRkQ4MDAiLz4KICAgICAgICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjRkZBRjAwIi8+CiAgICAgICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDwvZGVmcz4KICAgIDxnIGZpbGw9Im5vbmUiIGZpbGwtcnVsZT0iZXZlbm9kZCI+CiAgICAgICAgPHBhdGggZD0iTS0zLTNoMjB2MjBILTN6Ii8+CiAgICAgICAgPHBhdGggZmlsbD0idXJsKCNhKSIgZmlsbC1ydWxlPSJub256ZXJvIiBkPSJNMTAuNDkyIDNDNi4zNTMgMyAzIDYuMzYgMyAxMC41YzAgNC4xNCAzLjM1MyA3LjUgNy40OTIgNy41QzE0LjY0IDE4IDE4IDE0LjY0IDE4IDEwLjUgMTggNi4zNiAxNC42NCAzIDEwLjQ5MiAzem0zLjE4IDEyTDEwLjUgMTMuMDg4IDcuMzI3IDE1bC44NC0zLjYwN0w1LjM3IDguOTdsMy42OS0uMzE1TDEwLjUgNS4yNWwxLjQ0IDMuMzk4IDMuNjkuMzE1LTIuNzk4IDIuNDIyLjg0IDMuNjE1eiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTMgLTMpIi8+CiAgICA8L2c+Cjwvc3ZnPgo="/>
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxOCIgaGVpZ2h0PSIxNyIgdmlld0JveD0iMCAwIDE4IDE3Ij4KICAgIDxkZWZzPgogICAgICAgIDxsaW5lYXJHcmFkaWVudCBpZD0iYSIgeDE9IjAlIiB4Mj0iODYuODc2JSIgeTE9IjAlIiB5Mj0iODAuMjAyJSI+CiAgICAgICAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiNGRkQ4MDAiLz4KICAgICAgICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjRkZBRjAwIi8+CiAgICAgICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDwvZGVmcz4KICAgIDxnIGZpbGw9Im5vbmUiIGZpbGwtcnVsZT0iZXZlbm9kZCI+CiAgICAgICAgPHBhdGggZD0iTS0xLTFoMjB2MjBILTF6Ii8+CiAgICAgICAgPHBhdGggZmlsbD0idXJsKCNhKSIgZmlsbC1ydWxlPSJub256ZXJvIiBkPSJNMTYuNjY3IDVIMTQuODVjLjA5Mi0uMjU4LjE1LS41NDIuMTUtLjgzM2EyLjQ5NyAyLjQ5NyAwIDAgMC00LjU4My0xLjM3NUwxMCAzLjM1bC0uNDE3LS41NjdBMi41MSAyLjUxIDAgMCAwIDcuNSAxLjY2N2EyLjQ5NyAyLjQ5NyAwIDAgMC0yLjUgMi41YzAgLjI5MS4wNTguNTc1LjE1LjgzM0gzLjMzM2MtLjkyNSAwLTEuNjU4Ljc0Mi0xLjY1OCAxLjY2N2wtLjAwOCA5LjE2NkExLjY2IDEuNjYgMCAwIDAgMy4zMzMgMTcuNWgxMy4zMzRhMS42NiAxLjY2IDAgMCAwIDEuNjY2LTEuNjY3VjYuNjY3QTEuNjYgMS42NiAwIDAgMCAxNi42NjcgNXptMCA2LjY2N0gzLjMzM3YtNWg0LjIzNEw1LjgzMyA5LjAyNWwxLjM1Ljk3NSAxLjk4NC0yLjdMMTAgNi4xNjdsLjgzMyAxLjEzMyAxLjk4NCAyLjcgMS4zNS0uOTc1LTEuNzM0LTIuMzU4aDQuMjM0djV6IiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMSAtMSkiLz4KICAgIDwvZz4KPC9zdmc+Cg=="/>
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNSIgaGVpZ2h0PSIxNSIgdmlld0JveD0iMCAwIDE1IDE1Ij4KICAgIDxkZWZzPgogICAgICAgIDxsaW5lYXJHcmFkaWVudCBpZD0iYSIgeDE9IjAlIiB4Mj0iODYuODc2JSIgeTE9IjAlIiB5Mj0iODAuMjAyJSI+CiAgICAgICAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiNGRkQ4MDAiLz4KICAgICAgICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjRkZBRjAwIi8+CiAgICAgICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDwvZGVmcz4KICAgIDxnIGZpbGw9Im5vbmUiIGZpbGwtcnVsZT0iZXZlbm9kZCI+CiAgICAgICAgPHBhdGggZD0iTS0yLTNoMjB2MjBILTJ6Ii8+CiAgICAgICAgPHBhdGggZmlsbD0idXJsKCNhKSIgZmlsbC1ydWxlPSJub256ZXJvIiBkPSJNOS41IDNDNS4zNiAzIDIgNi4zNiAyIDEwLjUgMiAxNC42NCA1LjM2IDE4IDkuNSAxOGM0LjE0IDAgNy41LTMuMzYgNy41LTcuNUMxNyA2LjM2IDEzLjY0IDMgOS41IDN6bS43NSAxMi43NWgtMS41di0xLjVoMS41djEuNXptMS41NTMtNS44MTNsLS42NzYuNjljLS41NC41NDgtLjg3Ny45OTgtLjg3NyAyLjEyM2gtMS41di0uMzc1YzAtLjgyNS4zMzgtMS41NzUuODc3LTIuMTIzbC45My0uOTQ1Yy4yNzgtLjI3LjQ0My0uNjQ1LjQ0My0xLjA1NyAwLS44MjUtLjY3NS0xLjUtMS41LTEuNVM4IDcuNDI1IDggOC4yNUg2LjVhMyAzIDAgMSAxIDYgMGMwIC42Ni0uMjcgMS4yNi0uNjk3IDEuNjg4eiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTIgLTMpIi8+CiAgICA8L2c+Cjwvc3ZnPgo="/>
<img src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/payment-method_2dd397.svg"/>
>>> for image in images:
	print(image.keys())

	
Traceback (most recent call last):
  File "<pyshell#13>", line 2, in <module>
    print(image.keys())
TypeError: 'NoneType' object is not callable
>>> for i in range(len(images)):
	if str(images[i]).count(" src") == 1:
		continue
	else:
		print(i)

		
2
>>> imgSrcs = []
>>> for image in images:
	if str(image).count(' src') == 1:
		imgSrcs.append(image['src'])
	else:
		print('not appended')

		
not appended
>>> len(imgSrcs)
100
>>> for src in imgSrcs:
	if src.startswith('//') or src.startswith('data'):
		continue
	else
	
SyntaxError: invalid syntax
>>> for src in imgSrcs:
	if src.startswith('//') or src.startswith('data'):
		continue
	else:
		print(src)

		
https://rukminim1.flixcart.com/flap/100/54/image/e2a2c4d6799e2709.jpg?q=50
>>> 
>>> for i in range(len(imgSrcs)):
	if imgSrcs[i].startswith('//'):
		urlretrieve('https:' + imgSrcs[i], 'flipkart-images/img_{}.{}'.format(i+1, imgSrcs[i].rpartition('.')[-1][0:3]))

		
('flipkart-images/img_1.png', <http.client.HTTPMessage object at 0x1094204e0>)
('flipkart-images/img_2.png', <http.client.HTTPMessage object at 0x1094206d8>)
('flipkart-images/img_4.png', <http.client.HTTPMessage object at 0x109420390>)
('flipkart-images/img_5.png', <http.client.HTTPMessage object at 0x1094201d0>)
('flipkart-images/img_6.svg', <http.client.HTTPMessage object at 0x1094205c0>)
('flipkart-images/img_8.png', <http.client.HTTPMessage object at 0x109420898>)
('flipkart-images/img_9.svg', <http.client.HTTPMessage object at 0x109420518>)
('flipkart-images/img_11.png', <http.client.HTTPMessage object at 0x109420908>)
('flipkart-images/img_12.svg', <http.client.HTTPMessage object at 0x1094205f8>)
('flipkart-images/img_14.png', <http.client.HTTPMessage object at 0x1094204e0>)
('flipkart-images/img_15.svg', <http.client.HTTPMessage object at 0x109420438>)
('flipkart-images/img_17.png', <http.client.HTTPMessage object at 0x1094208d0>)
('flipkart-images/img_18.svg', <http.client.HTTPMessage object at 0x109420278>)
('flipkart-images/img_20.png', <http.client.HTTPMessage object at 0x109420080>)
('flipkart-images/img_21.svg', <http.client.HTTPMessage object at 0x109420470>)
('flipkart-images/img_23.png', <http.client.HTTPMessage object at 0x1094207b8>)
('flipkart-images/img_24.svg', <http.client.HTTPMessage object at 0x109420668>)
('flipkart-images/img_26.png', <http.client.HTTPMessage object at 0x109420940>)
('flipkart-images/img_27.svg', <http.client.HTTPMessage object at 0x109420390>)
('flipkart-images/img_29.png', <http.client.HTTPMessage object at 0x109420828>)
('flipkart-images/img_30.svg', <http.client.HTTPMessage object at 0x1094205c0>)
('flipkart-images/img_32.png', <http.client.HTTPMessage object at 0x1094203c8>)
('flipkart-images/img_33.svg', <http.client.HTTPMessage object at 0x109420518>)
('flipkart-images/img_35.png', <http.client.HTTPMessage object at 0x1094206a0>)
('flipkart-images/img_36.svg', <http.client.HTTPMessage object at 0x1094205f8>)
('flipkart-images/img_38.png', <http.client.HTTPMessage object at 0x109420358>)
('flipkart-images/img_39.svg', <http.client.HTTPMessage object at 0x109420438>)
('flipkart-images/img_41.png', <http.client.HTTPMessage object at 0x1094207f0>)
('flipkart-images/img_42.svg', <http.client.HTTPMessage object at 0x109420278>)
('flipkart-images/img_44.png', <http.client.HTTPMessage object at 0x109420048>)
('flipkart-images/img_45.svg', <http.client.HTTPMessage object at 0x109420470>)
('flipkart-images/img_47.svg', <http.client.HTTPMessage object at 0x109420630>)
('flipkart-images/img_49.png', <http.client.HTTPMessage object at 0x109420668>)
('flipkart-images/img_50.svg', <http.client.HTTPMessage object at 0x109420160>)
('flipkart-images/img_52.png', <http.client.HTTPMessage object at 0x109420390>)
('flipkart-images/img_53.svg', <http.client.HTTPMessage object at 0x1094206a0>)
('flipkart-images/img_55.png', <http.client.HTTPMessage object at 0x1094208d0>)
('flipkart-images/img_56.svg', <http.client.HTTPMessage object at 0x109420358>)
('flipkart-images/img_58.png', <http.client.HTTPMessage object at 0x109420438>)
('flipkart-images/img_59.svg', <http.client.HTTPMessage object at 0x109420240>)
('flipkart-images/img_61.png', <http.client.HTTPMessage object at 0x1094207b8>)
('flipkart-images/img_62.svg', <http.client.HTTPMessage object at 0x1094206d8>)
('flipkart-images/img_64.svg', <http.client.HTTPMessage object at 0x109420940>)
('flipkart-images/img_66.png', <http.client.HTTPMessage object at 0x1094207f0>)
('flipkart-images/img_67.svg', <http.client.HTTPMessage object at 0x109420780>)
('flipkart-images/img_69.png', <http.client.HTTPMessage object at 0x109420048>)
('flipkart-images/img_70.svg', <http.client.HTTPMessage object at 0x109420390>)
('flipkart-images/img_72.png', <http.client.HTTPMessage object at 0x109420710>)
('flipkart-images/img_73.svg', <http.client.HTTPMessage object at 0x1094208d0>)
('flipkart-images/img_75.png', <http.client.HTTPMessage object at 0x1094205c0>)
('flipkart-images/img_76.svg', <http.client.HTTPMessage object at 0x109420080>)
('flipkart-images/img_80.svg', <http.client.HTTPMessage object at 0x109420518>)
('flipkart-images/img_84.svg', <http.client.HTTPMessage object at 0x109420588>)
('flipkart-images/img_88.svg', <http.client.HTTPMessage object at 0x109420278>)
('flipkart-images/img_92.svg', <http.client.HTTPMessage object at 0x109420438>)
('flipkart-images/img_100.svg', <http.client.HTTPMessage object at 0x109420630>)
>>> for src in imgSrcs:
	if src.startswith('https') or src.startswith('data'):
		print(src)

		
https://rukminim1.flixcart.com/flap/100/54/image/e2a2c4d6799e2709.jpg?q=50
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNSIgdmlld0JveD0iMCAwIDE2IDE1Ij4KICAgIDxkZWZzPgogICAgICAgIDxsaW5lYXJHcmFkaWVudCBpZD0iYSIgeDE9IjAlIiB4Mj0iODYuODc2JSIgeTE9IjAlIiB5Mj0iODAuMjAyJSI+CiAgICAgICAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiNGRkQ4MDAiLz4KICAgICAgICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjRkZBRjAwIi8+CiAgICAgICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDwvZGVmcz4KICAgIDxnIGZpbGw9Im5vbmUiIGZpbGwtcnVsZT0iZXZlbm9kZCI+CiAgICAgICAgPHBhdGggZD0iTS0yLTJoMjB2MjBILTJ6Ii8+CiAgICAgICAgPHBhdGggZmlsbD0idXJsKCNhKSIgZmlsbC1ydWxlPSJub256ZXJvIiBkPSJNMTUuOTMgNS42MTRoLTIuOTQ4VjQuMTRjMC0uODE4LS42NTUtMS40NzMtMS40NzMtMS40NzNIOC41NmMtLjgxNyAwLTEuNDczLjY1NS0xLjQ3MyAxLjQ3M3YxLjQ3NEg0LjE0Yy0uODE4IDAtMS40NjYuNjU2LTEuNDY2IDEuNDc0bC0uMDA3IDguMTA1YzAgLjgxOC42NTUgMS40NzQgMS40NzMgMS40NzRoMTEuNzljLjgxOCAwIDEuNDc0LS42NTYgMS40NzQtMS40NzRWNy4wODhjMC0uODE4LS42NTYtMS40NzQtMS40NzQtMS40NzR6bS00LjQyMSAwSDguNTZWNC4xNGgyLjk0OHYxLjQ3NHoiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0yIC0yKSIvPgogICAgPC9nPgo8L3N2Zz4K
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNSIgaGVpZ2h0PSIxNSIgdmlld0JveD0iMCAwIDE1IDE1Ij4KICAgIDxkZWZzPgogICAgICAgIDxsaW5lYXJHcmFkaWVudCBpZD0iYSIgeDE9IjAlIiB4Mj0iODYuODc2JSIgeTE9IjAlIiB5Mj0iODAuMjAyJSI+CiAgICAgICAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiNGRkQ4MDAiLz4KICAgICAgICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjRkZBRjAwIi8+CiAgICAgICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDwvZGVmcz4KICAgIDxnIGZpbGw9Im5vbmUiIGZpbGwtcnVsZT0iZXZlbm9kZCI+CiAgICAgICAgPHBhdGggZD0iTS0zLTNoMjB2MjBILTN6Ii8+CiAgICAgICAgPHBhdGggZmlsbD0idXJsKCNhKSIgZmlsbC1ydWxlPSJub256ZXJvIiBkPSJNMTAuNDkyIDNDNi4zNTMgMyAzIDYuMzYgMyAxMC41YzAgNC4xNCAzLjM1MyA3LjUgNy40OTIgNy41QzE0LjY0IDE4IDE4IDE0LjY0IDE4IDEwLjUgMTggNi4zNiAxNC42NCAzIDEwLjQ5MiAzem0zLjE4IDEyTDEwLjUgMTMuMDg4IDcuMzI3IDE1bC44NC0zLjYwN0w1LjM3IDguOTdsMy42OS0uMzE1TDEwLjUgNS4yNWwxLjQ0IDMuMzk4IDMuNjkuMzE1LTIuNzk4IDIuNDIyLjg0IDMuNjE1eiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTMgLTMpIi8+CiAgICA8L2c+Cjwvc3ZnPgo=
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxOCIgaGVpZ2h0PSIxNyIgdmlld0JveD0iMCAwIDE4IDE3Ij4KICAgIDxkZWZzPgogICAgICAgIDxsaW5lYXJHcmFkaWVudCBpZD0iYSIgeDE9IjAlIiB4Mj0iODYuODc2JSIgeTE9IjAlIiB5Mj0iODAuMjAyJSI+CiAgICAgICAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiNGRkQ4MDAiLz4KICAgICAgICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjRkZBRjAwIi8+CiAgICAgICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDwvZGVmcz4KICAgIDxnIGZpbGw9Im5vbmUiIGZpbGwtcnVsZT0iZXZlbm9kZCI+CiAgICAgICAgPHBhdGggZD0iTS0xLTFoMjB2MjBILTF6Ii8+CiAgICAgICAgPHBhdGggZmlsbD0idXJsKCNhKSIgZmlsbC1ydWxlPSJub256ZXJvIiBkPSJNMTYuNjY3IDVIMTQuODVjLjA5Mi0uMjU4LjE1LS41NDIuMTUtLjgzM2EyLjQ5NyAyLjQ5NyAwIDAgMC00LjU4My0xLjM3NUwxMCAzLjM1bC0uNDE3LS41NjdBMi41MSAyLjUxIDAgMCAwIDcuNSAxLjY2N2EyLjQ5NyAyLjQ5NyAwIDAgMC0yLjUgMi41YzAgLjI5MS4wNTguNTc1LjE1LjgzM0gzLjMzM2MtLjkyNSAwLTEuNjU4Ljc0Mi0xLjY1OCAxLjY2N2wtLjAwOCA5LjE2NkExLjY2IDEuNjYgMCAwIDAgMy4zMzMgMTcuNWgxMy4zMzRhMS42NiAxLjY2IDAgMCAwIDEuNjY2LTEuNjY3VjYuNjY3QTEuNjYgMS42NiAwIDAgMCAxNi42NjcgNXptMCA2LjY2N0gzLjMzM3YtNWg0LjIzNEw1LjgzMyA5LjAyNWwxLjM1Ljk3NSAxLjk4NC0yLjdMMTAgNi4xNjdsLjgzMyAxLjEzMyAxLjk4NCAyLjcgMS4zNS0uOTc1LTEuNzM0LTIuMzU4aDQuMjM0djV6IiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMSAtMSkiLz4KICAgIDwvZz4KPC9zdmc+Cg==
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNSIgaGVpZ2h0PSIxNSIgdmlld0JveD0iMCAwIDE1IDE1Ij4KICAgIDxkZWZzPgogICAgICAgIDxsaW5lYXJHcmFkaWVudCBpZD0iYSIgeDE9IjAlIiB4Mj0iODYuODc2JSIgeTE9IjAlIiB5Mj0iODAuMjAyJSI+CiAgICAgICAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiNGRkQ4MDAiLz4KICAgICAgICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjRkZBRjAwIi8+CiAgICAgICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDwvZGVmcz4KICAgIDxnIGZpbGw9Im5vbmUiIGZpbGwtcnVsZT0iZXZlbm9kZCI+CiAgICAgICAgPHBhdGggZD0iTS0yLTNoMjB2MjBILTJ6Ii8+CiAgICAgICAgPHBhdGggZmlsbD0idXJsKCNhKSIgZmlsbC1ydWxlPSJub256ZXJvIiBkPSJNOS41IDNDNS4zNiAzIDIgNi4zNiAyIDEwLjUgMiAxNC42NCA1LjM2IDE4IDkuNSAxOGM0LjE0IDAgNy41LTMuMzYgNy41LTcuNUMxNyA2LjM2IDEzLjY0IDMgOS41IDN6bS43NSAxMi43NWgtMS41di0xLjVoMS41djEuNXptMS41NTMtNS44MTNsLS42NzYuNjljLS41NC41NDgtLjg3Ny45OTgtLjg3NyAyLjEyM2gtMS41di0uMzc1YzAtLjgyNS4zMzgtMS41NzUuODc3LTIuMTIzbC45My0uOTQ1Yy4yNzgtLjI3LjQ0My0uNjQ1LjQ0My0xLjA1NyAwLS44MjUtLjY3NS0xLjUtMS41LTEuNVM4IDcuNDI1IDggOC4yNUg2LjVhMyAzIDAgMSAxIDYgMGMwIC42Ni0uMjcgMS4yNi0uNjk3IDEuNjg4eiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTIgLTMpIi8+CiAgICA8L2c+Cjwvc3ZnPgo=
>>> for src in imgSrcs:
	if src.startswith('https'):
		print(src)

		
https://rukminim1.flixcart.com/flap/100/54/image/e2a2c4d6799e2709.jpg?q=50
>>> response = urlopen('https://www.snapdeal.com/products/mobiles-mobile-phones/filters/Form_s~Smartphones')
>>> html = bs(response)
>>> images = html.find_all('img')
>>> len(images)
40
>>> for image in images:
	print(image)

	
<img class="lazy-load" data-src="https://i4.sdlcdn.com/img/platinum09/downloadappicon2ndsep.png"/>
<img class="notIeLogoHeader aspectRatioEqual sdLogo cur-pointer" height="28" src="https://i3.sdlcdn.com/img/snapdeal/darwin/logo/sdLatestLogo.svg" title="Snapdeal" width="132"/>
<img class="ieLogoHeader aspectRatioEqual sdLogo cur-pointer" height="28" title="Snapdeal" width="132"/>
<img class="lazy-load cartProductImg" data-src=""/>
<img class="hidden imgUser"/>
<img class="js_svgLoader" height="32" lazysrc="https://i2.sdlcdn.com/img/sdDarwinLoader.svg" onerror="this.src='https://i1.sdlcdn.com/img/revamp/cyclicLoader.gif'; this.onerror=null;" width="32"/>
<img class="js_svgLoader" height="32" lazysrc="https://i2.sdlcdn.com/img/sdDarwinLoader.svg" onerror="this.src='https://i1.sdlcdn.com/img/revamp/cyclicLoader.gif'; this.onerror=null;" width="32"/>
<img height="32" onerror="this.src='https://i1.sdlcdn.com/img/revamp/cyclicLoader.gif'; this.onerror=null;" src="https://i2.sdlcdn.com/img/sdDarwinLoader.svg" width="32"/>
<img alt="" src=""/>
<img alt="" class="p-img" src=""/>
<img alt="" src=""/>
<img alt="" class="p-img" src=""/>
<img alt="" src=""/>
<img alt="" class="p-img" src=""/>
<img alt="" src=""/>
<img alt="" class="p-img" src=""/>
<img alt="" src=""/>
<img alt="" class="p-img" src=""/>
<img class="js_svgLoader" lazysrc="https://i2.sdlcdn.com/img/sdDarwinLoader.svg" onerror="this.src='https://i1.sdlcdn.com/img/revamp/cyclicLoader.gif'; this.onerror=null;"/>
<img class="product-image" src="https://n3.sdlcdn.com/imgs/i/f/2/230X258_sharpened/Coolpad-MEGA-5-32GB-3-SDL583323628-1-475ba.jpeg" title="Coolpad MEGA 5 ( 32GB , 3 GB ) Champagne Gold"/>
<img class="product-image" src="https://n3.sdlcdn.com/imgs/i/r/f/230X258_sharpened/Gionee-Gionee-F9-32-MB-SDL229423401-1-d51cd.jpeg" title="Gionee Gionee F9 ( 32 MB , 3 GB ) Blue"/>
<img class="product-image" src="https://n1.sdlcdn.com/imgs/i/f/2/230X258_sharpened/Oppo-F11-Pro-CPH1969-128GB-SDL257164210-1-b1082.jpg" title="OPPO F11 Pro ( 128GB , 6 GB ) Black"/>
<img class="product-image" src="https://n3.sdlcdn.com/imgs/i/c/t/230X258_sharpened/b1-66ea3.jpeg" title="Micromax canvas infinity ( 32GB , 3 GB ) Black Steel"/>
<img class="product-image lazy-load" data-src="https://n1.sdlcdn.com/imgs/i/s/p/230X258_sharpened/LG-Spirit-8GB-1-GB-SDL502580603-1-978b7.jpg" title="LG Spirit ( 8GB , 1 GB ) Black"/>
<img class="product-image lazy-load" data-src="https://n3.sdlcdn.com/imgs/h/i/3/230X258_sharpened/Redmi-Note-5-Pro-Gold-SDL819330469-1-10e7a.jpeg" title="Redmi Note 5 Pro 4 ( 64GB , 4 GB ) Gold"/>
<img class="product-image lazy-load" data-src="https://n4.sdlcdn.com/imgs/i/f/x/230X258_sharpened/Lenovo-Black-a5-32GB-SDL922102439-1-a3b34.jpeg" title="Lenovo a5 ( 32GB , 3 GB ) Black"/>
<img class="product-image lazy-load" data-src="https://n3.sdlcdn.com/imgs/i/c/w/230X258_sharpened/1-6eed6.jpeg" title="Micromax B5 Infinity ( 16GB , 1 GB ) Rose Gold"/>
<img class="product-image lazy-load" data-src="https://n3.sdlcdn.com/imgs/i/h/u/230X258_sharpened/Vivo-Y15-64GB-4-GB-SDL436983995-1-b1189.jpeg" title="Vivo Y15 ( 64GB , 4 GB ) Aqua Blue"/>
<img class="product-image lazy-load" data-src="https://n2.sdlcdn.com/imgs/i/f/2/230X258_sharpened/Micromax-Bharat-2-Plus-8GB-SDL302807141-1-f4409.jpeg" title="Micromax Bharat 2 Plus ( 8GB , 1 GB ) Black"/>
<img class="product-image lazy-load" data-src="https://n4.sdlcdn.com/imgs/i/g/m/230X258_sharpened/Realme-C1-32GB-3-GB-SDL677041238-1-dbd8b.jpeg" title="Realme C1 ( 32GB , 3 GB ) Mirror Black"/>
<img class="product-image lazy-load" data-src="https://n1.sdlcdn.com/imgs/i/f/x/230X258_sharpened/Oppo-Green-F11-Pro-CPH1969-SDL632473908-1-52efe.jpeg" title="OPPO F11 Pro ( 128GB , 6 GB ) Green"/>
<img class="product-image lazy-load" data-src="https://n2.sdlcdn.com/imgs/i/p/y/230X258_sharpened/Gionee-F205-16GB-2-GB-SDL227471569-1-def48.jpeg" title="Gionee F205 ( 16GB , 2 GB ) Champagne Gold"/>
<img class="product-image lazy-load" data-src="https://n4.sdlcdn.com/imgs/i/f/2/230X258_sharpened/Lenovo-k9-32-MB-3-SDL445623207-1-b0267.jpeg" title="Lenovo k9 ( 32 GB , 3 GB ) Blue"/>
<img class="product-image lazy-load" data-src="https://n2.sdlcdn.com/imgs/i/e/r/230X258_sharpened/Realme-Black-2-Pro-64GB-SDL288686634-1-60575.jpeg" title="Realme 2 Pro ( 64GB , 4 GB ) Black"/>
<img class="product-image lazy-load" data-src="https://n3.sdlcdn.com/imgs/i/y/1/230X258_sharpened/ivoomi-iPro-16GB-1-GB-SDL169201525-1-7be3f.jpeg" title="ivoomi iPro+ ( 16GB , 1 GB ) Gold Platinum"/>
<img class="product-image lazy-load" data-src="https://n4.sdlcdn.com/imgs/i/e/p/230X258_sharpened/Vivo-Ocean-Blue-Vivo-1820-SDL362390693-1-2249f.jpeg" title="Vivo Y91i (32GB, 2GB) Ocean Blue"/>
<img class="product-image lazy-load" data-src="https://n2.sdlcdn.com/imgs/i/c/w/230X258_sharpened/Gionee-Black-F205-16GB-SDL935869853-2-b4874.jpeg" title="Gionee F205 ( 16GB , 2 GB ) Black"/>
<img class="product-image lazy-load" data-src="https://n3.sdlcdn.com/imgs/i/c/w/230X258_sharpened/1-6eed6.jpeg" title="Micromax B5 Infinity ( 16GB , 1 GB ) Rose Gold"/>
<img class="product-image lazy-load" data-src="https://n1.sdlcdn.com/imgs/i/p/s/230X258_sharpened/Vivo-Y90-16GB-2-GB-SDL212184275-1-b6ec1.jpeg" title="Vivo Y90 ( 16GB , 2 GB ) Gold"/>
<img class="js_svgLoader" lazysrc="https://i2.sdlcdn.com/img/sdDarwinLoader.svg" onerror="this.src='https://i1.sdlcdn.com/img/revamp/cyclicLoader.gif'; this.onerror=null;" style="top:17px;"/>
>>> imageSrcs = []
>>> for image in images:
	if str(image).count(' src') == 1:
		imageSrcs.append(image['src']) if image['src'].startswith('https') else print('image skipped')
	elif str(image).count('data-src') == 1:
		imageSrcs.append(image['data-src']) if image['data-src'].startswith('https') else print('image skipped')

		
image skipped
image skipped
image skipped
image skipped
image skipped
image skipped
image skipped
image skipped
image skipped
image skipped
image skipped
>>> len(imageSrcs)
23
>>> imageSrcs = []
>>> for image in images:
	if str(image).count(' src') == 1:
		imageSrcs.append(image['src']) if image['src'].startswith('https') else print(image['src'])
	elif str(image).count('data-src') == 1:
		imageSrcs.append(image['data-src']) if image['data-src'].startswith('https') else print(image['data-src'])

		











>>> len(imageSrcs)
23
>>> '''for i in range(len(imgSrcs)):
	urlretrieve(imgSrcs[i], 'flipkart-images/img_{}.{}'.format(i+1, imgSrcs[i].rpartition('.')[-1][0:3]))'''
"for i in range(len(imgSrcs)):\n\turlretrieve(imgSrcs[i], 'flipkart-images/img_{}.{}'.format(i+1, imgSrcs[i].rpartition('.')[-1][0:3]))"
>>> 
>>> 
>>> for src in imageSrcs:
	print(src)

	
https://i4.sdlcdn.com/img/platinum09/downloadappicon2ndsep.png
https://i3.sdlcdn.com/img/snapdeal/darwin/logo/sdLatestLogo.svg
https://i2.sdlcdn.com/img/sdDarwinLoader.svg
https://n3.sdlcdn.com/imgs/i/f/2/230X258_sharpened/Coolpad-MEGA-5-32GB-3-SDL583323628-1-475ba.jpeg
https://n3.sdlcdn.com/imgs/i/r/f/230X258_sharpened/Gionee-Gionee-F9-32-MB-SDL229423401-1-d51cd.jpeg
https://n1.sdlcdn.com/imgs/i/f/2/230X258_sharpened/Oppo-F11-Pro-CPH1969-128GB-SDL257164210-1-b1082.jpg
https://n3.sdlcdn.com/imgs/i/c/t/230X258_sharpened/b1-66ea3.jpeg
https://n1.sdlcdn.com/imgs/i/s/p/230X258_sharpened/LG-Spirit-8GB-1-GB-SDL502580603-1-978b7.jpg
https://n3.sdlcdn.com/imgs/h/i/3/230X258_sharpened/Redmi-Note-5-Pro-Gold-SDL819330469-1-10e7a.jpeg
https://n4.sdlcdn.com/imgs/i/f/x/230X258_sharpened/Lenovo-Black-a5-32GB-SDL922102439-1-a3b34.jpeg
https://n3.sdlcdn.com/imgs/i/c/w/230X258_sharpened/1-6eed6.jpeg
https://n3.sdlcdn.com/imgs/i/h/u/230X258_sharpened/Vivo-Y15-64GB-4-GB-SDL436983995-1-b1189.jpeg
https://n2.sdlcdn.com/imgs/i/f/2/230X258_sharpened/Micromax-Bharat-2-Plus-8GB-SDL302807141-1-f4409.jpeg
https://n4.sdlcdn.com/imgs/i/g/m/230X258_sharpened/Realme-C1-32GB-3-GB-SDL677041238-1-dbd8b.jpeg
https://n1.sdlcdn.com/imgs/i/f/x/230X258_sharpened/Oppo-Green-F11-Pro-CPH1969-SDL632473908-1-52efe.jpeg
https://n2.sdlcdn.com/imgs/i/p/y/230X258_sharpened/Gionee-F205-16GB-2-GB-SDL227471569-1-def48.jpeg
https://n4.sdlcdn.com/imgs/i/f/2/230X258_sharpened/Lenovo-k9-32-MB-3-SDL445623207-1-b0267.jpeg
https://n2.sdlcdn.com/imgs/i/e/r/230X258_sharpened/Realme-Black-2-Pro-64GB-SDL288686634-1-60575.jpeg
https://n3.sdlcdn.com/imgs/i/y/1/230X258_sharpened/ivoomi-iPro-16GB-1-GB-SDL169201525-1-7be3f.jpeg
https://n4.sdlcdn.com/imgs/i/e/p/230X258_sharpened/Vivo-Ocean-Blue-Vivo-1820-SDL362390693-1-2249f.jpeg
https://n2.sdlcdn.com/imgs/i/c/w/230X258_sharpened/Gionee-Black-F205-16GB-SDL935869853-2-b4874.jpeg
https://n3.sdlcdn.com/imgs/i/c/w/230X258_sharpened/1-6eed6.jpeg
https://n1.sdlcdn.com/imgs/i/p/s/230X258_sharpened/Vivo-Y90-16GB-2-GB-SDL212184275-1-b6ec1.jpeg
>>> for i in range(len(imgSrcs)):
	urlretrieve(imgSrcs[i], 'flipkart-images/img_{}.{}'.format(i+1, imgSrcs[i].rpartition('.')[-1]))

	
Traceback (most recent call last):
  File "<pyshell#73>", line 2, in <module>
    urlretrieve(imgSrcs[i], 'flipkart-images/img_{}.{}'.format(i+1, imgSrcs[i].rpartition('.')[-1]))
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib/request.py", line 247, in urlretrieve
    with contextlib.closing(urlopen(url, data)) as fp:
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib/request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib/request.py", line 510, in open
    req = Request(fullurl, data)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib/request.py", line 328, in __init__
    self.full_url = url
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib/request.py", line 354, in full_url
    self._parse()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib/request.py", line 383, in _parse
    raise ValueError("unknown url type: %r" % self.full_url)
ValueError: unknown url type: '//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/flipkart-plus_4ee2f9.png'
>>> for i in range(len(imageSrcs)):
	urlretrieve(imageSrcs[i], 'flipkart-images/img_{}.{}'.format(i+1, imageSrcs[i].rpartition('.')[-1]))

	
('flipkart-images/img_1.png', <http.client.HTTPMessage object at 0x109ea6400>)
('flipkart-images/img_2.svg', <http.client.HTTPMessage object at 0x109ea65f8>)
('flipkart-images/img_3.svg', <http.client.HTTPMessage object at 0x109ea6320>)
('flipkart-images/img_4.jpeg', <http.client.HTTPMessage object at 0x109ea6240>)
('flipkart-images/img_5.jpeg', <http.client.HTTPMessage object at 0x109ea67f0>)
('flipkart-images/img_6.jpg', <http.client.HTTPMessage object at 0x109ea6780>)
('flipkart-images/img_7.jpeg', <http.client.HTTPMessage object at 0x109ea6550>)
('flipkart-images/img_8.jpg', <http.client.HTTPMessage object at 0x109ea6160>)
('flipkart-images/img_9.jpeg', <http.client.HTTPMessage object at 0x109ea64e0>)
('flipkart-images/img_10.jpeg', <http.client.HTTPMessage object at 0x109ea6710>)
('flipkart-images/img_11.jpeg', <http.client.HTTPMessage object at 0x109ea67b8>)
('flipkart-images/img_12.jpeg', <http.client.HTTPMessage object at 0x109ea6630>)
('flipkart-images/img_13.jpeg', <http.client.HTTPMessage object at 0x109ea6780>)
('flipkart-images/img_14.jpeg', <http.client.HTTPMessage object at 0x109ea6978>)
('flipkart-images/img_15.jpeg', <http.client.HTTPMessage object at 0x109ea6630>)
('flipkart-images/img_16.jpeg', <http.client.HTTPMessage object at 0x109ea6320>)
('flipkart-images/img_17.jpeg', <http.client.HTTPMessage object at 0x109ea64e0>)
('flipkart-images/img_18.jpeg', <http.client.HTTPMessage object at 0x109ea6278>)
('flipkart-images/img_19.jpeg', <http.client.HTTPMessage object at 0x109ea6668>)
('flipkart-images/img_20.jpeg', <http.client.HTTPMessage object at 0x109ea65f8>)
('flipkart-images/img_21.jpeg', <http.client.HTTPMessage object at 0x109ea6908>)
('flipkart-images/img_22.jpeg', <http.client.HTTPMessage object at 0x109ea6588>)
('flipkart-images/img_23.jpeg', <http.client.HTTPMessage object at 0x109ea6748>)
>>> 
