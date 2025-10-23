---
nummer: "62"
startLatitude: "47.377718"
startLongitude: "8.54146"
titel: "Zürich Biocard"
picture: "https://api.bannergress.com/bnrs/pictures/0f8d583886672ef36e28dd0a88fda13f"
region: "Zürich"
country: "Schweiz/Suisse/Svizzera/Svizra"
completed: "1380"
missions: "24"
date: "2017"
bg-link: "https://bannergress.com/banner/z%C3%BCrich-biocard-79bc"
onyx: "0"
description: "Zurich Main Station is the largest train station in Switzerland, it serves about 3000 connections a day. It's the main hub to connect to the rest of Switzerland."
lengthKMeters: "7,97"
umap: ""
title: "Zürich Biocard"
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
