---
nummer: "580"
startLatitude: "51,66616"
startLongitude: "6,450327"
titel: "Hafentempel Xanten"
picture: "Bitte Url nachtragen"
region: "Lüttingen"
country: "Deutschland"
completed: "12.864"
missions: "18"
date: "2023"
bg-link: "https://bannergress.com/banner/hafentempel-xanten-5274"
onyx: "0"
description: "Dieses 18 Mosaik führt durch den APX.  Hier muss man Eintritt bezahlen. die Preise findet ihr auf folgender Internetseite www.apx.lvr.de. Für Kinder ist dort ein Kletterparadies und Hüpfkissen."
lengthKMeters: "6,671"
title: "Hafentempel Xanten"
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

