---
nummer: "17"
startLatitude: "53.554089"
startLongitude: "9.986227"
titel: BROmission!
picture: https://lh3.googleusercontent.com/lr/AFBm1_aBiG3eOAJO2YhSxZUoN1bR2J-Scc_LMKzlSCsUqwkafqnpx-wMuvKSwvAKHUITsy6OpA_JBwBq9U59W3QaeMHYFYIgq_yZK-xasORNBVL_a786oQLsH1yei2Q9IeTHmAc-9DVURMDczaO7Okx_7K-BMlqn730XsfOGcIVV517x212E_2PGbXMev9FbyS-31MZGHnbP3BuCAv3CrsoH4fGaG6sJI5Wrpd0Z0AjhQsiMyKEzeZaa_BUQRRTofx7oUI73oGDbkyRu_hy5YdpWRRzAh27yt0mNUz4Eq6gvSjL12Dwf2TtJSfspqFCAzgmPmhqdeyS76RW5L7hZrJ2wFoou6wI304Oh1pcelO6Z67eDdR2HQECpVoG93Ng6x_otMjhpxqnZ2yQCFJHtnKLnDpHIvhL1r_6ZRlzc9s6RtE3EFaqNmgdnJt7sBPu3D6p4dIkoJJNiC30rcVYcGI0O_8xxn2qZdQjySaVDgkqoSI3P65XlLC2eVgVMRxs62QsBxYJcvJIj_rb8byb1n__qtZZIw4tclFEU_iwmfVwU2kOn4TrjbPdK08RkgtjMMCM7AIqXmAewodAEtpilatLLN7yhvIKoSbntqTOd162ImSYdyNmS7waIRfxwjZ2WgUNZwjHYeCPeZxEI0xCKzQKPlQadPkooFD5fj3Wsjx5roei_KimkeNbANHn_hd_yzYFgXFXB_ou1Gw
region: Hamburg
country: Deutschland
completed: "318"
missions: "6"
date: "2015"
bg-link: https://bannergress.com/banner/bromission-c276
onyx: "0"
description: "Go for a walk with your BROs! First of the sequence. 
This is starting at Google! Get a selfie -sorry, a brolfie- there."
lengthKMeters: 1,88
title: BROmission!
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

