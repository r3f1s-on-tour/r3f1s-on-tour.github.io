---
nummer: "544"
startLatitude: "53,556959"
startLongitude: "13,26129"
titel: "Frog in Neubrandenburg"
picture: "https://api.bannergress.com/bnrs/pictures/756fc53167da24deda52c4fe6b4b0f95"
region: "Neubrandenburg"
country: "Deutschland"
completed: "12.036"
missions: "36"
date: "2023"
bg-link: "https://bannergress.com/banner/frog-in-neubrandenburg-8380"
onyx: "0"
description: "Beginne eine Runde durch Neubrandenburg und entdecke auf deiner Runde die Sehenswürdigkeiten und Denkmäler der Stadt."
lengthKMeters: "3,013"
umap: ""
title: "Frog in Neubrandenburg"
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

