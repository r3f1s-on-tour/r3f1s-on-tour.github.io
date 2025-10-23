---
nummer: "22"
startLatitude: "53.462334"
startLongitude: "13.594348"
titel: "Erobere Woldegk"
picture: "https://api.bannergress.com/bnrs/pictures/3c2830ae35ae267284d887f7097ce367"
region: "Woldegk"
country: "Deutschland"
completed: "378"
missions: "18"
date: "2016"
bg-link: "https://bannergress.com/banner/erobere-woldegk-13fd"
onyx: "0"
description: ""
lengthKMeters: ""
umap: ""
title: "Erobere Woldegk"
---
# {{ page.meta.title | default('Untitled') }}

_**Datum:** {{ page.meta.date }} • **Country:** {{ page.meta.country }}_

![{{ page.meta.title | default('Bild') }}]({{ page.meta.picture }})

- **bg-link**: [{{ page.meta['bg-link'] }}]({{ page.meta['bg-link'] }})

- **nummer**: {{ page.meta.nummer }}
- **startLatitude**: {{ page.meta.startLatitude }}
- **startLongitude**: {{ page.meta.startLongitude }}
- **region**: {{ page.meta.region }}
- **country**: {{ page.meta.country }}
- **completed**: {{ page.meta.completed }}
- **missions**: {{ page.meta.missions }}
- **onyx**: {{ page.meta.onyx }}
