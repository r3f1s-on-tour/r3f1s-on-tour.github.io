---
nummer: "69"
startLatitude: "48.135108"
startLongitude: "11.576076"
titel: "Viktualienmarkt München"
picture: "https://api.bannergress.com/bnrs/pictures/d78faacdee4e460a4f3aecd6f6df5ff0"
region: "München"
country: "Deutschland"
completed: "1614"
missions: "24"
date: "2017"
bg-link: "https://bannergress.com/banner/viktualienmarkt-m%C3%BCnchen-14f4"
onyx: "0"
description: "Der Viktualienmarkt am heutigen Ort entstand aus der Verlegung des alten Münchner Stadtmarktes am Schrannenplatz, dem heutigen Marienplatz, der als Handelsort zu klein geworden war."
lengthKMeters: "7,60"
umap: ""
title: "Viktualienmarkt München"
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
