---
nummer: "569"
startLatitude: "51,516258"
startLongitude: "14,006949"
titel: "Spaziergang durch Senftenberg"
picture: "https://api.bannergress.com/bnrs/pictures/7b13bb8094f44ddd4b30776d91c0caaf"
region: "Senftenberg - Zły Komorow"
country: "Deutschland"
completed: "12.564"
missions: "6"
date: "2023"
bg-link: "https://bannergress.com/banner/spaziergang-durch-senftenberg-02a3"
onyx: "0"
description: "Der Spaziergang durch Senftenberg zeigt schöne Flecken und besondere Orte von Senftenberg. \nLänge ca. 5 km \nDie Festung ist ab ca.17 Uhr geschlossen dann nur noch  Zugang über Treppe am Tierpark"
lengthKMeters: "4,121"
title: "Spaziergang durch Senftenberg"
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

