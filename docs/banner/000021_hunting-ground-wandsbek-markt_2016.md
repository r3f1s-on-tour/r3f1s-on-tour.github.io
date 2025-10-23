---
nummer: "21"
startLatitude: "53.573784"
startLongitude: "10.071849"
titel: "Hunting ground Wandsbek Markt"
picture: "https://api.bannergress.com/bnrs/pictures/4a9916708f283ca0625a1546dbcf5d55"
region: "Hamburg"
country: "Deutschland"
completed: "360"
missions: "6"
date: "2016"
bg-link: "https://bannergress.com/banner/hunting-ground-wandsbek-markt-ventrue-3567"
onyx: "0"
description: "Die sechs Vampir Clans der Camarilla begehren diese Domäne. Welcher Clan wird obsiegen? Wen wirst du unterstützen?"
lengthKMeters: "1,51"
umap: ""
title: "Hunting ground Wandsbek Markt"
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
