---
nummer: "210"
startLatitude: "48.135108"
startLongitude: "11.576076"
titel: "Münchner Maibaum"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_b5MljbUkpUmUUk3bjbGJ8_O52mSqcilyMvu1-D3lcYw5fYLaI2fRVZC-upQ6g2si1bkon8vqt9K4A6pyC2eti_ZqAaVecvScRBBMhSPAn9ndBsFbp2hCqjRs4pPSIhVKXwzVStzBreoOg3oslKP9ztIYP6TXJO2suyTQ8N6h-ob8NNxwpcgUoOFChQUulOiVWMZ94uk65BA70-UqDHFKbYrSL_yLd8h4d1cmM6T95mtS0zbIVp7BILRSuTrQwi7mVDScfkVBROL6qfSfgA6IWQKKZBViike_lF2W3C9NY4rkVc-eLelv-wsyoewOpu55I6Scao4wjZRXeaXlqVEdZQuiorCzQK-DbDwGS5NqHBvhDNrtJwV07Z40U2gU_ssRdeo-49AKRjuVaJxLVnMI8IoO-T3UrU42VUAN7AbS4UuNiPmFrIbt5GotU6W5rn8n0gHOTjcHN6DNHA_QN4eT3vWS11OnA18YOVCn0zM0byO8PRSrnpM7dQNoa87WeVsEmL4CWtMmyqvWwLH43Z6lSnZkZtti5t8KNQ_Rl1jZ9ZLYbsH75f0oeF_k7nC-qbDRh-1YkdxYGtgPguq4Gd30YEUVw52ckYHwVloaVW2RO1EC9NbQcUuKmr94cxCwPgxDULIhmS9H6mos2qocVAHUDHlqmOgHMe5MGyHbwfb6fALK0FlsHMWCXCLSpoi0EJfPRUhYSrK0Z4Y6wLKorovNU8g2IyPU8Bjr76UTd5tZLAFHfvJJWPL0ltN7X1UIf6rCCFNTmY4IPuXA7NsxkmGp9EWxzGqeXT1LaqfeK5jiWHUtilv75dEFckF3cbHrU75ZQaSpyiuoQ8gWSB7GMlECDQynzNvkVz4jbw"
region: "München"
country: "Deutschland"
completed: "5112"
missions: "216"
date: "2018"
bg-link: "https://bannergress.com/banner/m%C3%BCnchner-maibaum-062e"
onyx: "1"
description: "Das große Maibaum Mosaik startet am Maibaum am Viktualienmarkt und führt uns in 4 Schleifen durch ganz München. Das Mosaik besteht aus 216 Missionen ."
lengthKMeters: "91,63"
title: "Münchner Maibaum"
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

