---
nummer: "399"
startLatitude: "52,510658"
startLongitude: "13,499647"
titel: "Green Dragon"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_bBhDA4eHsJz8Zovpih6i6Z8jcIkGeI_4SJ-1NqiBf5Ev9Hn9WYNLW6H3IN6Ww7J3OHfiYPhMUrFx0QQGgZ21Hi356wYTuhYNS9wqtxPApxWKC4Tiu7ZIQD0BtqOATr9osnydU6KEXDhQKgICqeKUgffaQM3PbLAKgeWmjRZK7TVmC-a5bilak-a-46scK4AVL3skJZn-KuWdyDam9BaTKoH-znAZge0aC51GDwfvM2N-wZufFNcIfM85cbfyGYUUiJSIeGL_IuIEWokCf-mf__Xeb3zwdl7bUsKCivbSZ4apfycjeKzGIsVJPg_6PJC5Y8jkawCtvxcogwkooIfiVidjkw3gr5TDuRWsEglpqheexl9gxd1R5loh9-7CUOTlQVCECIPnO20RtB_J5ZYq-GIpAHRWvIer_5J8SNrslgHm8pooKuOGYj5xh-E6Ki8bzyiGaNHMDDsaRGobg2YF26bLa0twNxaq2y8UbFGXkzTqMRZZdjzj3Ei1uBnLBj8MZTwBUONhzfiWSbr4KwiBCDOy9hlR1CaVU2Msx1UI9tU26D9JCo2SdPcOHpiwbCucbo16AEaXUDrQ90VdEyStQz-XzDpTCK7rdTxK27qqOQ4snAhPoztQpDVM5ZZRqVpNB8P4Y_vbGSzD6rBf82JpPFrsJdF0crCaCIA5njNso_lJsjyuz_NNL7S17FsypDYi0aeWz5o1q3y__720W2oxwVN0xzuL6xwFQENeI-_GAub42xIzqQf1jyoUB0KXyjns0exGv9P0BYLciU4iDCMhtznXL1pNOJnd7QQw3fJEm9ad68aN1xocjY4APhe6ti-tyGQbPzXiABjAoioJYPuSmnF7V8uB7mH_Y4"
region: "Berlin"
country: "Deutschland"
completed: "8.556"
missions: "24"
date: "2022"
bg-link: "https://bannergress.com/banner/green-dragon-70cf"
onyx: "0"
description: "Der kleine Drache schlüpft am S+U Bhf Lichtenberg. Begleite ihn Richtung Friedrichsfelde Ost, um von dort weiter den Weitling- & Nöldnerkiez zu durchstreifen. Seine Reise endet dort, wo alles begann."
lengthKMeters: "12,00"
title: "Green Dragon"
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

