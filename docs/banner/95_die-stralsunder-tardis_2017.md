---
nummer: "95"
startLatitude: "54.308521"
startLongitude: "13.031108"
titel: "Die Stralsunder Tardis"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_bjQDgdPCQu_hEbN0Oot4aAcwU_xtIzhSxDE17ZvKSkENF4gawwQx-um82KqjpfcKxBZWmVZPtekwBwXZWDCqpXr5Iy8xgTmqUh27gfUBlFHuDfaMv4NXrReO4H5WeMOvnQGlPLIpkxpm6q_uGmMqFETrzhAIBMiWHz7vYoBcQLiReChZO3NYbd8QQ9D7iwnLGP_itN2j2sr-5rWVSFwZAOmuvIDoeA6uOcBFUvy1sobPBiH7xNPZ30BDUsTGcIIuy6fKIP5qZ25xTSEeGPp1rYdsfigR_rt9vl0VDnESfdDsNU2Osg6t3qX6SyKrZgGzJGfI7oLS6ajdugejJ5q0HrXuenifjK1rJ7o8oOcmwGqJfkmDPkSfeKH_wKF5ognPoBUs7R8i4gLrKml3oSSlm1TjLUQTcaGGMnW_a_BArncEva3QhQSBI98zXYqIdKxYT3noRBicOAxwzX6SMX8bIvr-y6gnWBX39zESPHcU_4a9y_PsK1G6zwTITONiP2fPudMnKbxl-ueU3zzOrghQ3jV-5yixf-l4TxKNyh_tYYPQG9mknn_I3UFuzEkdY6N1qAPye8VE2yKFHXbxrGVXcNJISauyMYUSx49v_xRh19H5ZcQ-Ei9EAkhAsBhCxOWWhyIIPOVy6mLlDv-lxL9qimdYhHAgdB0hT_O4KhPTnBiprixrsu-fU2quyAufus4qcQvKHeQ1NZpUeIFMD24rrsnyec3CPZHdjVC2MdIfW3qJi16o05bhoGEzPFJC4hEl9j3PhGmKsiE5sTGPXlh4a_FflYSSP7hi1jvfderd3zvWEnIume7iogZt7QA3nH_djWiCHqJQ9sn6HUfi9FZFHy6ZThjQ6YjnBV"
region: "Stralsund"
country: "Deutschland"
completed: "2454"
missions: "24"
date: "2017"
bg-link: "https://bannergress.com/banner/die-stralsunder-tardis-e5ff"
onyx: "0"
description: ""
lengthKMeters: ""
title: "Die Stralsunder Tardis"
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

