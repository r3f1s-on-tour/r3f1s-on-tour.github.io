---
nummer: "65"
startLatitude: "48.148899"
startLongitude: "11.580952"
titel: "Rund um die Ludwigskirche"
picture: "https://api.bannergress.com/bnrs/pictures/41194c44e62f228147d66dbcb6a8e51b"
region: "München"
country: "Deutschland"
completed: "1488"
missions: "24"
date: "2017"
bg-link: "https://bannergress.com/banner/rund-um-die-ludwigskirche-ac36"
onyx: "0"
description: ""
lengthKMeters: ""
umap: ""
title: "Rund um die Ludwigskirche"
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
