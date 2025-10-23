---
nummer: "515"
startLatitude: "52,505506"
startLongitude: "13,306116"
titel: "Banksy - Stop and Search"
picture: "https://api.bannergress.com/bnrs/pictures/9fa8dee798ddf525290fe2b7ab8b2e41"
region: "Berlin"
country: "Deutschland"
completed: "10.968"
missions: "24"
date: "2022"
bg-link: "https://bannergress.com/banner/banksy-stop-and-search-a9d5"
onyx: "0"
description: "Banksy, an English artist and sprayer, has advocated for peace as early as the 90s. His art has inspired many generations and hopefully will do so in the future. Over the course of these missions, you will be lead through one of the most capitalistic streets in Berlin, the Kurfürstendamm. Start and end is a mural at S Charlottenburg. Enjoy your trip!\n\n--------------------------------------------------------------------------\n\nAll credit goes to Banksy. ly <3"
lengthKMeters: "6,987"
umap: ""
title: "Banksy - Stop and Search"
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
