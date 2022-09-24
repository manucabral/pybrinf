## pybrinf

A lightweight, zero dependencies and free Python library for extract browser information.

'Python Browser Information' allows you to extract, export or view basic information about your browser using the python language.

This project is just started, currently in development.

### Installation
PyPI package is not available yet, clone it.
```bash
git clone https://github.com/manucabral/pybrinf.git
```

### Usage
Setting up
```py
from pybrinf import Brinf

brinf = Brinf()
brinf.init()
```
Open a url
```py
browser = brinf.default_browser
browser.open('www.google.com')
```
Close the browser
```py
browser.close()
```
Get downloads

```py
for download in browser.downloads():
    print(download.url)

# get last download and open it
download = browser.downloads(limit=1)
download[0].open()
```

Get websites history
```py
for website in browser.websites():
    print(website.title)
```
Use another installed browser
```py
chrome = brinf.browser('chrome')
firefox = brinf.browser('firefox')
yandex = brinf.browser('yandex')
edge = brinf.browser('edge')
```

### Constributions
All constributions, bug reports or fixes and ideas are welcome.