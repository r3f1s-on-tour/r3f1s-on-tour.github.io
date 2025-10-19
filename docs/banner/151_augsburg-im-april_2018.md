---
nummer: "151"
startLatitude: "48.367894"
startLongitude: "10.894525"
titel: "Augsburg im April"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_bWv1tjnOmcIZO2_4R6APdDxC5n5FxXwvCdRoN8dxbi5wC7zVX6RMDcoNrlpnSMWExnOTTzmvdw9iI3HxlxoB1zVz9hwKHMQoVEA0hKik-syWMHjLTrm6vykx8mhIM4dgVTeq1_M9mEW9ful4_sEtqg0OhgFg9vep7YrDvtZz6tG7R6JftJlU7aSCGFZ_yu8VpiXl5nu-e6lvOLMbaYKI8WsR_ICWbhzNsrWLhoydUW-juIx-yoXmVvb0of71c7Tvinq5_QF_sdvFZcN7J5ObT12oQCMyNsj6NNGbx_NKb4igl49M-nrBqttxE_RtKerjq0ySCNzBr9eyRL30rab9oKesWuPH7BLnYZZFoavI90isjnZOXnyxpIRXpcZNwKtuL-60C6-nnTKwtr1QWGchAN__7QBlAB3oO3G_4CZX1znb6olx7SzIRcXuF9ro7cqrJKIbww7UET9MYfALGeCpXdJWQunosQf-EjjijO7LY77reEnZrVj82bJgCdYw8rn4_dNRN8YFWn-IRtwU3lbBUX4A0mmFO0iJYFEZbWhqiR35vEJ7cVxvSVPskbqILmiLb7V2ngLUxNkvNT1ryDTwsGYLKMIn5bvz4anj803dC1BhX9gyzId1f2DqZRwh3IVXABV00YOj6rSzmzMDqWLZccfOyNoSyzehe3dSC5KMnYZYi0QwI_XtABY0qolhpPVzPrRIkwEpejic7vldMz10bxJP7sl2Ucd30-wVdbxvgpzZ2aMRmId4JEqT8aobmrIfOZ-J0TMAdwCtvadg8fu0wJWGdbYMRfQlAx9hiaZgRUfDIxY0qMRmP5AbdgXyMopPjLwgONRJvaXTDlkJAcqN_q165CVx_rqWLy"
region: "Augsburg"
country: "Deutschland"
completed: "3690"
missions: "30"
date: "2018"
bg-link: ""
onyx: "0"
description: ""
lengthKMeters: ""
title: "Augsburg im April"
---

# {{ page.meta.title }}
_**Datum:** {{ page.meta.date }} • **Country:** {{ page.meta.country }}_

## Bild
![{{ page.meta.title | default('Bild') }}]({{ page.meta.picture }})

## Infos
- **nummer**: {{ page.meta.nummer }}
- **startLatitude**: {{ page.meta.startLatitude }}
- **startLongitude**: {{ page.meta.startLongitude }}
- **region**: {{ page.meta.region }}
- **country**: {{ page.meta.country }}
- **completed**: {{ page.meta.completed }}
- **missions**: {{ page.meta.missions }}
- **onyx**: {{ page.meta.onyx }}

