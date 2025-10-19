---
nummer: "471"
startLatitude: 52,50885
startLongitude: 13,497454
titel: Cat Eyes Green
picture: Bitte Url nachtragen
region: Berlin
country: Deutschland
completed: "10.320"
missions: "6"
date: "2022"
bg-link: https://bannergress.com/banner/cat-eyes-green-bd57
onyx: "0"
description: "Dieses Banner ist die zweite Farbe von insgesamt 6. 
Sie startet und Endet am S+U Lichtenberg. 
Als Passphrase wird jedweils die aktuelle Missionsnummer abgefragt

This banner is the second colour of a total of 6. 
It starts and ends at S+U Lichtenberg. 
The passphrases are only asking for the current mission number."
lengthKMeters: 2,258
title: Cat Eyes Green
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

