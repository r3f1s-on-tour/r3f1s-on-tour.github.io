---
nummer: "516"
startLatitude: "52,502456"
startLongitude: "13,303693"
titel: "MD 2022- Stolpersteine, Berlin"
picture: "Bitte Url nachtragen"
region: "Berlin"
country: "Deutschland"
completed: "10.974"
missions: "6"
date: "2022"
bg-link: "https://bannergress.com/banner/md-2022-stolpersteine-berlin-0d29"
onyx: "0"
description: "Part of MD 2022- Stolpersteine"
lengthKMeters: "2,946"
title: "MD 2022- Stolpersteine, Berlin"
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

