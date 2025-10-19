---
nummer: "13"
startLatitude: "53.558877"
startLongitude: "9.862231"
titel: "Botanischer Garten Mosaik"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_ZNayG0Q1TaSwV2kA5OjJhwY8JEA1AHkXgSugtRAsms_SXdXguTNPqWBFvluydM0vXd071JZN7x_3FB3RVP6_bbRjgS7ILl51EIIfpxDBLQkaYQS4jeDvQm-diJVps-vhYaAdifcQ_189cFFCyk8VurRc1SIoRq90hpL2AGfLdgCPvCDuIEz16iiNjeN8qj0_6NrclpKagg4iQbvRZO2ZYyEVs2qRg49--UT2MFnQfL7kxnmyH2PJaCk43f2tR3iZEtyhnCseR_hRZCHJHba47RLJiJeqnFqIRYtu-hMqA-5Z3R6TCRGN7f_3xg4lyZFfEdcTWmx3QqJjCOPAFKpWRn5JWz6fQsv25gDimHU_ac-i_SsuDQXU_rghSK2d4EpfG7q8iuc2KIgeouT9SrU_BZX5STy6Oy7nDCScFBufvrrysqyW2KbiZIJewnKurjBrmHrH_7Sta3Lyag_p45GJ0vu6Q-hqIsikeCOhAG1txRAddSumoxSP6Sbv6SYK1qRXLr1VWNHD9ec-zBlIO8i_fwj0p4qnxWBg0_C6cs7vWhLfHtnslk-Xe3n0i7KyLEE-EemNzL5aJyl_PZh8JAON-9tBpNCn4QIkqItErRbM54ZqWpIQ4yJUdyfcqHZv7F7wwMOAhCkCiAos23zqq_jKLkjcP4voFFZKKX86SY9xQ1yzyJZSRyO9vQ5fo4I70AIlFhRQpNLA"
region: "Hamburg"
country: "Deutschland"
completed: "258"
missions: "18"
date: "2015"
bg-link: "https://bannergress.com/banner/botanischer-garten-mosaik-30ba"
onyx: "0"
description: "Ein wunderschönes Mosaik aus dem Botanischen Garten / Loki-Schmidt-Garten"
lengthKMeters: "4,28"
title: "Botanischer Garten Mosaik"
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

