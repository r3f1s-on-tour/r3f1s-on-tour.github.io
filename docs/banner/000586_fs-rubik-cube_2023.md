---
nummer: "586"
startLatitude: "51,062715"
startLongitude: "13,745904"
titel: "#FS Rubik Cube"
picture: "https://api.bannergress.com/bnrs/pictures/58e35104a29b981b51012f9c4d015604"
region: "Dresden"
country: "Deutschland"
completed: "13.014"
missions: "6"
date: "2023"
bg-link: "https://bannergress.com/banner/fs-rubik-cube-5915"
onyx: "0"
description: "Can you solve this riddle at the FS in Dresden?"
lengthKMeters: "1,828"
umap: ""
title: "#FS Rubik Cube"
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
