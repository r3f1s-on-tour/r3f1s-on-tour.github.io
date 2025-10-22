---
nummer: "5"
startLatitude: "54.309207"
startLongitude: "13.115364"
titel: "Silhouette von Stralsund"
picture: "https://lh3.googleusercontent.com/pw/AP1GczNI-ZyjX21eRIE94q8r7gSQvHkYtXFoPmWCXOPYJCywjCSq3UYCkKVwuUd5vatVIJO8vajK2JuyK5Kf0ffy0T0_Y8GVkiU9sodnY4wG2DE0Ekwi5rtUPoEMdf2qdn8AZ18FgRqg9DOZ_B-aJyuLIV1msg"
region: "Stralsund"
country: "Deutschland"
completed: "138"
missions: "6"
date: "2015"
bg-link: "https://bannergress.com/banner/silhouette-von-stralsund-a792"
onyx: "0"
description: "Vom Dänholm entlang des Strelasunds in Richtung  Parow charakterisiert die neue Rügenbrücke sowie die drei großen mittelalterlichen Kirchen der Backsteingotik die Silhouette Stralsunds."
lengthKMeters: "5,51"
umap: ""
title: "Silhouette von Stralsund"
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

