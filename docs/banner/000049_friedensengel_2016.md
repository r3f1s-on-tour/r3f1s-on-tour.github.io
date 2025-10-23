---
nummer: "49"
startLatitude: "48.140735"
startLongitude: "11.599442"
titel: "Friedensengel"
picture: "https://api.bannergress.com/bnrs/pictures/07497fdbabbc83aa9d872aec006f5387"
region: "München"
country: "Deutschland"
completed: "1140"
missions: "48"
date: "2016"
bg-link: "https://bannergress.com/banner/friedensengel-8105"
onyx: "0"
description: "Der so genannte Friedensengel ist eigentlich der griechischen Siegesgöttin Nike nachempfunden und erinnert an den Friedensschluss nach Ende des Deutsch-Französischen Krieges von 1870/1871."
lengthKMeters: "13,40"
umap: ""
title: "Friedensengel"
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
