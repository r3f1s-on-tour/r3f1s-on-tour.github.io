---
nummer: "26"
startLatitude: "51.338149"
startLongitude: "12.380866"
titel: "Drachenfrau"
picture: "https://api.bannergress.com/bnrs/pictures/1b0601554cccf46bbf897c8a7d97d3b7"
region: "Leipzig"
country: "Deutschland"
completed: "468"
missions: "24"
date: "2016"
bg-link: "https://bannergress.com/banner/drachenfrau-5063"
onyx: "0"
description: "In der fast fertig sanierten Innenstadt kann man gut shoppen, altes und neues entdecken oder einfach durch die Gassen wandeln. Viel Spaß dabei."
lengthKMeters: "7,44"
umap: ""
title: "Drachenfrau"
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
