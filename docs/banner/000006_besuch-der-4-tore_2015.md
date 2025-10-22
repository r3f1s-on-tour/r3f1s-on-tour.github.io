---
nummer: "6"
startLatitude: "53.556192"
startLongitude: "13.266122"
titel: "Besuch der 4 Tore"
picture: "https://lh3.googleusercontent.com/pw/AP1GczMm-fJxwsRbALPJLTC-Zl7SMcFXyW54vRBOKRLjytSlbvXZOHFOvJf2RO5ujsN_LCxRAXQUK1c9Aya9tKaYogsDHBbRqNnXjjcam_-suxi7vAU7LV0G1px1zXPhXMESqFDIoOZeKnlGZ4Yfz7BAD3hygA"
region: "Neubrandenburg"
country: "Deutschland"
completed: "144"
missions: "6"
date: "2015"
bg-link: ""
onyx: "0"
description: ""
lengthKMeters: ""
umap: ""
title: "Besuch der 4 Tore"
---

# {{ page.meta.title }}
_**Datum:** {{ page.meta.date }} • **Country:** {{ page.meta.country }}_

## Bild
![{{ page.meta.title | default('Bild') }}]({{ page.meta.picture }})

## Infos
- **nummer**: {{ page.meta.nummer }}
- **startLatitude**: {{ page.meta.startLatitude }}
- **startLongitude**: {{ page.meta.startLongitude }}
- **region**: {{ page.meta.region }}
- **country**: {{ page.meta.country }}
- **completed**: {{ page.meta.completed }}
- **missions**: {{ page.meta.missions }}
- **onyx**: {{ page.meta.onyx }}

