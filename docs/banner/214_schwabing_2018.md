---
nummer: "214"
startLatitude: "48.157109"
startLongitude: "11.584829"
titel: "Schwabing"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_ZqJP9JIfWaRdAO895sH8ARrKEXocbSiNOcY_yrp80vGYaWOwg_c2ftaFNzO5u8DOi6Qmlhnc7Ek295yTP4mpAA1JH1Y2x1SXwhkBn-xabgUnS9_yZqxqDtAIzDdO_ZuLTQAnO7My4ZCUhEpSoo5P-RqKd2KZchdspB-kosSNriTWVprn5pY4-6xEo3tUnUm2uvRI-ztX20z6cT3jDuy6K5zQHa00Lthu2FK-kc5ll12jGvA2wetweoTPiDskuVoCotwSEhAZWLdT0WKTo12UDd_PMAD0GcToZBSQ4Vv5rU0lBHJWQpoLlxB5HleCIquUbDQnvbFDMtMLREnc7v-zEhzReNPlS9tx_GhfxFoQrc87wKJ-4tl9lJjf8CdGHmiWo36JbI9sm_7MRGicpK-iIDSIBl7VWK6oZlyiZgphcgcUJx6mwSZhHP4HPiKUtEO0S0lYByAiqrzaJqnsUVWfOqi656CZZk7l0rlsWtJAwNj4YSjNUkoZsk_8CErAVe8GZgkrAEx3HdYduuhL8spkjSlaA2sDKZ-9FNqUscWhrYAwhYrEXVPXPb29Sh2RFfMhqLMHdB3j8Up8W1Ubur9NHlVMw5jBQ1-N6LRVklrmtwiPqGCEi52ohYw2nL5GMO6kmO6XE3yuegCvWJp2kkSwLjZdzesPkYl_yJO0ryLgUAEVqTk2OwdxOYqxO6YOK6RgYSj8KHEUQIEJhOAA7Q8E0QGFe91gJIzW9lcVzQVrl99Sofwai9AxAuICsrq6fvjCISUeYdh77fNJ1QCLojOB5swuTGlmaE-a21ky0Zhpdt1tadLuEcjhQYkuCl4Kum1l-gu-ECy4T-c_1UiXbv4ACJJF9U6RI"
region: "München"
country: "Deutschland"
completed: "5202"
missions: "24"
date: "2018"
bg-link: "https://bannergress.com/banner/schwabing-611f"
onyx: "0"
description: "Eine 24teilige Runde durch den Münchner Stadtteil Schwabing.\nDie Strecke führt von der U-Bahnstation Giselastraße über die Münchner Freiheit bis zum Scheidplatz."
lengthKMeters: "9,11"
title: "Schwabing"
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

