---
nummer: "462"
startLatitude: "52,551914"
startLongitude: "13,465811"
titel: "Art of Frog"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_ZVlLJcOJ9EYFpLMAdKZw3TzW6MT6LVteYe9jvb7TgOltZh_JyEF69_F0YFnBmEz0-g6HPwgbiMDBRNlUq9P9DFvSkbkE2fuu3R2ykV7BD8-F1cNRYJtUXGPK66JKGjRSR3RPeR8TIrYF8FNuz6b98i8GuAhzQnAyieRwS-9eV6ijU_YAB_rBK-2SsEDgkBobLzjBLHlyL7hcXckB1Z1fuQWzVNy69DFp0o7qWZMqkQtKiibkMtYKs9iJytHyxNb4ZPeZuCFxG1RqFo5ZbWQ2VqdCfXpvn5tDs_z9U4VKBitMuNyyHMKJg3VoY6JG9L6wR2oxCvnibwcFLcnTZEB5Vjf0l3v9WWxH8BfLD2FRKmBMFUWKKGEWkYmthl7a6xBVRCF952mOFl4CV_WvgKX_3iTVHmT_jKmVQSJ91xh5pmXhxB9E_LeVzWFtOBXZcB82jiMQdye-YIPyctuVHJgWSFsXMl6DXp8K3GPbb9oibTEq1cArElslpXxVcZTZFOS192a5tMLwrPdDyB3MS8ZbHVXxAmmdTmnHzYaCG9qHQC9_vzLBP9h06YBf9UTyBWgPTuMGJ7rjbKQKEMXcuEB_sKDvqPadrpFbBnKZWqbJS6j8pTzqwbHNho6vuO9LN-Ota6c-xfSVld-aTRDHZS94duMKowy4BgqO9yRh79v0ZgF4XYN_0cFSFQXmODTAsLrPc2vD_V13RiTqtZZA7oYmBxfKYCpLpsb1VeVTYKMnAES78JYDANLNmDnqviEOy7-Huf3vMMLON32lhPeg2uKja32Ijunu1iPw5DMtWN7UtcC-o3wyU_eXQreK7p7Xla8uQTcgSx6oHbSOSY1mOFVdh6YWLtiBFnZg952sZAUYaGSkWkhjWpR5oLzIf8bRMOguMTzSLg"
region: "Berlin"
country: "Deutschland"
completed: "9.558"
missions: "6"
date: "2022"
bg-link: "https://bannergress.com/banner/art-of-frog-32d8"
onyx: "0"
description: "In dieser Missionsreihe erkundet ihr die Gegend rund um den Weißensee"
lengthKMeters: "3,605"
title: "Art of Frog"
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

