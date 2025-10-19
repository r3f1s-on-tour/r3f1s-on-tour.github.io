---
nummer: "401"
startLatitude: "52,509237"
startLongitude: "13,497382"
titel: "Catwalk Flummi"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_YyhA49V5ZCVUi4TtsFy2xnvp9rMHi1pOu716r9TPIJHjXSobpia453UXGPK2E0NgphbbqYUoOKo6csT4Cp79JsWxPc6hUPPSVn3Kr8QWhpusv8eNZ9yEQlg0EH0rtcFBO-5J-3TVoFgJ1WXrb3drCFn5a8wY2rlsntzxeV1rE5Oa267qEmmda1jUU3iQ_nm3Yb8xp17prnTlFjNsdc8kvC-3gfG5WZjEPgTXq-4sMJ5iMfIVq6elwFSH3iDfnUe0ieXXCWFj4LNpT10dyU3GIHqtRDvE5MjDA9MmTcleOGXwfg_tyZ_uQaKeBPiTmEARmy5SUFCpQuayU-kCPz61ewUtSwxUwMJ6E7oDmMz4FWoXcsumHG8bnEs0Rc4Rh8389HLycl4AltL8DnXpQABtQYe4m6PXHRUfaO8BD2omETndHc89RhbbaIGvtmDcP_mucpJjym6M93_5Q8xgyX1a-aol6s3pHsuZZkhK0giZpkvjOLfsdbK9DXZqml-AiMjueToQmXX-GarTL6ow8P7DlmPjokMgBe0TVCQ7HUKlAVPS38Rc6z1unn3xjZOWENFTfw0kHm36fq73uVP3QF2HsRFKFL5C6yOt7pJ0omOmNtczhl6xxU-DisDVMhJTuxkUpyll2l0z-bTFAnJlEpz-YYNwMMZajBb9Kcq7H4xpIhCTjkDECCmm2VPe3PbmrOU-uzaxkH5sKVNhT5BOqixVjodtMNjhcy2M9qm43MySyxxuAZQwRGlgTbgB1YA9HxLK8QXwBaSKt3KdFK1ynA6_5n-d2tVHm4074m8vNM4kLEd5XQdNnP1DgUTocYvdxrAfGZ4435g2R1CDFkYFiAPdwKuq0nbUnn8oSI"
region: "Berlin"
country: "Deutschland"
completed: "8.592"
missions: "18"
date: "2022"
bg-link: "https://bannergress.com/banner/catwalk-flummi-13fb"
onyx: "0"
description: "Begleite Flummi auf einen Entdeckungsstreifzug vom S+U Lichtenberg nach Friedrichsfelde und dort im Bogen durch den Weitlingkiez zurück zu seinem Ausgangspunkt."
lengthKMeters: "5,00"
title: "Catwalk Flummi"
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

