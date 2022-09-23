## pybrinf

A lightweight, zero dependencies and free Python library for handling browser information.

This project is just started, currently in development!

### Usage
PyPI package is not available yet, but clone it.
```bash
git clone https://github.com/manucabral/pybrinf.git
```

### Example
Setting up
```py
from pybrinf import Brinf

# initializes
brinf = Brinf()
brinf.init()

# use the default browser
browser = brinf.default_browser
print(browser.name)

# use another installed browser
edge = brinf.browser('edge')
edge.open('www.google.com')
edge.close()
```

Downloads

```py
for download in browser.downloads():
    print(download.url)

# you can filter
download = browser.downloads(limit=1)
download.open()
```

History
```py
for website in browser.websites():
    print(website.title)
```

### Constributions
All constributions, bug reports or fixes and ideas are welcome.