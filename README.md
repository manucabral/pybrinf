## pybrinf

A lightweight, zero dependencies and free Python library for extract browser information.

'Python Browser Information' allows you to extract, export or view basic information about your browser using the python language.

This project is just started, currently in development. Only supports **Windows**.

### Features
- Supports [popular browsers](https://github.com/manucabral/pybrinf/wiki#supported-browsers)
- Detects your default browser
- Use any installed browser
- Get downloads or history

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

Get downloads from all installed browsers

```py
for download in brinf.downloads():
    print(download.url, download.browser)
```
Get history from all installed browsers
```py
for website in brinf.history():
    print(website.title, website.url)
```
Get last session tabs of a browser
```py
browser = brinf.default_browser
session = browser.session()
for tabs in session.tabs()
    print(tabs.url)
```

Get all installed browsers in your system
```py
browsers = brinf.installed_browsers()
```

Check out the [wiki](https://github.com/manucabral/pybrinf/wiki) for more details.

### Constributions
All constributions, bug reports or fixes and ideas are welcome.