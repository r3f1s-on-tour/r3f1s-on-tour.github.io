---
nummer: "329"
startLatitude: "53.561402"
startLongitude: "13.261756"
titel: "Green Unicorn"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_a6F4JNd0LhPB1r95No3D7ugx7L1bmtZb6hNftOfRF9JNgX1YC9is8agrH3acPw7OdlSa540Xm77R6Zb5RVHSrihTLP2aY0UaaFExj9XkF8JSiLs11u07KbCf4pIqtqcwsdTVfSwSLEuf72tT6InrLntOLet297QFRI9Vt7MFAQSw0h0IonncgFuyfrNWnHQdPSyLCGsVojwOHZe_6XY8cNjpbiuxkyjc8Dbcu2ii5mr8JH6HvXjpfFc0zboUMDSgvqTr8Vc-C3ETdJgm1_4y7ScV89LcLm-k2eKaHU2wvX5Gp6HJAHbz2H-KdeNrmigh7fjgPNwYCtxg_ChsTYLYwJeGGkIhiE1rQWbBgofsDVrC_2AXvIPbGbI1gHd0tfIu7ci24poOPgYD4mFzne59JhMhY0wtW3Xfi3uNISvDujrRvS9tMPkj0bYIDrrUEReZ_J05FKZQIAp5VhaWoiyfA_CIZewL8yc_RuRFN7FAYW-J0bejoyd10NruxrAWB0RuKc8q2EHU2QMLWZno0rzbnL1eZXzXVh2IGR7VZc8T2A38swV-3b25mDroVqpWUusRz5vtNPng4ywCpQyrfG0Zz2uuFAtHwDSXEpPi6N_DPqSDv3p_XxqO24r3C8SZDVG97qJo9mNO7Zop19spgyztPffPZmJF7iJ6g3GGGhL4i7IhxdBQa1ClhWXV7nJ4rFAoJThgwLfe7bFZ0pbxLFtuSjMroY6ElX_cijgDoKIWtJ6LeuzN2We6-_ozCkiC376rkrOt7GlN3wDfY4ZTbR7oqMYq2mDB9ClrFwl2yZwSm4DcgWiYghzeWwuGbkiJvjnC5d9Acc5zhtd2DIwnKFFljmOBOlbmfl3Bzg"
region: "Neubrandenburg"
country: "Deutschland"
completed: "7548"
missions: "36"
date: "2021"
bg-link: "https://bannergress.com/banner/green-unicorn-3bef"
onyx: "0"
description: "Die Missionen führen durch die Grünanlagen von Neubrandenburg. Dabei sieht man unter anderem den Burgwall, Strandbad Broda, den Kulturbark, das Augustabad und die hinterste Mühle."
lengthKMeters: "24,03"
title: "Green Unicorn"
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

