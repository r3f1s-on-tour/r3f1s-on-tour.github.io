---
nummer: "164"
startLatitude: "49.452761"
startLongitude: "11.078086"
titel: "Blaue Nacht Ost"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_Z5KENZzQm9Yr8h7Q1VMhRsoZoR1w45tz0xFcZLwP7A-5EP-BuNiTACtibtKibcCUzxVFmyiTcYrFiGS_mCQtHZLPI98ceBuV3IIny008CXpew7vySvzTedqT0KXAWsrWSCQ0F5vscD4-NRbtZENeW867tVCHAMFt4C4EoJxV4MV73kpWdiKOkrY0s94KFp856KwwIfJQsabaUWnuHoDMWirgoLS6KHwzcwXsqek-QRz_NgrimZvP6bztm8t1fE7G8coteKnRiSkRgHaSeXfDq9Vp9k31EXa29NY41mSffsuu48Xxa0wScOG8evOilDPKX95dg888wk7M7IWjHdccG1usLTO4Y23bgl2v_qUI5ptpsMGk7JPsznPPzDRS2bBZZt4J76g4I-kURonYQyJHlUi30-faTmyHLrL0gGgiJ3UP5biPbKXbK62pkOY6u9iZbkwKUIpBfVPcaThIAopMY00UUB9QNBD3-LJeWqzBUcaiPFiut3YckvdLkWqhhhOhjOqXhKie6okfIp_B2KfZP3E_GbLK_Nk5SuUYjXytXD5dYZPLDPiyy0aTxKCwtCbHnF4YglUFw4tpVC3JBX_iNEz5-iAM4PTMrrTdOH3lG7SDp5Ryh3DRv_WrTM-5DTZSJXYjXkBZH4a8TJMJJ2gl29tRKndcQxy6d3fkJkbGYaVW6s4Je4REO4QRRhchHR20RomuiYqOC-jdbbFR9krUqDGjOfbUrnNTNepnMSV1lVfQaf10oeWFfhK_8SJThJTu7Yye918vyFdrIbiyQoO1RCgngrWkXoatS0s4XzJYscqWWOuhm_Xxwv8k5kp4MgNfGck-3tOUAi38hyCr65Kf0-GKvwGoI"
region: "Nürnberg"
country: "Deutschland"
completed: "3984"
missions: "36"
date: "2018"
bg-link: ""
onyx: "0"
description: ""
lengthKMeters: ""
title: "Blaue Nacht Ost"
---

# {{ page.meta.title }}
_**Datum:** {{ page.meta.date }} • **Country:** {{ page.meta.country }}_

## Bild
![{{ page.meta.title | default('Bild') }}]({{ page.meta.picture }})

## Infos
- **nummer**: {{ page.meta.nummer }}
- **startLatitude**: {{ page.meta.startLatitude }}
- **startLongitude**: {{ page.meta.startLongitude }}
- **region**: {{ page.meta.region }}
- **country**: {{ page.meta.country }}
- **completed**: {{ page.meta.completed }}
- **missions**: {{ page.meta.missions }}
- **onyx**: {{ page.meta.onyx }}

