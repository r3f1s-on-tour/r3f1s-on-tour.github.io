---
nummer: "504"
startLatitude: "51,253636"
startLongitude: "6,771298"
titel: "Find the Alien"
picture: "https://api.bannergress.com/bnrs/pictures/abf6cf5b89cb3c4d941e4591cc9d2cab"
region: "Düsseldorf"
country: "Deutschland"
completed: "10.776"
missions: "24"
date: "2022"
bg-link: "https://bannergress.com/banner/find-the-alien-90f6"
onyx: "0"
description: "Willkommen auf dem Düsseldorfer Nordfriedhof. Nachdem hier schon die Borg gesichtet worden sind, \ngibt es starke Anzeichen dass es hier auch Aliens gibt. Folge der Route in der richtigen Reihenfolge!"
lengthKMeters: "5,541"
umap: ""
title: "Find the Alien"
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
