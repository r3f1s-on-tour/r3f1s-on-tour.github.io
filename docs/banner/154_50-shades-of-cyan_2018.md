---
nummer: "154"
startLatitude: "47.807234"
startLongitude: "13.042008"
titel: "50 Shades of Cyan"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_al0S24_R7lBFZEf_r_fn9rew1TW1gU5AVD77V1Vnga-AaoMRZhfo2CWBHGp_kTiyQl3XmlrvVMiqhshasuBeOgIKC78em3McDpwMD4GwIFTq1Y-ajM0ta39c1enkjVc8X8MWfhFx0cY6n_kR4mVgY2t46Qssd5Sol70MgBRJztknOknVeqLuj7A8HyXK3rhnm_URQ4xB0JzMPypRTaBtXV9k9DqNyEG3TuIgxGd1___rsaO7IvS3A9LS8dx47EDzIgChfn1qsEpLpEK8WTqzEm8jeMfAIZs4KOok3YnEeanwgRfi50B0si1-X62gDEwJk4h7B_ho1ymbT_5vMGdRZgNu_pIqtTEYOBNG0ri6msDb3NcHXWNJ--GDWdt2NL45CXugbQjzjGDJf_yQZhSpSO8fMWUy6LEn8YZfqzMfR4XuoINEntwhUX9_pffprNmiFoaadrkdd2LkmcmzeClEmcNMGr2m1WngWiQd-fbGJFlODH4t6Y2SfVtJbOA61k2IKscPFttGtgjdxchGayOwpe2VhNhmniRlVQ6ZQ73ept0R36UdEzOuKdIHL9SrCJxGeDmLaVTp8vex1hR_NiGpdCqpmZ7y2gNnqFvFlcPKHY7CDBv1NP2zkxaZ5nano8visfXnSIXQYzfu9EIK9A0s63yZoPfVdfYGZOQmkQ-L3qyx6pGnlEEe95g2UwL_9q4-Fe1eLQP7OfWz9Zv1Q-DGACma1QGJU5gIC5nNq_NheuQMO0ntCET23aVOQ-dMo4H_Nh6Cd0BjwbybjTabYoxwpZ20RSvBIuaoZI1voRKiOLkG5w6wLqNu2cLTNzxJ9OCA6JOFLpHHUamXfpltILz9_i4d67KlA"
region: "Salzburg"
country: "Österreich"
completed: "3738"
missions: "12"
date: "2018"
bg-link: ""
onyx: "0"
description: ""
lengthKMeters: ""
title: "50 Shades of Cyan"
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

