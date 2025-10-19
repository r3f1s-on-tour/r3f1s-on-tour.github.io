---
nummer: "97"
startLatitude: "48.53133"
startLongitude: "12.147025"
titel: "Landshuter Katze"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_YKWSHbQ3Dd6kSjlT36VzN3LyrJlkfn0MUiV4yQgZJpjBIchAwJadvpisL-BTWCQQzGix1cIw7QVX5QbVRHgXg_DafU9OLPHyItnBxoFD01MRlktB26EtGrXz0Nwl56DQi-wvm6eE_mN4dThmecNw7zz4__zfsUeDh9MncbZqwQ4FV3jVgMIURots7OzCThCHWpUni_m_ED2n8dhMe2oFpwDKkTpIy799-n5oaSkCauMcyKvso3OwBHrboMhzzZr_po37zYaZNznR9wKksqb-6W2KLr9vG2Fs7gU6pjCQ_flr_XfrUmIeiPZe4k74vry7-YW1uTLsvI-zcOADWEXb55QWvdWchK18y_wttyWvCcVR5U8RH3FEWAYJVnHnoUqb9UTfGi2EEQLNvuATp-hzSsdo2FxD8v1WLpkcc7GMIgR0wcSjRD-pcUO2Xp5eV3od3Vb9WvMu3_Mb4tHbTksZyVpUqoG5RYAnfCpl0HLNbaFENd5ncpEOmQHkc7tY07DFxg5ogi-0CYLcNHolf724szPM9-s-TEboRi8gzj73uw0_CTNcAEyHHbCbG_F8UnsYDEU5rJQP6XAVrf0DHYlpDUdIs7S292Ovk5p7pLqJu4sXSqOBUcTMabOuy8E4QECse6w3iiyBIbpoLted0ViV2HQmCy3QjuZCX174uwMYmXRD1PYz0s9v3mW5jORp4_ujKCxAeBZSrGKC_4i48vfPAGS8MnV2cTKEm0PoJp4jmFadvS50WyMJKwBv-UQIG8krrn-UHSvx2FE2_BfyuMRVECb1Vh7RzvNNAuVze2uC8OeGOkQXhW_s8kGT-GLx032P2ZHa1CkqmGXqkGcl2lTNrzT2CycNhVWw8v"
region: "Landshut"
country: "Deutschland"
completed: "2496"
missions: "30"
date: "2017"
bg-link: "https://bannergress.com/banner/landshuter-katze-d42b"
onyx: "0"
description: "Die Landshuter Katze führt euch durch unser schönes Landshut. \nViel Spaß"
lengthKMeters: "7,93"
title: "Landshuter Katze"
---

# {{ page.meta.title }}
_**Datum:** {{ page.meta.date }} • **Country:** {{ page.meta.country }}_

## Bild
![{{ page.meta.title | default('Bild') }}]({{ page.meta.picture }})

## Links
- **bg-link**: [{{ page.meta['bg-link'] }}]({{ page.meta['bg-link'] }})

## Infos
- **nummer**: {{ page.meta.nummer }}
- **startLatitude**: {{ page.meta.startLatitude }}
- **startLongitude**: {{ page.meta.startLongitude }}
- **region**: {{ page.meta.region }}
- **country**: {{ page.meta.country }}
- **completed**: {{ page.meta.completed }}
- **missions**: {{ page.meta.missions }}
- **onyx**: {{ page.meta.onyx }}
- **description**: {{ page.meta.description }}
- **lengthKMeters**: {{ page.meta.lengthKMeters }}

