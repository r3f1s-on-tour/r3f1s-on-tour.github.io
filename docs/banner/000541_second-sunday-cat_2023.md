---
nummer: "541"
startLatitude: "53,506861"
startLongitude: "13,74885"
titel: "Second Sunday Cat"
picture: "https://api.bannergress.com/bnrs/pictures/0166c6cbf03cc2bb96914b8599396a95"
region: "Strasburg (Uckermark)"
country: "Deutschland"
completed: "11.988"
missions: "24"
date: "2023"
bg-link: "https://bannergress.com/banner/second-sunday-cat-226f"
onyx: "0"
description: "Beginne eine Runde durch Strasburg und entdecke auf deiner Runde Sehenswürdigkeiten und Denkmäler der Stadt Strasburg. Starte in der Schulstraße"
lengthKMeters: "8,511"
umap: ""
title: "Second Sunday Cat"
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
