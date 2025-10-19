---
nummer: "260"
startLatitude: "52.528296"
startLongitude: "13.424493"
titel: "HellSpawn"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_ak3ifbyFYF_HE8Ki1ZJ2AcgdSShrW_CsnrDY04gG_ynr2P5YFcHpzEsixI3oY3mpCQy9f5JGt2S-Sbd8fDnIvE9W9goruh_JVURAo5FsacZq9dOV4z4iQg3vif2ssT5gJqopZtRFKR6ehSqg1Qk0MJp7ecYzjaK2rnHEzDhiIL6DS5nB6lq1N-B4D3eGGRkTRVhrogRLpIAxvVE5sOFn-rsfZDw2j5YaU3qMcITz0XpDuB5N3TzzSd6ICg8cER48KrUw0gwisJnR_cVr6uxsZ7npw0_eC9qBsUkmpUWr0rTWUNGvxq0vPYdmlW7vXoFMRnKwnPwkbPgw-n7g6TmSZpOubyczH5-11tdkydvHUm5RSQpabhRSau5Nbu20YJJY7b1tN7xcP2frXvUC46Oy0o5hOQPIdjIIcGHoVUz3I9N-z3P9pfgCTf05xGv5Ou56iRHkihG2ufEeF-_yGs2SivLLg3ZKf92T5lqnsY4TsxrmmM6ULDjCkJ1m7oWgjrAIhnOPnQmi8Jglg9UriKw5PW-YwmLGz9fevgsj-i28mWtp3E3rkK3GaFPBGguMyxtJ9q5hUrtBk50thQjCKBNmtSkBP7MrcZTllLJURPAdLgSQH6GmbSdkaP91ydJdZuY93lLG3Y1ZKOWdc6qiS5A4IOL6scOz_yzAeo9wcvHMUhgHZMY0slQXQUmJWxmdX4jN7cBgUNK1bxEPKFgSTSTnYVJtxQhi60WcIariTc0TT6a_yZizfCvfbrfMBUpV3peLmGnSaFB1XNcHrqQ7mWIgHdAlLT7oPoxiwX7CNIZm-oFqjE6-C3HUp41nnvlYg5UwozVCXkSgzlXHVP8Sz3fEvdWqVWrgM"
region: "Berlin"
country: "Deutschland"
completed: "6234"
missions: "24"
date: "2020"
bg-link: "https://bannergress.com/banner/hellspawn-7a6a"
onyx: "0"
description: "This mission is guiding you through the beautyfull Bötzowviertel in Berlin. It is part of 18 missions which gives you a really nice banner of the Spawn."
lengthKMeters: "4,77"
title: "HellSpawn"
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

