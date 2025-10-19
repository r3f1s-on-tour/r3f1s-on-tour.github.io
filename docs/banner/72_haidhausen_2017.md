---
nummer: "72"
startLatitude: "48.128008"
startLongitude: "11.603175"
titel: "Haidhausen"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_ZDJD3ozbP-2QYLSq-I3JFrgVJZMOhC8nS8z1tH--zRkgPCRkbh35_Hu4Oqy8O_g4TlaQ5CNwCIQZ9vldTF8EFEjahOUNZxzEsks47thSlwvpPyY2U-8lMJFLRBMBS9qinNRLEgdt8IjvkWcAWN0yiJ4aWHzA1IEMAM-BL3WfCox7NIVhTxuuHGFA3PcYQ9zKncmfn6z6lct0UWpSm_l1ogVjecrr-bLqo7pQyGpfBk04kmaHmgztUfkTPKuEDZjiYDLoOHUvnbysQj0ZMo01SVKyM5jtZ8Q-vBpmI7YwhXww6qeman1LbUjQZ6xPO15v4DVsbjpsLMVOoqfjS7EJCvFx5TYWxIbw6pz9GhQ5j6PV3BtOTyxat7cClrAw0QQqMx3JrEaqrdiuvA0q8994FjP1QN6bHN21c_3WwUqpJyZwfBRtli5ZWQCRvmMTz0Lz4C6A_NuQ4r3BEBCMO_fR8C-KKVjTgv5URYoZtJaa6Ck9o_jUYb7azKmX_P4Z0hgQR7QFoy8cNGN8IyrdWU_n9Kx8CIXu7Rzf9xlN20curUYbtSjB4l0LdjpmcU_-dsxaMxXyVlGUHKpfDYwf55usQcMju9i-dlH_oTIswPYPdE-gDOOUz9TNNcHaoXrIEAZdQd_W8BDxMAqQM7UDYdAj7jC54TjVz1P2KTReG02pslVNQwuhf8clmeNMrWUbxOvGPiyS0Q2YSwwW7_pJyHc6ZWDJtGdgClF_TTgarJ1oKvWuXNlvXgfKNXszEJHYldT5BX0ctLIr3GiYa9Uy1RjrPHqElqYNUGMcTMimHre3Cl3Y_Uh3CS82ZmTxYntBGRxnvp9HFxVsLKYdKgjVLQFVbOSzV5afCdhbUB"
region: "München"
country: "Deutschland"
completed: "2022"
missions: "12"
date: "2017"
bg-link: "https://bannergress.com/banner/haidhausen-930a"
onyx: "0"
description: "Eine Tour durch Haidhausen vom Ostbahnhof zum deutschen Museum"
lengthKMeters: "4,84"
title: "Haidhausen"
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

