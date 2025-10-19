---
nummer: "478"
startLatitude: "52,756318"
startLongitude: "13,244588"
titel: "Spooky Green Second Sunday in Oranienburg"
picture: "Bitte Url nachtragen"
region: "Oranienburg"
country: "Deutschland"
completed: "10.404"
missions: "6"
date: "2022"
bg-link: "https://bannergress.com/banner/spooky-green-second-sunday-in-oranienburg-9faa"
onyx: "0"
description: "Starte eine kleine Entdeckungsrunde durch Oranienburg. Die Runde startet und endet in der Bernauer Straße."
lengthKMeters: "1,599"
title: "Spooky Green Second Sunday in Oranienburg"
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

