---
nummer: "171"
startLatitude: "52.532442"
startLongitude: "13.475188"
titel: "The Eye of the Eagle"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_ZC1z93Pg_6C3EALQhGiNRUL6lF30MkOTfxy9vVfpUkVAn0fuCQ5dUb5qI3AzfNa00dPE39pjCE0RE32AMa_QeOn5ZkvMnW6IIgXZh6FHiVqDxsunSi7KtMsqu5TD7n8H7d0zuVmbHBBO4F1Z5kLG657QQvuzRVba0ZktBj54I2mUP7ojbvmWimo-CjhiIlyndAfcDKuEBb8eDhhef2iGG_pG85dMOIMaA0uLcRwd3LrwPph7_cc3E8EwV9vYvncnXFRpqzmFONKutTuD9M5XmSNkyb_az8YrrxX8Vr_gsH1HhT6iUwfdIGBmYHILQbVi_MnAtFl9ytFk1dYqt7SF1w9ka4tSInhkpC1VpP2B2P-FP_y9sv680sECrhfOuCaQLDI4tFWI014BJQ1kUQ1ZwE6yFPckZcB8LO6onHTNQLhjxc84BxqnsoMStjFw3Re2oLt7oMshEngku2veFhLBn6lImRxLB5b__13AAEU3PXj93zeBrETFmLM5huJNM6qqxU9tOapryWeVhFSyEhX92QGksaWE1C-SygxvVVPi-fJmiZZxlU5vtE5IGGxXAsli4hN9s3_j09W7sm8OmufLvcZaAM8BCsdSHB8pnNLhJTma4eyZFiUxzxhx3IeHqIAS4MMpW8v3PWbT-gl1T0QsOF4LUuvXsukOciYxyDMa0xeeV1mCU3AZgtC8ge-f6QsbJChwufeake8TLUN6DuigAZhlSpDTITPoApcee8wFfR3lnWx9IyUNWdfuUCLR9YYgLC7R8F2hWDww45RRFAGlhPJoVmkTF2W9PZfPZCSNjh83porBxQqJd7qrBtkLkyXc_7ExTpgGn-Q6XSUPB9Uiy2AvUBtRBIsLXD"
region: "Berlin"
country: "Deutschland"
completed: "4140"
missions: "18"
date: "2018"
bg-link: "https://bannergress.com/banner/the-eye-of-the-eagle-066e"
onyx: "0"
description: "This is a 18 missions walk through the Fennpfuhl park. At the end you will have an eagle in your profile, the heraldic animal of Poland, Austria, Germany and many other countries."
lengthKMeters: "5,81"
title: "The Eye of the Eagle"
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

