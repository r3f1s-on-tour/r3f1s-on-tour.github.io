---
nummer: "567"
startLatitude: "51,757653"
startLongitude: "14,333559"
titel: "Tour de Cottbus"
picture: "https://api.bannergress.com/bnrs/pictures/3f258f0ce5e2c5102ec9311981f34cb8"
region: "Cottbus - Chóśebuz"
country: "Deutschland"
completed: "12.552"
missions: "24"
date: "2023"
bg-link: "https://bannergress.com/banner/tour-de-cottbus-f2cd"
onyx: "0"
description: "Etappe 1 von 24 beginnt am Wahrzeichen von Cottbus und ist eine Runde um den  Spremberger Turm. Am letzten Portal gibt es den Hinweis auf die nächste Etappe."
lengthKMeters: "16,661"
umap: ""
title: "Tour de Cottbus"
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

