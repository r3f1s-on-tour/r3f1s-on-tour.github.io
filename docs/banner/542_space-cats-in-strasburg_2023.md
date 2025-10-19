---
nummer: "542"
startLatitude: "53,507919"
startLongitude: "13,746105"
titel: "Space Cats in Strasburg"
picture: "Bitte Url nachtragen"
region: "Strasburg (Uckermark)"
country: "Deutschland"
completed: "11.994"
missions: "6"
date: "2023"
bg-link: "https://bannergress.com/banner/space-cats-in-strasburg-bacf"
onyx: "0"
description: "Beginne eine Runde durch Strasburg und entdecke auf deiner Runde Sehenswürdigkeiten und Denkmäler der Stadt Strasburg. Starte in der Schulstraße"
lengthKMeters: "1,047"
title: "Space Cats in Strasburg"
---

# {{ page.meta.title }}
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

