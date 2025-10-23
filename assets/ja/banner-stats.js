<script>
// Minimal, vanilla JS – keine Abhängigkeiten
(function(){
  function pct(part, total){ return total ? ((part/total)*100).toFixed(1) : "0.0"; }

  function renderTable(el, rows, total){
    const wrap = document.createElement("div");
    wrap.className = "bs-table-wrap";
    const table = document.createElement("table");
    table.className = "bs-table";
    table.innerHTML = `
      <thead><tr>
        <th style="text-align:left">Name</th>
        <th style="text-align:right">Banner</th>
        <th style="text-align:right">Anteil %</th>
      </tr></thead>
      <tbody></tbody>`;
    const tb = table.querySelector("tbody");
    rows.forEach(r=>{
      const tr = document.createElement("tr");
      tr.innerHTML = `
        <td>${r.name || "—"}</td>
        <td style="text-align:right">${r.count}</td>
        <td style="text-align:right">${pct(r.count,total)}</td>`;
      tb.appendChild(tr);
    });
    wrap.appendChild(table);
    el.appendChild(wrap);
  }

  function renderCollapsible(el, title, rows, total){
    const det = document.createElement("details");
    det.className = "bs-details";
    const sum = document.createElement("summary");
    sum.textContent = title;
    det.appendChild(sum);

    // Suche/Filter
    const search = document.createElement("input");
    search.type = "search";
    search.placeholder = "Suchen …";
    search.className = "bs-search";
    det.appendChild(search);

    const container = document.createElement("div");
    det.appendChild(container);

    function draw(filtered){
      container.innerHTML = "";
      renderTable(container, filtered, total);
    }

    // alphabetisch (Name), sekundär nach Anzahl absteigend
    const base = rows.slice().sort((a,b)=>{
      const an = (a.name||"").toLowerCase(), bn=(b.name||"").toLowerCase();
      if(an<bn) return -1; if(an>bn) return 1; return (b.count||0)-(a.count||0);
    });

    draw(base);

    search.addEventListener("input", ()=>{
      const q = search.value.trim().toLowerCase();
      if(!q){ draw(base); return; }
      const f = base.filter(r => (r.name||"").toLowerCase().includes(q));
      draw(f);
    });

    el.appendChild(det);
  }

  function renderStats(root){
    const topN = parseInt(root.dataset.top || "20", 10);
    const title = root.dataset.title || "Einträge";
    const dataScriptId = root.dataset.src;
    const dataNode = document.getElementById(dataScriptId);
    if(!dataNode){ console.warn("banner-stats: Datenquelle nicht gefunden:", dataScriptId); return; }
    let data = [];
    try { data = JSON.parse(dataNode.textContent || "[]"); } catch(e){ console.error(e); }
    if(!Array.isArray(data) || !data.length){ return; }

    const total = data.reduce((s,r)=> s + (r.count||0), 0);
    const sorted = data.slice().sort((a,b)=> (b.count||0)-(a.count||0));
    const top = sorted.slice(0, topN);
    const rest = sorted.slice(topN);

    // Überschrift
    const h3 = document.createElement("h3");
    h3.textContent = `${title} – Top ${topN} (von ${data.length})`;
    root.appendChild(h3);

    // Top-Tabelle
    renderTable(root, top, total);

    // Rest ausklappbar
    if(rest.length){
      renderCollapsible(root, `Weitere ${title} (${rest.length}) – anklicken`, rest, total);
    }
  }

  function boot(){
    document.querySelectorAll("[data-banner-stats='json']").forEach(renderStats);
  }

  if(document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", boot);
  } else { boot(); }
})();
</script>
