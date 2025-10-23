---
nummer: "47"
startLatitude: "48.139141"
startLongitude: "11.565815"
titel: "MUNICHS CELTIC KNOT"
picture: "https://api.bannergress.com/bnrs/pictures/954131ec881716126388a45ec52ad185"
region: "München"
country: "Deutschland"
completed: "1086"
missions: "36"
date: "2016"
bg-link: "https://bannergress.com/banner/munich-s-celtic-knot-a147"
onyx: "0"
description: "36er Mosaik durch München, das Wissenswertes über die Kelten vermittelt.\n\nDie Kelten besiedelten einst ganz Europa und hinterließen ihre Spuren in Großbritannien, Frankreich, Deutschland & Anatolien"
lengthKMeters: "10,38"
umap: ""
title: "MUNICHS CELTIC KNOT"
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
