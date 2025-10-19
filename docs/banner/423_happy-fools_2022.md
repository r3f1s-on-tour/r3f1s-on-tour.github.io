---
nummer: "423"
startLatitude: "53,50675"
startLongitude: "13,745004"
titel: "Happy Fools"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_ac0kAJbk8KpPsRG5eMYpfguptN-Z-Gq5v3Z8nrywuGPPhxrIy_sHvOYjxth41Nep4VIqAtA_ZUK3MowvV6426fS0wq8kNZ4a989DG4ApzUKh2Qek22YtAWeNZq837wzBy11RWxv8Z4i3J1zD8VHvGpSGpMqSzm4MhkMB-3sEl2hFeYe65kEkweBD_y2TZvbnnAYie92aFVDbGMThGZAX_EPXfBE-szgVo4f_D1whHyvXOt-Vprcruo5Cmp8o1MAEek-Bn1bfDVSXDA6550LrWyeaYTc7_6cjGo4aPTnzebfYuBg7sqxR6takfHtE2kmaQD5l7Ici44HrKa2lWnBI3CdwDTcx9Upkh_2mHmsSHY2W8L11T3AkaL7eWrzQ7Fb0uWuwfHe6MAGtsFO6P_LtJ1szCcYk28k_G0Emc4tdQDYPLA16x8ijGv0M_NnZbxVdbKS3_u6hzLGn8U9CtmJcJVpihTybYHQZybIWOEGkdpjGIYDVsm9IzmNThx-iJICtp8dZCNWyC2Endg0BINA-b7Q-W5I_sBBmTKbgDt__ZvmTWWCmvpeVl_UFY62q3F8zYTn6j5kfn4K8MbQJqq520su-CYT_X-cXJpn9CKPepPqlDIFLcZWB51iX4eDWrqJbcvyVZNerod__4Ozg_Cset9qWbW38zmuQVFR6Bv87EJgDa4aKkd7KLdzi4PWghPcG7kM7SZQ9GyLmiANws5rqQV4YtXWKN6l3vk2b1K355MTPpVtRKZKrLGzIYZvrU7Qjje1M_G8skPaLxgle9lqPZrmDSVZsKdcTozw4mpXNVa_PQnfdlNDdN8WQyV2HdS6xTR7OabjrnPieEYasIaDW1r1vS-d6yurX5TFIM_dMrJ8Es8T4882MlochDihb2m_iqWo1ES"
region: "Strasburg (Uckermark)"
country: "Deutschland"
completed: "8.814"
missions: "6"
date: "2022"
bg-link: "https://bannergress.com/banner/happy-fools-630b"
onyx: "0"
description: "Starte am Markt eine Entdeckungsreise durch die Stadt Strasburg Uckermark und entdecke dabei historische Orte der Stadt."
lengthKMeters: "2,77"
title: "Happy Fools"
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

