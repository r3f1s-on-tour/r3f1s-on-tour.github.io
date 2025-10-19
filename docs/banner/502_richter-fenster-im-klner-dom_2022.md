---
nummer: "502"
startLatitude: "50,941286"
startLongitude: "6,956972"
titel: "Richter Fenster im Kölner Dom"
picture: "Bitte Url nachtragen"
region: "Köln"
country: "Deutschland"
completed: "10.746"
missions: "18"
date: "2022"
bg-link: "https://bannergress.com/banner/richter-fenster-im-k%C3%B6lner-dom-7363"
onyx: "0"
description: "Richter-Fenster ist das von Richter entworfene Südquerhausfenster des Kölner Doms.\nRichter window is the southern transverse window of the Cologne Cathedral, designed by the artist named Richter."
lengthKMeters: "4,3"
title: "Richter Fenster im Kölner Dom"
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

