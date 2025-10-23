---
nummer: "76"
startLatitude: "48.254208"
startLongitude: "11.444106"
titel: "Stadtwappen Dachau"
picture: "https://api.bannergress.com/bnrs/pictures/b038833bc9235fa7d58e6918acb67bda"
region: "Dachau"
country: "Deutschland"
completed: "2070"
missions: "24"
date: "2017"
bg-link: "https://bannergress.com/banner/stadtwappen-dachau-b0c1"
onyx: "0"
description: "Zeig allen, dass du Dachau wirklich besucht hast! (Start- Bahnhof)\nShow everyone that you've been to Dachau! (Start- Train Station)\n\nIn rememberance of liberation Dachau's concentration camp."
lengthKMeters: "11,39"
umap: ""
title: "Stadtwappen Dachau"
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
- **description**: {{ page.meta.description }}
- **lengthKMeters**: {{ page.meta.lengthKMeters }}
