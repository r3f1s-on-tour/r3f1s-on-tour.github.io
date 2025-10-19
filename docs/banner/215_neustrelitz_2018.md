---
nummer: "215"
startLatitude: "53.360699"
startLongitude: "13.058199"
titel: "Neustrelitz"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_ZSqqY_hluEoiCVlJQwaul3uSwjetPvooAwzU4hpSAALOiWNENu_aq1a86tvWQdPyQ2YWl9nZ5URroU07DALSa1eLtZ3GYnPE8sV-YjCGZUMypZqRFXvWpUOoDsDiVx-YCm6_ZHETASOa6B2U3bJ8xXYtZElo59mXWlfg0P1Scql_1asqpku769cAXM2-4gXOw_ALsLq9exHwVQM5g-wUN-oA__XSrTRkFYuy5pf2CuSX_7th2gd5vtAQuhXdeOdjg-N4FL9EAEDkIgrDrbzbt-f-a8vtmxTVbOFWqYYePTsuh71rUs8URDZ3ZsUj8hhLVR12hj5GQF5YG7TtQQExa_CjDlNZeYkNFWPB05uBo-4ACIP_WDHvmxc9ccd2hYFHddy5-bYXVay-383SIp5VWoKnyo9Z0QfdvCPFBYrmkycnoLWt25ULqZ-6n0c5BrL09zBj9BdEUx-Xgg5dJ-oV-E3NoujOuxVVx1BYj-NrbpDaxOiA-d0-CgVyRyfJ2APoWk-DmnT-czksipk3vZzLLebpX-nOK_cnkLcD3-OR13XVseeAckZ7G3U90u7W4XzYdNt4A3RWmMtNw-d9ZkRfOdj1a9cjhQPUx54TWU0VdxqbH6-eC4zyE6t3iEokJC8qPYhXN_hbfW5sjxL-rGGLNAjoLAAKoj-eL9ofj14stUQU6WY83Vxd-OsE4RzeD241YLzJ5ZN1oGZ5gnvt1uGDPHlcHM8RSPhvgmwMvKC6sTDgbJs_jXQd0j5FUD_-OoD1N4VuuSRWy85g0trPJ7ghREcN21u3BRzHl4NeIYioGuQKPsL0C3dqScV69Xc8GFpIXP_chBPCYPrcy6snUX8ucvJ_5oTyE"
region: "Neustrelitz"
country: "Deutschland"
completed: "5220"
missions: "18"
date: "2018"
bg-link: ""
onyx: "0"
description: ""
lengthKMeters: ""
title: "Neustrelitz"
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

