---
nummer: "554"
startLatitude: "53,56027"
startLongitude: "13,261232"
titel: "Ohara Koson Birds"
picture: "https://lh3.googleusercontent.com/pw/AP1GczPsKGtUjCgULDf5zZG4nxKtUseKAcb6zICx9slAc67s2u4iVPHGN4HA3lfUvoKjVdmOn2C_NPd5QFf0Ct7qopS-Xd1i_0YTAkqfgyLEFHmSFx1rJ63BGEf4x1qyLmNVGU6P0hyRke2k2C2DNFMWqp17sA"
region: "Neubrandenburg"
country: "Deutschland"
completed: "12.360"
missions: "96"
date: "2023"
bg-link: "https://bannergress.com/banner/second-sunday-bird-in-neubrandenburg-fff5"
onyx: "0"
description: "Beginne eine Runde durch Neubrandenburg und entdecke auf deiner Runde Sehenswürdigkeiten und Denkmäler der Stadt Neubrandenburg. Starte am Bahnhof deine Runde"
lengthKMeters: "5,756"
title: "Ohara Koson Birds"
---

# {{ page.meta.title }}
_**Datum:** {{ page.meta.date }} • **Country:** {{ page.meta.country }}_

## Bild
![{{ page.meta.title | default('Bild') }}]({{ page.meta.picture }})

## Links
- **bg-link**: [{{ page.meta['bg-link'] }}]({{ page.meta['bg-link'] }})

## Infos
- **nummer**: {{ page.meta.nummer }}
- **startLatitude**: {{ page.meta.startLatitude }}
- **startLongitude**: {{ page.meta.startLongitude }}
- **region**: {{ page.meta.region }}
- **country**: {{ page.meta.country }}
- **completed**: {{ page.meta.completed }}
- **missions**: {{ page.meta.missions }}
- **onyx**: {{ page.meta.onyx }}
- **description**: {{ page.meta.description }}
- **lengthKMeters**: {{ page.meta.lengthKMeters }}

