---
nummer: "407"
startLatitude: "52,530972"
startLongitude: "13,382606"
titel: "SPAZIERGANG"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_ZwYVnNnoTcq8skhCNFXg9KwAnTtZDj21-sxAmFd10mdhHySXJKqIKBqplNK6MTPEmoe46UvmLjNHZ6FfMM-YmbJb6uHAZh1deC7rpImXu5MeWc3QUSjaveTtUngnBorQdlhls4fydhzcq39fSGTQvVDqMVfqLyrOpo2QR-RkPIa22kjFNo-dmOfWR37_Tlt3QEO9jBGsYk_TnRSVzznRMmg6WQv8b-motfIAtgnMUDRoqwx4IkjwRXgGZrlUsbMfVoydkdZfgVqVKuL3wUHG2jy9Ia9X2ozfFoUxOzBZu-lcMFwe9uhWpH0yrAMyAN4994kgJAoBnxZixQeIHDH657SZUuHwp1OnL-JMy_j0Z0AWL9znbIkJSFejcouQnwECEt6H6oahEog9AHjJdHYDTj1fmh-3p68-1AQ2dV7mRKy4O3hvSJSLfAkvCtuZpSwkD17SwFFp3XU8EW8ELgkGdnPGeGUlPUMD2zMbmsLaKWOcix41ctFgZuq1viI15PJWgK8Bjg3PhCVoLuHqTRDWrW9_UzD0P6AfS77fyLM0Xc2yvOugY1R07kupffufZv8NNm7cMfunBzLLc0P5PAhoz7G18NueXpZqD3XZJHT9XSODrLMvm_5rtzOknx0EBjYeD6LZxGMtFqzenaojyv4PkAIgRjbMrSCIcHS1zUweZtOcbEYVugW7FL4R6wTq2wdtlznxVlxn1_H11Bu_kzElf8TWJzRKubLp_Tx8wBtXhxUjOsc5siPbJRXNMtpU6bSd7k1UrCGU19WVCpQiXXElWn1SxlcqEbH7gZyeCV1gd9BoMzNlm8n_hRkKyLSyBZxMJ0UTXgTubN9sU4SmrhvR9QwiuzD_18ZUy_xJRlya_t4k53gIX_t5yESjyRLGuVPq0NVwW4"
region: "Berlin"
country: "Deutschland"
completed: "8.676"
missions: "6"
date: "2022"
bg-link: "https://bannergress.com/banner/spaziergang-88bd"
onyx: "0"
description: "Eine kleine  Runde in Berlin Mitte"
lengthKMeters: "6,23"
title: "SPAZIERGANG"
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

