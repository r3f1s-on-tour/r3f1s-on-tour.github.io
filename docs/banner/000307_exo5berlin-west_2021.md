---
nummer: "307"
startLatitude: "52.506572"
startLongitude: "13.332128"
titel: "EXO5BERLIN West"
picture: "https://api.bannergress.com/bnrs/pictures/cd0bd932f3624a817bdd17cfe08e6aa4"
region: "Berlin"
country: "Deutschland"
completed: "7206"
missions: "48"
date: "2021"
bg-link: "https://bannergress.com/banner/exo5berlin-west-4c82"
onyx: "0"
description: "This mission banner will show you famous places in Berlin city west. The first mission starts at Zoologischer Garten."
lengthKMeters: "14,77"
umap: ""
title: "EXO5BERLIN West"
---
# {{ page.meta.title | default('Untitled') }}

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
