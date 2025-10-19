---
nummer: "284"
startLatitude: "48.139281"
startLongitude: "11.566211"
titel: "Roter Krieger"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_aM_5WhPcMwMTicPf6LgEOYVYSSvX5tNrnngoAXPCKonZVttPo64CfdFTKkN4KvN2nFhEFqmzxHyJudRvTnNNk45hLgUALX3kmX-vDbVGsdEhvMbm0cYKuUK-ARAsvHw38IN9S_Mb5KeDa2ucvQrRlaJMvFR1MelVEMw-5iKO3BlKg5b3sxjlb7oX5exoyoffbjvSA3wiQctWCHHpq5fsVrjt0m6FMTr5jigXYck4j1pBa7X1geKUeGmhuPd_VRoO0lTDSsEojoGpdUBJdIjGeDPsPQs9g8OC97GDpYp7fjKMLGBD4kV2n_KJpMBFrguw1d6JTJQrBCX-JSNmi25lWWLl1qhtIm_0ao5r5Q6gxkhf38QG1gbhn5-bHAIDHf0d6WrH1AKqQ4N2GmG_uCzSXwJzPmo5qibjvuQtmh6L4p41-W3zf15cd1uehav7vts6Icv2lqWvtsxoqW2lMXSy6E-JCb0vgcd8wqYfryW-Ze3noMTcTg4GyxcjL64UNSNxNuZwNV78wpHSnCMFR-rA-70z-wL8M1rQvKEJ8j3SO8L8jeBfAEF4zEw8XZEk-h-AB0wuzxgZ_ytrAESlbu9AfA73fwO4SiRcHPyar4wdcscfMqop20XDkP08xRVASDyUCBLJ-0YyozCv_8M7UELsbQayEs9zs9cBnyVTmZdCOnvUytvO1kHANKVQtAnuA7X13cSbgVCsMKZ9PDfUhBlPnidWnKLv6MJpDbom648FSkOzxFROLDvhEWQ6F-pdM583iWCCiU3UMl01hMBwmGEZ14fmg4IH8hY14RmpB6XdmUwP_ENZuXSeHCvGGT8sIZzOKulNdr1TQ9lvTsz4NVIlS6kiPhFZDgCY2u"
region: "München"
country: "Deutschland"
completed: "6630"
missions: "54"
date: "2020"
bg-link: "https://bannergress.com/banner/roter-krieger-7556"
onyx: "0"
description: "Erkunde die Stadt München ab dem Stachus über den Marienplatz, die Altstadt und wieder zurück."
lengthKMeters: "9,01"
title: "Roter Krieger"
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

