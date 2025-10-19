---
nummer: "77"
startLatitude: "48.134439"
startLongitude: "11.596121"
titel: "Wiener Platz"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_bxwK2_lS9sedZZEmYlEPewy41bNwxrk__OKYT5e7eejkfcZWTDjWUzy73FujvGjyPmw6vg1OB5zV2g9W4wk5uAtnthSNqBZMOYDB-614hYz0LH4rSRkZGwEki1MKz6FHOL6W1R_2_lD4KHjxRGSfoEV2EgqcmpdV9YL0B74MdiZyXmL05QSB6tN1Pt81Dt7D1R5IaUGkb7VDtjxhPJoVWdLZ0dYZzrR_YJD7qP_gPNi0VoYqwOR4ivLdNrYhhuCfYfybbslCY8dU8Sa-KCCCBAnTZUsNu31MPE3ZA6BwgS1MBlXbEpVuSTnxelvwIl65S6gU3NeZOXDQJWxRSQ8QSv6YiDl_uj8Mb3KZVUCkhJ39jQKEmaRq6-LrDQOYR5RrIFepFhIWEswDUdCKgB-E32u0Rt7bF8QE-y1yNWOBK7gFDUiU8jgP-NNvuKzAnQVCpD47IqDzS27h_abCP9fOuG46wWZOvygid0y0zFHKKukL5zuIMNleJkU6YVTubEFTkfjC68AygZJ6lkjSKDr3xniT-n2Zn55VCGtoEnu3XyFyAbQEGA8th8hYFmoyg6fVd-BoPRJkVm3aVFFKSq9brwI_aqalIHq_ORe_-TTFmtz83mZOidSDFuJQ7yV5pollW07sy7vB__JCbkYL9cyIJIPpM9RvBehhXxX77encLD_Hd25EaIeldCfpXNffXz8gSMMp4KyGIq77Is5uc6UPZ41EjK5G1osFuhCvMz3GIPWZ7mbQBWOBZv7ulUJtbqmRvbFgR00YH7YYhlGi5k3pUlcWXH5DRgG0sUENRcYDbBZArFp8ZtSHCeYsnvMkbGA6IFY8sxW_7iunCs3_o4J3SW7AItCC8pUH0g"
region: "München"
country: "Deutschland"
completed: "2088"
missions: "18"
date: "2017"
bg-link: "https://bannergress.com/banner/wiener-platz-d456"
onyx: "0"
description: "Am Wiener Platz befindet sich seit 1889 der kleinste der 4 ständigen Märkte Münchens. Nebenan befindet sich der Hofbräukeller, wo auch bis in die 1980er Jahre das Hofbräu-Bier gebraut wurde."
lengthKMeters: "7,90"
title: "Wiener Platz"
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

