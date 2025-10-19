---
nummer: "106"
startLatitude: "48.141346"
startLongitude: "11.586407"
titel: "Funky Owl"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_ZN9e1VDVzZMV3RCV3fzz7LDTFRcknRdWtpWDMNY0gbXVrg-_flVLQlPIAVHtjse1OvGYWJVYkoOKZHgC1OJbG7wi_LEeoxlA4m9WSyr_Qid_L3wQFmZCnvgxq7V4dWk4IuSqEELKlnmdURWaTV3LjPwoODwajJjnBqjpeB0ZOwimvNzXeCnGr4IegXni53xQT3s_xSCnA9eSNYejX_XCUaoIG8NI-qEKZelJMx10589-nyvGsQ8VAGoFmkGmjGrIO5q9dD9Tz8iMgpf50Bw7Cj-afflY0xpskcaZZKZN8_uI5wTQfFKifUcbGv-3n6L1RJLTCOtNnEfNU580HBZ-FNHLrH8F0n6_HXrMPEciqdBsp_pwA2hlI602koirRdHCWC6I4qkYhP5KkksWyhXGCDy4A-tc5E6vbaNaD_GxX39LU3xMJb6Ks1N75w0h_HaUtoDwCan1U9gmyTJf3WVmUzih0Ln6VKIFvSXIC3id9yiGfj4DpQZo5RssRiLe6YdUaICXuIqG541asggdZmuwIktfshmHZBTt2LnQ--5MIlR_mC4MTda1GLsJ3Zi5PLoI1RJ-q34ybaQ9X8_mSxFlFrK51-GMJ_8ouQ_hgGZtPRMHr9U8ua_LkOtmdtS80JNZ52_xTa2w34RjVWFBMmCi_27rTlbXWh6OfmztvH6F3WH_8MFSPyyEKs_1aMOId2HOpqA_83Bx-paIRg5yxPgbLDMAu1f_QHxIcMqSixHWbL0XsKQLA3AMwJYBh7OK-DiO3lkY3kNfoz90cUka9n01zL8HguSQwMK7fgNuS36Mxjhewr1Lf1dvf4lYL5wI3hjA2u3u7-YID-8spmV6lUWwpIsJWbB6SSNrMH"
region: "München"
country: "Deutschland"
completed: "2694"
missions: "12"
date: "2017"
bg-link: "https://bannergress.com/banner/funky-owl-e1be"
onyx: "0"
description: "Diese Missionsreihe startet in der Nähe der Eisbachwelle und führt euch vom St. Anna Platz, über die Maximilianstraße, Richtung Marienplatz. Es gibt viel zu entdecken!"
lengthKMeters: "3,28"
title: "Funky Owl"
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

