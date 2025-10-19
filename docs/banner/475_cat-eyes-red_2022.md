---
nummer: "475"
startLatitude: "52,50885"
startLongitude: "13,497454"
titel: "Cat Eyes Red"
picture: "Bitte Url nachtragen"
region: "Berlin"
country: "Deutschland"
completed: "10.368"
missions: "6"
date: "2022"
bg-link: "https://bannergress.com/banner/cat-eyes-red-31ed"
onyx: "0"
description: "Dieses Banner ist die vierte Farbe von insgesamt 6. \nSie startet und Endet am S+U Lichtenberg. \nAls Passphrase wird jedweils die aktuelle Missionsnummer abgefragt\n\nThis banner is the fourth colour of a total of 6. \nIt starts and ends at S+U Lichtenberg. \nThe passphrases are only asking for the current mission number."
lengthKMeters: "2,258"
title: "Cat Eyes Red"
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

