---
nummer: "179"
startLatitude: "48.149014"
startLongitude: "11.460917"
titel: "Stammstrecke München"
picture: "https://api.bannergress.com/bnrs/pictures/a79aadf92efd27e31e9091eebee114de"
region: "München"
country: "Deutschland"
completed: "4308"
missions: "54"
date: "2018"
bg-link: "https://bannergress.com/banner/stammstrecke-m%C3%BCnchen-4ade"
onyx: "0"
description: ""
lengthKMeters: ""
umap: ""
title: "Stammstrecke München"
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
