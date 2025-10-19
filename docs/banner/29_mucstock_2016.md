---
nummer: "29"
startLatitude: "48.128008"
startLongitude: "11.603175"
titel: "MUCstock"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_Z_2O59V43xJ7y54cQ323OBsxzbD4OHNyhBKtlgYZxiL-dEYgoQfLr7qE6aQ3XjG9UGN_tQEhmc1j8oPyQzdCIGu1m2kcD8qNBaoHD_2kxS2NMfk5ZvenYaaTe73dYN6QN7u6Jfrnzz85tzdJkoQ-PxKFZ_mM5ZeKXyNXqZo_TNMiTGR734nrZQxNJmJ_W36iItMubPpFbeiCbmromk_M-8p-1Oex9aiXvbW3uP5sc3rQXq7im6w8kKbgYldDKhrWS7pXl4Xv8zpMupku3FJ9-F3FRvdSE5HRWYie4e836CYFzEKa6XDQKMpMnCZaNfQkUrK-G-RMLDWblaXNJ0u5NN85vS-j61J2MpaURreFR9RvbzsswW2HVNMchpEx9xYuJJYmaiMVntJtHI0alLm9hpolY0rLU25piSWNGMOj5HzAcIupCjnrV4jAIKxrzZZ29xq2VSCWQsQZDx9dgCRDuVna6avm4cdNxuO0wN4xn8SGq12vNJjHoOgZZyXAGNsPHYbh1lr-gp3yLuTxXgkd1t1oxGHnvbXzQzF6b-tmLx0EC_--0fPIMZGpu1Gal_lL57ROhWA0VfCneqok99qfiWVAR1ydyVyfftCYEMEY9_Pk-rnXMxtQonpxKeOx08mKAXBgNQMc3KoouedY3QNzX5tdHx56XEMncSUutyoHwkZv-mV0Vrwp30gbzmlgYiLD0r6dL8LWC3tJ6T9kjkRY8B2Uok5hURffemR-zq_Rx2eeScQGgfWEDmIz3X17zzY4I2VO7sFZv2CUWK2iix46Y-YBkDkubx5QiGfFKNt-IkLUyzQinDrSk5i-DzTxLEXlLBaaJFYz-ColXCCQCInu7fXNjHqLMlVkHe"
region: "München"
country: "Deutschland"
completed: "546"
missions: "12"
date: "2016"
bg-link: ""
onyx: "0"
description: ""
lengthKMeters: ""
title: "MUCstock"
---

# {{ page.meta.title }}
_**Datum:** {{ page.meta.date }} • **Country:** {{ page.meta.country }}_

## Bild
![{{ page.meta.title | default('Bild') }}]({{ page.meta.picture }})

## Infos
- **nummer**: {{ page.meta.nummer }}
- **startLatitude**: {{ page.meta.startLatitude }}
- **startLongitude**: {{ page.meta.startLongitude }}
- **region**: {{ page.meta.region }}
- **country**: {{ page.meta.country }}
- **completed**: {{ page.meta.completed }}
- **missions**: {{ page.meta.missions }}
- **onyx**: {{ page.meta.onyx }}

