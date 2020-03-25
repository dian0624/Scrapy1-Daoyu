# Scrapy1-Daoyu
技術點:
1. Scrapy框架

  1. 找出網頁URL規律以及，爬取多頁面中的主播圖片連結、主播名稱與所在城市資訊。
  2. 設置**scrapy的圖片管道類定義繼承於ImagesPipeline自己的class**，用於向圖片連接發請求，保存響應在**setting中的IMAGES_STORE路徑**，藉此保存圖片於本地。

---------------------------------------------------------------

功能說明:

使用Scrapy框架爬取鬥魚直播網頁，抓取直播主姓名與直播所在城市，
以及設置圖片管道將直播預覽圖抓取到Images資料夾中。

![image](https://github.com/dian0624/Scrapy1-Daoyu/blob/master/6464.jpg)   
