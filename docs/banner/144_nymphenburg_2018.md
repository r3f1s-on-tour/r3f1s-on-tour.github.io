---
nummer: "144"
startLatitude: "48.15844"
startLongitude: "11.511265"
titel: "Nymphenburg"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_ZqqErX2_mOCT2dXD7pP9FZVqMPTXP-KNirEIbK8F6QU10VmvcWqFN_qK9pxphi354qUrWJ4HcN16eX3OAtvxBzIKmNBSgUk5Rv-3Kx3SBw3L1ISpzIes35dzlkbWbisKjuG0-Zfwehv5aPmNIhlTSX3BfAzaJ7h1wbYA2sjkBedY3QVlfsnWpmw-wKYaMWXldqMGngd7Muwx-q0y019oIJR-VBsix-5umDxGRzqrB_N00hmLZE43NU3MUYah4B4E-rQltvjxVX2yFaA25onF5IlPI9zP0DeK3EgSB6T0chwqGHJvd3pJnDbo7gN1qepG39C7mb9aH38ZyykSAG7cPWfHePkouIFtmA66vVUyXaPdUdRRNYONmHEYZg8UZggZm_jKIsQbZTEXYCL3QtQUDswmntCqx8DeVHDWiJk2rbhyavb5YmEYhdvnik3fJiLPRdp_Jsy5RJpWy-mFS1c8DIyqUHz3PzmFKkJsrUyAlTjJJjUu3xMx_fDMie9J3DIUWVgT0Q5dt323SVSrPZQT8ry0aFtwCwITj6EPizXmXgd5eSeF5xKGi07tEbkcwubO5-QAwltBiT7ko_nyftea6T-ISMe-nsKUNdezoKSr-7AVMBjrhL5npk1KgxMPsWIavXjOGaYqP7_Vb-IoWQKpfFzdXvRziBO4MxjSKIF-Tq395RJczF-Oqo0GagqoqZLd0zTPvIytBgYHFQY-IkLu2M7j5YBQuOmCtGo3L_9yfxcLKrouyWELHhRq1zt4aXmsaDzVbXYJY_kvJW0JphwPbVTH8-oo8lnvRcZN21iZ1XZFntzvWSv_Y1yz-oC7YXweUB6owohgRx69ZnKGbvIGlNeEGLj1ybDgfx"
region: "München"
country: "Deutschland"
completed: "3432"
missions: "18"
date: "2018"
bg-link: "https://bannergress.com/banner/nymphenburg-2b6d"
onyx: "0"
description: "Eine Tour vom Schloss Nymphenburg über den Hubertusbrunnen zum Löwenbräukeller immer der nach dem Schloss benannten Nymphenburger Strasse entlang."
lengthKMeters: "8,65"
title: "Nymphenburg"
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

