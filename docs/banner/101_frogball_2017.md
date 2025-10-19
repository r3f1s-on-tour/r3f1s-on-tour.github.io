---
nummer: "101"
startLatitude: "48.918289"
startLongitude: "11.874977"
titel: "Frogball"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_bmDAVVxN5MFILsssfQcRuQY6Oc4nKiyfjTfRvgcDC-AKi1Tfxq2-PCiROGoZQBkbL4svnNzwsWCdtrW-KAvScE_9_YE6_72ohiln4Iont86rgbtgioz9Th6ebWHzMEiWAvMFhScTToDo48PS3k-OKWHYKoqR6MtOvjyjPpVfNU7J5ygLF-J_KVlKvc5VDmkWYc42fqdr2lzg0WXsoQ713l6PfR5z4AAiQhMy6qWkRLOaXNqIa8Nr6fCyv2s_UL2VGQLc8oJMyzZ0vU43oA17hUQMP-Y7fVBPHYVvW3k3dnar45pbk1mO4GkRROwVLjyDczvuz_Oabolv1XMH5WQGcx-nZgt5psuTIqMkpbjkF6sdnLcTdBkY2MWKtwfsgOYmvBrU9oCImmkR9kf3khLL2-wX7YQokSBTYeJVNFmI9iqZUwgcWNDkYmRkw9b4g6pk3Asx_XXDTcrMhTm97EILmChqArhoY7vfm9RJzckMcLz1Opnz_G3--w2jHVs2azyj9t5mjnZafd4V2gdiPmIH3SpMYuwQo_9CwR-4xjjp1w_9GnC05gUu1Onl5xhdrNU1f-AVsizc-yr1QZ0euumeEUyNq4jpwfo-sdvuJofXeBaJJ6BOT5XYB-Px2ZnlaXd-IWE-oOYe6ocuszGU5OnLeouXHQoXu1KS-DhpLlKS7Ub9JewscXWrGxyFk65VzeqvDMor14vuSrq6GExXOV7nkrOw0G_kiQIyR9nluHePWBn6BpGq-ouVF28tIp5Dr5bzSlakvleVbCH6hT0VwoM9nDjp_DBSkp4dOnaa1iJ4C076Wp1WaBp1VUb7XiJY-qE91nXbyAfz98icX1xNvKpI9ytQdbr_alhmKj"
region: "Kelheim"
country: "Deutschland"
completed: "2604"
missions: "24"
date: "2017"
bg-link: "https://bannergress.com/banner/frogball-97a6"
onyx: "0"
description: "Spiel, Schlag und Sieg! Entdecke bei einer gemütlichen Partie Frogball die wunderschöne Stadt Kelheim am bayrischen Bosporus!\nMit freundlicher Unterstützung der Resistance Rhein-Main"
lengthKMeters: "7,87"
title: "Frogball"
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

