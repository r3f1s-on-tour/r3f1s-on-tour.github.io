---
nummer: "12"
startLatitude: "54.097717"
startLongitude: "13.456953"
titel: "Greifswalder Flagge"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_ZxXyest1RCEfqC8CZuHrfJuFK6WZricLvikMWbfPLY0sSK4F6z38byNZi5enJER3WHy7SJ3UpbXoryyXIwMFEbezfvzuQYjKoefFGSIniC8XO740p405arV_FAGVH-9kThQaVoN-R5P25pukRPZ4M6Q-LHPcEAJ8RQkzfM_GOF9tiCY_Y6uqwqcAYfbw4G-9_RFX2Xepl5mzNLMHpcBu2Hmt6gHRwV3Ocwv7LdW15TwOqq-UYGz5ezxg9sUDyB0GNj9nv9TKcB4L0D3F9Is4W1j3KU-jyX96LM0kjQdlxepUxlCCrJk03GV-5OZY1eUqtEBRI3BEJEKwcaC6PvQaFNEf96mJmYlgBtmNqxr-xOYbrqewiAb0nRhmrhi9F6oN3LudxkE4zIs3RkXqMXVCYqL2GOkgMLHdcP4B--ZO-jBOAIBTzsZ3gmzcve0tbXEvq4YHLb5i_yCfY4ne7Gl7Vs3gbtxiFgiWVg0eM_Hdjy4V9pBU9KuKFBZt21mO2dpg5rbj7ggZNV6QOKuSwtwP0RV1lmAjToSuuU-MarsAVczeIfvyCGvptuAFfF7V0p2Mzuq4dXGQ6hF46r1Hwfxbyn-prKb_FhQKHZnTY8unjw3vltqw5AggLwc-YTaRv1MTSU5T-wjTQoKKaIaeM-YdGyKrUgONJRMDqHxb9xm0IBe5LMMfYQQ2s5C8vKtH1AZOITziR2yg"
region: "Greifswald"
country: "Deutschland"
completed: "240"
missions: "18"
date: "2015"
bg-link: "https://bannergress.com/banner/greifswalder-flagge-efe8"
onyx: "0"
description: "Zeige Flagge für die einzigartige Universitäts- und Hansestadt Greifswald! Dies ist die erste von achtzehn Missionen für das Mosaik der Greifswalder Flagge."
lengthKMeters: "12,22"
title: "Greifswalder Flagge"
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

