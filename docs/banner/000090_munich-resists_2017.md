---
nummer: "90"
startLatitude: "48.139956"
startLongitude: "11.586938"
titel: "Munich resists!"
picture: "https://api.bannergress.com/bnrs/pictures/aa450cbf2fff346fcbba9f846ff0b53f"
region: "München"
country: "Deutschland"
completed: "2364"
missions: "66"
date: "2017"
bg-link: "https://bannergress.com/banner/munich-resists-aa8d"
onyx: "0"
description: "Sei kein Frosch - und folge dem Weg des Widerstands durch die bayerische Landeshauptstadt!"
lengthKMeters: "25,94"
umap: ""
title: "Munich resists!"
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
