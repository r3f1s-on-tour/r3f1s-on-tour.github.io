---
nummer: "69"
startLatitude: "48.135108"
startLongitude: "11.576076"
titel: "Viktualienmarkt München"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_YEX1KdLAMMueR1pgT7_mOYnOdFR2CVsgNwqrU6F6Dv9_ySjPXQCfqU9THPCRdkmvonlKnynT4AT_UfV5qKcTrJNHDQpJMqDvML7v-KZwXVchyJ6h_oKHSnX-uGNamgwT_qDQJ4clxa2UYnAlArHjiT1f1B9p8wvVp3ErzHVgigPKw8Qx7H-gS_36IK4s4JfJk97sYGOKXaQKtW5t3Rm9QTLk33Z0oJbitsFhiwY2Bh60LqqEMNriT9_QYU52BKz459k5cE7DdjO2fbvC1O-Y0Y79RmCwjJCHLlF_3Q8ezEboVIcDWLCF8tzRDuvpR4iZpTzGkOm5uWLLxMRNdhhAcR1w4m53TcWmd6e3lQbv8henfpPwgiGxA7EsOBkBPdyCZorGBMOdAN7Je1RF1K-VoGkvvyBTPnnkQ6yZpcoQGnWlJPe0kucB6Cz6yad4mnXI2-yzm-st1SSgZicttYDLnaRlw_eDk-6zh6ac7qNYblWpTTnFMeYBDSXcAbif7KQNz52VDYvAWcut_mQkqKOJMbDFM_coXDtp4u2EWcnHGxbOFNQJh53ghyo3qhvQhTGBf6-UXmaeyJgFKsotuACh1BfWFSzh1xGyXUKLmQPxckwVnIm4Sz90gN844RlZnk2jaE6KVy-iCgNEaHbVVhasMTnoVa2rmcOEbtaW-JvQXO5Ux8BoDAGY1poC7Gy8Xnu_chBLE1QHBlApmYZAsf4sFRwHlmPSCzt7aFYS1Nkl5meTIga7D317MGjea1V4L5w0ECOvu0cSc5VRg1kfAlHdvyhBGswwPhRuBUPc_0bWED4z9yElw1fV3NjfJ_DAHoC8KeUDnMkpZeo5VrqxmleHUB_B3IThA"
region: "München"
country: "Deutschland"
completed: "1614"
missions: "24"
date: "2017"
bg-link: "https://bannergress.com/banner/viktualienmarkt-m%C3%BCnchen-14f4"
onyx: "0"
description: "Der Viktualienmarkt am heutigen Ort entstand aus der Verlegung des alten Münchner Stadtmarktes am Schrannenplatz, dem heutigen Marienplatz, der als Handelsort zu klein geworden war."
lengthKMeters: "7,60"
title: "Viktualienmarkt München"
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

