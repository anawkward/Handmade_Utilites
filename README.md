# MyUtil.py
some useful user exprience, simplified funtions to import. maybe you can study basics of python understanding these scripts :D

- MyUtil.subplot() : make subplot at once
(example)
```python
import MyUtil
import cv2

img1 = cv2.imread('C:/img1.png')
img2 = cv2.imread('C:/img2.png')

MyUtil.subplot(img1, img2, col = 1)
```

# Crawler.py
absolutely and greedily crawl by text you specified. specialized to extract html table data, i.e. each row must have fixed length.
navigate through all nested iframes. and specify iframe path and content path.
it uses selenium webdriver

```python
## example ##
import selenium.webdriver
import crawler
from bs4 import BeautifulSoup

option = selenium.webdriver.ChromeOptions()
driver = selenium.webdriver.Chrome(executable_path='C:/chromedriver.exe',options=option)  # if you don't have, get one on the internet
url = r"some website address you want to address XD"
driver.get(url)
##... manually navigate to the place you want to scrape ... ##
# keys are to find "table where?" and "how many columns?" by analyzing distance between two keys with one row difference.
key1 = 'book_name_in_a_first_row'
key2 = 'book_name_in_a_second_row'
# or key2 = 'another_column_in_a_first_row_if_it_is_one_liner'

# <1>: if "row" has "different number of end nodes inside", this algorithm won't work. check if tags shows up along with proper order at <2>
driver.switch_to.default_content()
iframeList = driver.find_elements_by_tag_name('iframe')
iframeListAll, soupListAll, iframeIdsAll = crawler.wfs_iframes_to_soups(driver, iframeList, verbose = False)
iframeId, common_parent_path, length_between_keys = crawler.crawl_first(soupListAll, iframeIdsAll, key1, key2)

driver.switch_to.frame(iframeId)
soup = BeautifulSoup(driver.page_source, 'html.parser')

rawlist = crawler.crawl_to_list(soup, common_parent_path)
# <2>: check if texts are well ordered here. if so, you can specify where you want to extract like <3>
for e in enumerate(rawlist):
    print((e[0] % length_between_keys, e[1]))
# <3>
useful = (3, 7, 21, 22)
for i in range(len(rawlist)):
    resList = []
    order = i % length_between_keys
    item = rawlist[i]
    if order in useful:
        resList.append(item)
# <4> list_to_excel if needed
crawler.list_to_excel(xlpath, sheet_num, dataList, ncol)
```







# lifehacking tools(exe, scripts for exe)
use exe file, or modify py script

- b2s.exe : I monitors your clipboard every second. if you have path like "C:\\...", I change format to "C:/..."

- mouseLock.py : I prevent mouse to across border. if you have a monitor not using, or turned off for some purpose, it might be useful

- double_checker.exe : it's made to help "manual" double-check between documents. you can select strings to compare by pressing "ctrl + C"
