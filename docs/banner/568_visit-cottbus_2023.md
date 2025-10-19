---
nummer: "568"
startLatitude: 51,749995
startLongitude: 14,324926
titel: Visit Cottbus
picture: Bitte Url nachtragen
region: Cottbus - Chóśebuz
country: Deutschland
completed: "12.558"
missions: "6"
date: "2023"
bg-link: https://bannergress.com/banner/visit-cottbus-70f4
onyx: "0"
description: Diese Mission beginnt am Bahnhof und geht über die Bahnhofstraße in Richtung Theater.
lengthKMeters: 5,169
title: Visit Cottbus
---

#{{ page.meta.title}}
_**Datum:** {{ page.meta.date }} • **Country:**{{ page.meta.country}}_

## Bild
![{{page.meta.title | default('Bild')}}]({{page.meta.picture}})

## Links
- **bg-link**: {% raw %}[{{ page.meta.bg-link }}]({{ page.meta.bg-link }}){% endraw %}

## Infos
- **nummer**:{{ page.meta.nummer}}
- **startLatitude**:{{ page.meta.startLatitude}}
- **startLongitude**:{{ page.meta.startLongitude}}
- **region**:{{ page.meta.region}}
- **country**:{{ page.meta.country}}
- **completed**:{{ page.meta.completed}}
- **missions**:{{ page.meta.missions}}
- **onyx**:{{ page.meta.onyx}}
- **description**:{{ page.meta.description}}
- **lengthKMeters**:{{ page.meta.lengthKMeters}}

