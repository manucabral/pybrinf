## pybrinf

A lightweight, zero dependencies and free Python library for handling browser information.

This project is just started, currently in development!

### Usage
PyPI package is not available yet, but clone it.
```bash
git clone https://github.com/manucabral/pybrinf.git
```

### Example
Getting your default browser
```py
from pybrinf import Brinf

brinf = Brinf()
brinf.init()

# get default browser
browser = brinf.default_browser
print(browser.name)
```

Default browser downloads

```py
downloads = browser.downloads

for download in downloads:
    print(download.url)
```

### Constributions
All constributions, bug reports or fixes and ideas are welcome.