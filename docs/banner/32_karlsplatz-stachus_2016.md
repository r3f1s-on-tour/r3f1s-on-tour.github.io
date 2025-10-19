---
nummer: "32"
startLatitude: "48.139141"
startLongitude: "11.565815"
titel: "Karlsplatz Stachus"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_ZEWusogIQpjNq5R3Km65dNavF8GhSFC44Pt2PJP5g-YjGIjjufdIl1uHxz54deAutpQR24ZVSKMp5YlBcJLTOLI3wQNZsJaau9o0_nuuIlhkuocT_P3-mic0LKGK9vVJErZhz2ZiPXaJk5sPi62q_RPGQNJ8FA0x8gi3SBcE6QjgdXzb2wkKPUjLdjp5KO3IgpewX9bOQRhD1fEIWco0L-X2NxxerP-wzr6zrYmq2Ybd9mQIxDv_IRtKYxSP7x0sZzPb4JL6dpUi7jqH_q3NP6oCgEVyk8kcw1X5KdP7INF5G7DkQlwJK05buH7qzF9pKQQIMjf-adsravPGL1_5it_HUFi8G9h9NkfLLSHf7KcC-BzqgqLrtdNBG_AphF1BiAYW7RU2NHpuFu4nLPMvDI7iWj_W8-XqHZ0C48bFCAPUs5rqjbHFD_W0Ptf2FLPAs6gVf0DO1morssEWiGO09qZN-Qpt-mPTjNE1Xj8auHiSvHsN6KHFqL2IlQ6jknLUO0dyexJoAw2YWTt5lPjGdb5M1FP9MWF3Uaq4q2FLzsKC7Bzok-0EcI3plMZZSAcHR7jp0zZNt7kF9TqvPvJnz0y9yD_7GWPHB4ltmUdAJHwKotydF7FGDtpF5_wxURjWM9-SclrXm3EMbDWesa6jJYN4MEjXXS_4s1OVjHujgfJ3AajLUs9KMUrc0kr2rzxSBpi8F8_-paMpU3lDn7VuAZk4JUSXM4DGhD97s8mNYli7dsR0CGkL-d6s2pvK1UKAwAKYA0Y6WVk46sjygKMlUffT2Fbst3yiZYqTY5yeQkPUtbtz7Dz7xqMUySHfnBH38ZLfLl-akylQboUt7ypTbbeY0FgwqdhlyJ"
region: "München"
country: "Deutschland"
completed: "648"
missions: "24"
date: "2016"
bg-link: "https://bannergress.com/banner/karlsplatz-stachus-a1a8"
onyx: "0"
description: "Der Karlsplatz liegt an einer Stelle, über die im Mittelalter die Salzstraße führte, die Herzog Heinrich der Löwe von Föhring nach München verlegt hatte."
lengthKMeters: "6,14"
title: "Karlsplatz Stachus"
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

