# {{__TITLE__}}

*{{__DATE_DE__}}*{{__IF:region__}} • {{__VAL:region__}}{{__/IF__}}{{__IF:country__}} • {{__VAL:country__}}{{__/IF__}}

{{__IMG:picture__}}

## Details
{{__IF:lengthKMeters__}}- **Distance (km):** {{__VAL2DP:lengthKMeters__}}{{__/IF__}}
{{__IF:missionsCount__}}- **Missions in banner:** {{__VAL:missionsCount__}}{{__/IF__}}
{{__IF:completed__}}- **Total missions completed:** {{__VAL:ompleted__}}{{__/IF__}}
{{__IF:nummer__}}- **This is my banner no.:** {{__VAL:nummer__}}{{__/IF__}}

{{__IF:description__}}
!!! note "Description"
    {{__VALBR:description__}}
{{__/IF__}}

{{__IFANY:bg-link,umap__}}
## Links
{{__IF:bg-link__}}[🔗 Bannergress]({{__VAL:bg-link__}}){ .md-button .md-button--primary }{{__/IF__}}
{{__IF:umap__}}[🗺️ uMap]({{__VAL:umap__}}){ .md-button }{{__/IF__}}
{{__/IFANY__}}

> File: `{{__FILENAME__}}` • #{{__NUMBER__}} • Slug: `{{__SLUG__}}`
