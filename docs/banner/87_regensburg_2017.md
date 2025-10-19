---
nummer: "87"
startLatitude: "49.021398"
startLongitude: "12.102184"
titel: "Regensburg"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_bylKz7x3ujiUf5EMEzjX2m3zltG2drTSzbiZgrkRjrGJc6K29QGlmA5qRpJKdP_y68KumPye9kzdxASVwdHr_wil-g_kBYfja2FUUPSuIwHDhzwbCg1hrh7DULfXvzpMVTA7lmAfiY2lEvRpiydF567UPXQHD8u_qaxfNo8lMHZLgo5rQustX81bx7jl6heHkjiVi1dxGRtWB6mwyA7OxS-tiu5l4jsqUE1bEIVDSJtNpArQHEvc9ZHBIKoRsuIqjUVlXKw851OI_eQsJAo_YfZfiv2KgPMaqyOlS4IwPyfRuFvAid_gdrQ4nSaUxedCFX7I4sAX1Y59qXqagTdSBn-MaJuD_kfnJYuNCsEFT7MBeVaQ7UailG_3CVK8a7hS_68yPMfETs9ZqnakUz8fompPw_9zNJ8KHfB8XRXjopiVKiF1m53IAL7nZeCIftNux472xQRZYS1R719kaQsJf8fdCfyOapbK-XEbmbJfCb048Dq0mgaiRN0mintX2T9mmYEbwW6FzEOq6h3C1uzv4wtxxjLoK17dLXANQpvsuz5MzJV1Qhq_hxDbvsW1UKxSvQATFyg1DNnPj6lgRt2Dd6xYcFBlVOVxSt-H4bjXBkRowmApATiXMMedttYZ1xOK-rcYYXMk8JRTQEa9XHgzDChbt9cfX_33GvyMEtycQAKHDH1qcTjxgHqL1OA7khE110iiWSjcPd4LgUA0nwlBKymf6nlU85GbpwWiTBUHp3Uy9_fDSCOsgK6TOBQzcw-Z2WMeiviW-OlTx4uwaWWjQykljR7AsVkTnGONL4WvhL93xVXzhUDXbb7xcQ7uXxU5exc7X66MCAQq0ZzpICEsKbyHk99d4oeJZx"
region: "Regensburg"
country: "Deutschland"
completed: "2256"
missions: "24"
date: "2017"
bg-link: "https://bannergress.com/banner/regensburg-42b9"
onyx: "0"
description: "Das typische Regensburg-Panorama, wie du es von Postkarten kennst - jetzt für deine Missionssammlung! \nThe typical panorama of Ratisbona as you love it! Now for your mission-collection!"
lengthKMeters: "6,76"
title: "Regensburg"
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

