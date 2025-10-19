---
nummer: "494"
startLatitude: "50,943451"
startLongitude: "6,959376"
titel: "Deifel in Köln"
picture: "Bitte Url nachtragen"
region: "Köln"
country: "Deutschland"
completed: "10.566"
missions: "6"
date: "2022"
bg-link: "https://bannergress.com/banner/deifel-in-k%C3%B6ln-7270"
onyx: "0"
description: "Starte am Hauptbahnhof einen Rundgang und entdecke Köln. Auf deinem Abenteuer entdeckst du Sehenswürdigkeiten, historische Orte und den Kölner Dom. Die Runde endet am Hansaring"
lengthKMeters: "2"
title: "Deifel in Köln"
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

