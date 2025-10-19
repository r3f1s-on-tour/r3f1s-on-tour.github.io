---
nummer: "585"
startLatitude: "51,057646"
startLongitude: "13,740839"
titel: "Happy Penguins"
picture: "Bitte Url nachtragen"
region: "Dresden"
country: "Deutschland"
completed: "13.008"
missions: "6"
date: "2023"
bg-link: "https://bannergress.com/banner/happy-penguins-d971"
onyx: "0"
description: "Weihnachtliche Pinguine verstecken sich am Dresdner Elbufer. Kannst du sie finden?"
lengthKMeters: "1,619"
title: "Happy Penguins"
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

