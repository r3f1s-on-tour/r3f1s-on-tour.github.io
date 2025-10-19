---
nummer: "550"
startLatitude: 53,507239
startLongitude: 13,745734
titel: Moutain Dragon in Strasburg
picture: Bitte Url nachtragen
region: Strasburg (Uckermark)
country: Deutschland
completed: "12.180"
missions: "6"
date: "2023"
bg-link: https://bannergress.com/banner/moutain-dragon-in-strasburg-66e0
onyx: "0"
description: Starte am Marktplatz  einen Rundgang und entdecke Strasburg. Auf deinem Abenteuer entdeckst du Sehenswürdigkeiten und historische Orte. Die Runde endet auf dem Marktplatz
lengthKMeters: 3,514
title: Moutain Dragon in Strasburg
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

