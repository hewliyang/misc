# Major fast-food outlets in Malaysia

This repo contains code to *scrape* datasets for all KFC, McDonalds, Pizza Hut and Dominos outlets in Malaysia.

`pip install` the packages you need.

Last updated : `28/12/2022`

Usage:

```python
import pandas as pd
from utils.scraper import get_mcd

mcd_df = get_mcd()
```

These API's return a lot of data, most are irrelevant. Check which ones you want to use with

```python
mcd_df.columns
```

Note that the data is pretty noisy. There is probably a lot more cleaning to do!
