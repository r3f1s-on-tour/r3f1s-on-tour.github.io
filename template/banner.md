# {{__TITLE__}}

*{{__DATE_DE__}}*{{__IF:region__}} • {{__VAL:region__}}{{__/IF__}}{{__IF:country__}} • {{__VAL:country__}}{{__/IF__}}

{{__IMG:picture__}}

{{__IF:notice__}}
<div style="
  margin: 10px 0 18px;
  padding: 12px 14px;
  border: 2px solid #FFD500;
  background-color: #000;
  color: #fff;
  border-radius: 8px;
  font-weight: 500;
  line-height: 1.6;
">
  ⚠️ <strong>Notice:</strong><br>
  {{__VALBRLINKS:notice__}}
</div>
{{__/IF__}}

## Details
{{__IF:lengthKMeters__}}- **Distance (km):** {{__VAL2DP:lengthKMeters__}}{{__/IF__}}
{{__IF:missions__}}- **Missions in banner:** {{__VAL:missions__}}{{__/IF__}}
{{__IF:completed__}}- **Total missions completed:** {{__VAL:completed__}}{{__/IF__}}
{{__IF:NUMBER__}}- **This is my banner no.:** {{__VAL:NUMBER__}}{{__/IF__}}
{{__IF:missionDay__}}- **Mission Day:** {{__VALYESNO:missionDay__}}{{__/IF__}}

{{__IF:description__}}
## Description
{{__VALBR:description__}}
{{__/IF__}}

{{__IFANY:bg-link,umap,trips__}}
## Links
{{__IF:bg-link__}}<a href="{{__VAL:bg-link__}}" style="display:inline-block;margin:6px 8px 0 0;padding:6px 12px;background:#3c8b3c;color:#fff;text-decoration:none;border-radius:6px;">🔗 Bannergress</a>{{__/IF__}}
{{__IF:umap__}}<a href="{{__VAL:umap__}}" style="display:inline-block;margin:6px 8px 0 0;padding:6px 12px;background:#0066cc;color:#fff;text-decoration:none;border-radius:6px;">🗺️ uMap</a>{{__/IF__}}
{{__IF:trips__}}<a href="{{__VAL:trips__}}" style="display:inline-block;margin:6px 8px 0 0;padding:6px 12px;background:#8a2be2;color:#fff;text-decoration:none;border-radius:6px;">🧭 Trips</a>{{__/IF__}}
{{__/IFANY__}}

> File: 
```
• {{__FILENAME__}}
• #{{__NUMBER__}} 
• Slug: `{{__SLUG__}}
```
