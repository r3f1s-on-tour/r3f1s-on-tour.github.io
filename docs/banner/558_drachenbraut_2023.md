---
nummer: "558"
startLatitude: "50,997731"
startLongitude: "9,733295"
titel: "Drachenbraut"
picture: "Bitte Url nachtragen"
region: "Rotenburg an der Fulda"
country: "Deutschland"
completed: "12.408"
missions: "18"
date: "2023"
bg-link: "https://bannergress.com/banner/drachenbraut-e1b4"
onyx: "0"
description: "Willkommen zu meinen ersten Mossaik in Rotenburg an der Fulda."
lengthKMeters: "4,39"
title: "Drachenbraut"
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

