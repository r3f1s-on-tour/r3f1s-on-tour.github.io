---
nummer: "66"
startLatitude: "51.523668"
startLongitude: "7.452509"
titel: "MissionDay Dortmund - (25 03 2017)"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_Y1cw6pMDItF04CpUGhgeXBegvkjlLeSe13RL-28OZ69jov02DkpKzRV1fHjfH99EeFK6-vzNS8uYF3sbkfBfVGqWehxMimh_Wuxd_BAYm3AHDWaTWj7nI75vV2qGTOwlNd5uvmIoLCgGoRiUOYTFqEqlYDi1rBRCSPvMSW6sYDTaBk5eOpZqrzAlf97Vfcu8xzqDK-wEiIv7wZRl5tJo-5_WDvHwPnzY2TUJDfshmgBb52F8BoMfE0DUD5afljFQ2N2e8i92v47PHuL3HsV_lgQDfxNnhPsEGJwoC1saoHe9FKGVM6qYhb0YU0G1kvwAZpq43rOxb94vIpADkwqmcFap290ANLSNcbPXZc0RCWRucqi5cCtRm-0Fqzt-LNdR8dn47ZQyrsWPh7g8ZARfIXpuJe4ZFPR26W9A_5NjQsIRbHrY1k90v6vDjX7ubulbXAypJXER33ozWOt1rN7qJskxnvSVmVXKSUWUQraVUWPxMdjrRaYYdnAZUYdpSadkcWLO2TlQIR6-K4DhyoAI8OyuULGm-ZmcBFdcRpYxtjqAPibAO7TVAupLHuHYcQ--cazB9fM1ApttTcWIZ1wv87Uj9b1KyJNVyBWzpYhuQDlt3oCbjy99kGC8pbyDgddkP8GyWT1eP9cXjFAoxzFugytzqpkWmBvTQl_e_PC7V6Za0LBT0x-yxMnlzpdaPQBaWSLH0hDxr9nV1LiM3UMt2Iqfg-aX5lmxP41r_zzzMkseAQeoggz7LvpS-snCukrpMvf5FAv555mjxuleNaHb-6AStWwZSTIa3yiTwfNFOJEHm3b8BR2HpNJaRb2LM-uV5FVrPyaERZacxb-3usPMaxLIgvNJY"
region: "Dortmund"
country: "Deutschland"
completed: "1500"
missions: "12"
date: "2017"
bg-link: "https://bannergress.com/banner/md-dortmund-ca72"
onyx: "1"
description: ""
lengthKMeters: "92,87"
title: "MissionDay Dortmund - (25 03 2017)"
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
- **lengthKMeters**:{{ page.meta.lengthKMeters}}

