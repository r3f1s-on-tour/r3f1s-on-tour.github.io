---
nummer: "562"
startLatitude: "53,561402"
startLongitude: "13,261756"
titel: "Treptower Tor"
picture: "https://api.bannergress.com/bnrs/pictures/5f7927c0f266221315c11d67fd512db6"
region: "Neubrandenburg"
country: "Deutschland"
completed: "12.456"
missions: "24"
date: "2023"
bg-link: "https://bannergress.com/banner/treptower-tor-3721"
onyx: "0"
description: "Das Treptower Tor ist eines von 4 Toren  in Neubrandenburg. Im Baustil  der norddeutschen Backsteingotik wurde das Tor im 14. Jahrhundert errichtet."
lengthKMeters: "10,222"
umap: ""
title: "Treptower Tor"
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
