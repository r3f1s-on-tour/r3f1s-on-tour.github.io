---
nummer: "500"
startLatitude: "50,943701"
startLongitude: "6,933796"
titel: "Narrenkappe"
picture: "Bitte Url nachtragen"
region: "Köln"
country: "Deutschland"
completed: "10.704"
missions: "24"
date: "2022"
bg-link: "https://bannergress.com/banner/narrenkappe-f124"
onyx: "0"
description: "Take a walk around Koeln-Ehrenfeld. This district is known for its variety of street art."
lengthKMeters: "9,984"
title: "Narrenkappe"
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

