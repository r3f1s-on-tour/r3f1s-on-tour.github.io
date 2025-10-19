---
nummer: "498"
startLatitude: "50,944624"
startLongitude: "7,098962"
titel: "Green Phoenix"
picture: "Bitte Url nachtragen"
region: "Bergisch Gladbach"
country: "Deutschland"
completed: "10.668"
missions: "60"
date: "2022"
bg-link: "https://bannergress.com/banner/green-phoenix-736c"
onyx: "0"
description: "Willkommen im Wildpark Brück. Entdecke bei 60 Missionen die Vielfalt des Waldes."
lengthKMeters: "3,096"
title: "Green Phoenix"
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

