---
nummer: "540"
startLatitude: "53,56603"
startLongitude: "13,259574"
titel: "Second Sunday"
picture: "https://api.bannergress.com/bnrs/pictures/37af51a3f3295a162c245f325a7e4d61"
region: "Neubrandenburg"
country: "Deutschland"
completed: "11.964"
missions: "6"
date: "2023"
bg-link: "https://bannergress.com/banner/second-sunday-2075"
onyx: "0"
description: "Second Sunday im Oktober 2022 in Neubrandenburg"
lengthKMeters: "2,132"
umap: ""
title: "Second Sunday"
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
