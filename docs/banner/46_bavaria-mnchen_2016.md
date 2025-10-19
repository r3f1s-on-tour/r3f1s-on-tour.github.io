---
nummer: "46"
startLatitude: "48.130672"
startLongitude: "11.545971"
titel: "Bavaria München"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_Y0MjpZGkkB3EJkele8vXUwUTUQfcbN6xvIKeV0vS6qcKTDWXkojfqSNk44VI1CVamQXKE4IxfoNoOCLaQodTSG-2J1hHO9XUMnuJILKjOGvxNdis7wfdniLBi5EqwDjmPyT-f4d-yrpA0FtT8hfISWhIfzPKerQ75e0PLS3MvHXD2D1u08hyWDyGDBIxBnfnXIPlSNkl6MR0E0cn4v8xE-FW9njov0hgl7RP72MmHXoRDGAGVfQzmC23jQW7v_o0UwwSLrgrlJyQLStOjh5KjQ-PFVjUqO7n4DF4qviShU2Zjddrts5PtMFAnn7B0mhEaBuWIUbz1rckvy8GYDXgxXXx_8AnSsHrS-KXO8PANl5HCsVVPXG9p8HdqNShP23ZHrUa2JwL6g4AykWC_0C8g3SeBp2aB8jDNMg2jYy3bStqoKCtuML53mCnCXRi8vBjA921J2hEj0nLR9SMt2uX8y42FgX35AzyxM3Lz6Cc13AJDvhb0pn6SfQfXnCfL43dVYpGkIA8Tn8fbKDx17oyDdZz86YGGW-vxoEvve-Rj30h5Svzba3agPycJHOEiegxJ437w66MJln3_txBqWE5cpdshetTffuv77CP14knenhN2XkczFauBt6JU56RttrJJYzevFIsDVJOzdrgpkNFAq1NF5DHYp67TFkx2_JuiaaTbVuNWuLleBQqW6069VYul7DT8K3hbDp2I0P1bTrf_ZwUyN3MK6ob_687xHhVEK0HKf3_M9I1W7ssDxnjPGLAozUyXHHIas5tCBOGrC221CEpMzAjfz49OuVZxYGLN6uDYrKnT_gcvy7gUed-X2zU7y-7AJGoLBK9LplzvheoDXbaYkj-dq7blZ"
region: "München"
country: "Deutschland"
completed: "1050"
missions: "24"
date: "2016"
bg-link: "https://bannergress.com/banner/bavaria-m%C3%BCnchen-78e7"
onyx: "0"
description: "Die kolossale und monumental anmutende Bronzestatue der Bavaria wurde im Auftrag von König Ludwig I. (1786–1868) in den Jahren 1843 bis 1850 errichtet. Sie bildet eine Einheit mit der Ruhmeshalle."
lengthKMeters: "9,69"
title: "Bavaria München"
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

