---
nummer: "593"
startLatitude: "47,497523"
startLongitude: "19,054263"
titel: "Belváros-Lipótváros"
picture: "https://api.bannergress.com/bnrs/pictures/9b37d605591bc696e5dc8d4849919780"
region: "Budapest"
country: "Magyarország"
completed: "13.110"
missions: "24"
date: "2024"
bg-link: "https://bannergress.com/banner/belv%C3%A1ros-lip%C3%B3tv%C3%A1ros-57e4"
onyx: "0"
description: "Discover the central part of Budapest in District V, situated on the east bank of the river Danube."
lengthKMeters: "4,671"
umap: ""
title: "Belváros-Lipótváros"
---

# {{ page.meta.title }}
_**Datum:** {{ page.meta.date }} • **Country:** {{ page.meta.country }}_

## Bild
![{{ page.meta.title | default('Bild') }}]({{ page.meta.picture }})

## Links
- **bg-link**: [{{ page.meta['bg-link'] }}]({{ page.meta['bg-link'] }})

## Infos
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

