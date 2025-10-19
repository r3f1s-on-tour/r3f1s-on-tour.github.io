---
nummer: "26"
startLatitude: "51.338149"
startLongitude: "12.380866"
titel: "Drachenfrau"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_Yvrbbircdy7_qBmSQaQ2VNzUAN3AwiDwPAGwFuKQN7bzjq99pvwUPQ7s3C-lCwppLBsOYbqPu5FYSn5Nh8PU3I62nLsazhm6_ojWOq667tYaKDNB1Lsn2Lg2wGwuFtqqHmPimQ-gFFeOwdfmI3jdRx-tVRJ3HK0kywZKWBzRzHk96IA1ho0uSZCKfstPpSvfF8dSdXAyTk4Fqfuv-DhP5OY-JvZtSCZFmIFeOUGRswjMsHxL4IvXsbc8agjqjQOmq2g1czo9IRwE9Hh0dJCRqI9FooosUOLUUy82Ltwa7BoSYBORtJwsnnEbb_KAmsTQ298GT5IPbyQ6wM_dDQ98hVpG42rL8kkySOKU7clOwtggrfvMEY24t05D_K6LLXB16T_v2ThcHbxwU50JidZBFVQBEpIQM1Js89RGJdBwqq8_J0nWto44DYBulnWE2SBNk6eOXTNF_sACnwCJqJXlCafmlI6Yz8XyrnY6Uk-MTdsL0KRzC49t2c85nnDsu5SCD5QbRXsTpNj2I1tk_4_HiTp-grqycgw3DAsdEkwGZJa4vu3iltwUAFlXD3gq2ep-hFOPRTmD3u-grT6_ZR8s-qYPhXFGO_gkD8WJU-Zz_ckqhI3hpuMBI33DiBwCNDZ5Mu3zaqukmVskJh_Mk1EkdyjaZxIL5yQ2yEB2DsQVpzjwVfNSUSn38mH6cnoFXd829DXVG4alGsIa1NrGUUmKM-6DL67rLObDUzSOe2FJpl5oXv_pAyura2eZhVgOJ03C3MhDnpjHyzsIr_m7db_d-0z1YdpPKzgyMwr5mwJdoKHGiX0lfDG0XMFj7dozdzBvAL6UWr3UJltzs1wboZI-43hDjNKkgURNcq"
region: "Leipzig"
country: "Deutschland"
completed: "468"
missions: "24"
date: "2016"
bg-link: "https://bannergress.com/banner/drachenfrau-5063"
onyx: "0"
description: "In der fast fertig sanierten Innenstadt kann man gut shoppen, altes und neues entdecken oder einfach durch die Gassen wandeln. Viel Spaß dabei."
lengthKMeters: "7,44"
title: "Drachenfrau"
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

