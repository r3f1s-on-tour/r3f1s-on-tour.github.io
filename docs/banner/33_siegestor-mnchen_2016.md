---
nummer: "33"
startLatitude: "48.140569"
startLongitude: "11.577356"
titel: "Siegestor München"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_b8pDWghIi6kH5DUFpKFMwFBGJwCqLM5-hnH9e18qlH-etDavKt-URwO61WRBSFo60PPNwhyR6TPv2ICELuFhBI1zcp-auWOucHyJBiiCmTfxksekW5Hnkf5a5ApFlz0DK8rf7ncbZt9ma7IMH9Zs7fy9vGGO_kzHtc4s_M830IEnUGt0OCR8XTufpe8v2tFdg2-dlV2wdpr4P59c9O5QIZZy5XoSJvXp3JIDZm5D-SxxG6wVyb1TTnCjpv_zbujvQ0GZgjkuuBKvorBnsRWIpsbRmM1E2wFzTOIWt8kXjL_kILw-AqFtFi5-aNPC8vvTCToyQivC1AMNdhagNti_0k7MQ8Pls_7XQ-ZTNbv-3o7VtLNj6BE12f53aqrmTtLdOR9zbuVBt_fANG1snLPyW2sylIGMZry2mSfpYTk_9q3weLod8Ipx7hSy0Zqf3PHLWbLyDml_mBJ4p8L1X4GloLyiCl_ZNARgkn_MJIRdNg9vK5FhsvBSQwPj4hXQz0wg2cpsTV1wIKlmXlNlR6voUfwycebQcLPo3ZRHPNT8h-h0z6pudxsha420lIG-7UNmKvh2Tf1ZJvaH9Qqb8mGK63LoP5fLcGQeBJQ7O9bFbqsYjqfdvS2Pr_X3zqKboia-XNm5Kv6PfPYgYZgaGk-cToa2XshiM0NqoU8r038mYXvWjSul8o2VE6F897CsnUSTdvhHfAuGj1qWDPekcJgbQXC6zw2zdmohPvl7A72xX49ZrD269yjuNjkd64c7vnSec4dtnv0lRh0guKXk-ztS2WhCLrSVqEA3FjJegFxeah96Yj6i7nn3hh-0JmKIxZLUoeZJXxI3p-nSB-m9j4h4rObYgLatoophXa"
region: "München"
country: "Deutschland"
completed: "672"
missions: "24"
date: "2016"
bg-link: "https://bannergress.com/banner/siegestor-m%C3%BCnchen-4f77"
onyx: "0"
description: "Das Siegestor wurde 1843 bis 1850 aus Kelheimer Kalkstein errichtet. Am 15. Oktober 1850 übergab König Maximilian II. im Namen seines abgedankten Vaters das Siegestor an die Stadt München."
lengthKMeters: "7,66"
title: "Siegestor München"
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

