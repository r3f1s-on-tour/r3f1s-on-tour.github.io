---
nummer: "456"
startLatitude: "53,561425"
startLongitude: "13,259994"
titel: "Sturmtruppler in Neubrandenburg"
picture: "https://api.bannergress.com/bnrs/pictures/f4c34f53c0e4612d09d9bb4302e5533a"
region: "Neubrandenburg"
country: "Deutschland"
completed: "9.474"
missions: "48"
date: "2022"
bg-link: "https://bannergress.com/banner/sturmtruppler-in-neubrandenburg-ff30"
onyx: "0"
description: "Erkunde Neubrandenburg. Die Mission beginnt am Bahnhof, führt durch den Kulturpark zum Lindenberg und dann zurück über die Südstadt. Führt dann durch den Kulturpark und endet wieder am Bahnhof."
lengthKMeters: "30,217"
umap: ""
title: "Sturmtruppler in Neubrandenburg"
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
