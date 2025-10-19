---
nummer: "75"
startLatitude: "48.158265"
startLongitude: "11.503287"
titel: "Nymphenburg"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_YSKnLVQ-L4q4_j511asK98SSW85j4B3-Z_MPsl9506fLrrD1bMrET5bEmuDALmQTFRasLlKLY_hMfYKuWunc3AcghXt6-CopB4Vvf1VdA3vlciZY4yPWrPCydmzWdKLVvnqke3kXBQym19rChMlPb8dslfPofBmVTBuXnCqdxOnAedZb6RWf3tmswMXNazz8gJOgORufwzNGhnR2m-SwNPThCjr8Vgj-s_s6NCFdmwOsmjPpUWpkSr1gjvBzHrQaoplMP2CR6QmexubZ5kj1-shr51LGDVlKscRfu9UB8tj7SJ1vMMgYak5L4iKMVfQyVqrHZJSv-RP5WK6QdNDC8uPH4VQMVmFzrn_e0VoVh0pHuYXXs_sd8zTdJpxm_EEv5MarRC2X-tyOnd3ZeIq5Khro-8d6xcJG2ti-rdxovtrbgs6YEVZhlwHKy2lXoD-Vk44xgH55fikPNgQFz9sjQeRcQ_oyc6UoxiYPs0uJ8_xrTEXD9B0zZlN9tdUAyEF4yG_9mwdlO_F6YM8h-hF_GpSzIO_JcIyuBjoi7K4grPddGFURlzcWxoaiSZhjkqwWcGJF5FHPKbQtKZJVnxftxnYlyviZhZG6ICW14kof2PDYcd8_I2MCF7bCtEbsNcxoKk9J2ZpDT04K8Z4913SqV1at2NdMaCa0iEvCTE0hWE2K3-kQYmmn__G73xr5d063w39aAUZb2gVBphG_Wg2iBiZEPi66mUpyAW0W1ChazZt-Ad_ys5GhhTC1JZ0kgTF6dT1SdJ-2UOaE6194HZ6ZIG5eaDRl5jexNYOuk80uRcuee6hTpMk95MDLbpEpV6z-OugFoNTpF3yDWRQ2t2RZWHE8GZF0_iwuJk"
region: "München"
country: "Deutschland"
completed: "2046"
missions: "3"
date: "2017"
bg-link: "https://bannergress.com/banner/nymphenburg-19e0"
onyx: "0"
description: "Schloss Nymphenburg und seine Parkanlage wurden Ende des 17. Jh. geplant und erbaut. Wir erkunden den Parkteil, der nahe am Schloss gelegen ist. Viel Spaß!"
lengthKMeters: "1,14"
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

