---
nummer: "508"
startLatitude: "51,260319"
startLongitude: "7,145203"
titel: "Elberfeld im Schneckentempo"
picture: "Bitte Url nachtragen"
region: "Wuppertal"
country: "Deutschland"
completed: "10.836"
missions: "12"
date: "2022"
bg-link: "https://bannergress.com/banner/elberfeld-im-schneckentempo-82c3"
onyx: "0"
description: "Eine gemütliche Runde durch den Stadtbezirk Elberfeld der Stadt Wuppertal."
lengthKMeters: "2,828"
title: "Elberfeld im Schneckentempo"
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

