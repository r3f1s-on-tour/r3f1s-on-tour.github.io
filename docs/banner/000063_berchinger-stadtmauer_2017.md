---
nummer: "63"
startLatitude: "49.108382"
startLongitude: "11.444384"
titel: "Berchinger Stadtmauer"
picture: "https://api.bannergress.com/bnrs/pictures/109263d1997f0bef578efd3bf35cd29b"
region: "Sollngriesbach"
country: "Deutschland"
completed: "1404"
missions: "24"
date: "2017"
bg-link: "https://bannergress.com/banner/berchinger-stadtmauer-6ad3"
onyx: "0"
description: "Die 1. von 24 Missionen, um ein Mosaik der Berchinger Stadtmauer in's Profil zu kriegen.\nHack only. Am besten zu Fuß machbar."
lengthKMeters: "7,46"
umap: ""
title: "Berchinger Stadtmauer"
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
