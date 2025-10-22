---
nummer: "75"
startLatitude: "48.158265"
startLongitude: "11.503287"
titel: "Nymphenburg"
picture: "https://api.bannergress.com/bnrs/pictures/069e66615474f09b4374fee4f40390be"
region: "München"
country: "Deutschland"
completed: "2046"
missions: "3"
date: "2017"
bg-link: "https://bannergress.com/banner/nymphenburg-19e0"
onyx: "0"
description: "Schloss Nymphenburg und seine Parkanlage wurden Ende des 17. Jh. geplant und erbaut. Wir erkunden den Parkteil, der nahe am Schloss gelegen ist. Viel Spaß!"
lengthKMeters: "1,14"
umap: ""
title: "Nymphenburg"
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

