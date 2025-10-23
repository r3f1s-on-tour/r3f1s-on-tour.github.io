---
nummer: "12"
startLatitude: "54.097717"
startLongitude: "13.456953"
titel: "Greifswalder Flagge"
picture: "https://api.bannergress.com/bnrs/pictures/98098407103277f8e6c82ac9c530ea09"
region: "Greifswald"
country: "Deutschland"
completed: "240"
missions: "18"
date: "2015"
bg-link: "https://bannergress.com/banner/greifswalder-flagge-efe8"
onyx: "0"
description: "Zeige Flagge für die einzigartige Universitäts- und Hansestadt Greifswald! Dies ist die erste von achtzehn Missionen für das Mosaik der Greifswalder Flagge."
lengthKMeters: "12,22"
umap: ""
title: "Greifswalder Flagge"
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
