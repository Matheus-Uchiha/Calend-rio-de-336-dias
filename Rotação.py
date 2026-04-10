%%html
<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Calendário anual (336 dias) — com fases lunares</title>

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

  <style>
    :root{
      --paper:#ffffff;
      --ink:#0f121a;
      --muted:#5b6476;
      --line:#d7ddea;
      --wash:#f4f6fb;

      --nova:#0f172a;          /* new moon */
      --cresc:#1b4dff;         /* first quarter */
      --cheia:#c79a12;         /* full moon */
      --ming:#6d28d9;          /* last quarter */

      --radius: 16px;
    }

    /* Print setup */
    @page { size: A4; margin: 12mm; }
    * { box-sizing: border-box; }

    html, body { height: 100%; }
    body{
      margin:0;
      font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, "Helvetica Neue", sans-serif;
      color: var(--ink);
      background: linear-gradient(180deg, #eef2ff 0%, #ffffff 40%, #ffffff 100%);
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }

    header{
      padding: 18px 18px 10px;
      display:flex;
      align-items:flex-end;
      justify-content:space-between;
      gap: 16px;
      border-bottom: 1px solid var(--line);
      background:
        radial-gradient(900px 250px at 0% 0%, rgba(27,77,255,.12), transparent 60%),
        radial-gradient(700px 220px at 85% -10%, rgba(199,154,18,.10), transparent 55%),
        #fff;
    }

    .title{
      display:flex;
      flex-direction:column;
      gap: 8px;
      min-width: 0;
    }

    h1{
      margin:0;
      font-family: Fraunces, serif;
      font-weight: 800;
      letter-spacing: -0.02em;
      font-size: 22px;
      line-height: 1.05;
    }

    .subtitle{
      margin:0;
      color: var(--muted);
      font-size: 12px;
      line-height: 1.35;
      max-width: 85ch;
    }

    .print-actions{
      display:flex;
      gap: 10px;
      align-items:center;
      flex-wrap: wrap;
      justify-content:flex-end;
      text-align:right;
    }

    button{
      appearance:none;
      border: 1px solid var(--line);
      background: #fff;
      color: var(--ink);
      padding: 10px 12px;
      border-radius: 12px;
      font-weight: 700;
      font-size: 12px;
      cursor:pointer;
      box-shadow: 0 12px 24px rgba(15,18,26,.06);
    }
    button:hover{ transform: translateY(-1px); }
    button:active{ transform: translateY(0px); }

    .hint{
      color: var(--muted);
      font-size: 12px;
      line-height: 1.25;
      max-width: 26ch;
    }

    main{ padding: 12px 18px 16px; }

    .legend{
      display:flex;
      flex-wrap: wrap;
      gap: 10px 14px;
      align-items:center;
      padding: 10px 12px;
      border: 1px solid var(--line);
      border-radius: var(--radius);
      background: linear-gradient(180deg, rgba(244,246,251,.95), rgba(255,255,255,.95));
      margin-bottom: 10px;
    }
    .legend strong{
      font-size: 11px;
      letter-spacing: .08em;
      text-transform: uppercase;
      color: var(--muted);
      margin-right: 6px;
    }
    .chip{
      display:inline-flex;
      align-items:center;
      gap: 8px;
      padding: 6px 10px;
      border-radius: 999px;
      border: 1px solid var(--line);
      background: #fff;
      font-size: 12px;
      font-weight: 600;
      color: var(--ink);
    }
    .dot{
      width: 10px; height: 10px;
      border-radius: 999px;
      box-shadow: 0 6px 14px rgba(15,18,26,.10);
    }
    .dot.nova{ background: var(--nova); }
    .dot.cresc{ background: var(--cresc); }
    .dot.cheia{ background: var(--cheia); }
    .dot.ming{ background: var(--ming); }

    /* 12 months on A4: 3 columns x 4 rows */
    .months{
      display:grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
    }

    .month{
      background: var(--paper);
      border: 1px solid var(--line);
      border-radius: var(--radius);
      overflow:hidden;
      position:relative;
      box-shadow: 0 12px 24px rgba(15,18,26,.05);
    }

    .month::before{
      content:"";
      position:absolute;
      inset:0;
      background:
        radial-gradient(700px 200px at -25% -35%, rgba(27,77,255,.10), transparent 58%),
        radial-gradient(600px 220px at 120% 10%, rgba(109,40,217,.07), transparent 58%);
      pointer-events:none;
    }

    .month-header{
      position:relative;
      padding: 10px 12px;
      border-bottom: 1px solid var(--line);
      background: linear-gradient(180deg, rgba(244,246,251,.92), rgba(255,255,255,.92));
      backdrop-filter: blur(6px);
    }

    .month-name{
      margin:0;
      font-family: Fraunces, serif;
      font-size: 14px;
      letter-spacing: -0.01em;
      font-weight: 800;
      display:flex;
      align-items:baseline;
      justify-content:space-between;
      gap: 10px;
    }

    .month-meta{
      font-family: Inter, sans-serif;
      font-size: 11px;
      color: var(--muted);
      font-weight: 700;
      white-space:nowrap;
    }

    table{
      width:100%;
      border-collapse: collapse;
      position:relative;
      background: rgba(255,255,255,.94);
    }

    thead th{
      font-size: 10px;
      text-transform: uppercase;
      letter-spacing: .08em;
      color: var(--muted);
      font-weight: 800;
      padding: 7px 0;
      background: var(--wash);
      border-bottom: 1px solid var(--line);
    }

    tbody td{
      width: calc(100%/7);
      height: 27px;
      text-align: center;
      vertical-align: middle;
      font-size: 11px;
      padding: 0;
      border-bottom: 1px solid var(--line);
      border-right: 1px solid var(--line);
      position: relative;
    }
    tbody tr:last-child td{ border-bottom: none; }
    tbody td:last-child{ border-right: none; }

    .day{
      display:inline-flex;
      width: 22px;
      height: 22px;
      border-radius: 8px;
      align-items:center;
      justify-content:center;
      font-weight: 700;
      color: var(--ink);
      position: relative;
      z-index: 1;
    }

    /* Weekends */
    .sunday .day{ color: var(--cresc); }
    .saturday .day{ color: #1f2a44; }

    /* Moon marker */
    .moon::after{
      content:"";
      position:absolute;
      top: 5px;
      right: 5px;
      width: 7px;
      height: 7px;
      border-radius: 999px;
      background: var(--line);
      box-shadow: 0 8px 16px rgba(15,18,26,.10);
    }
    .moon.nova::after{ background: var(--nova); }
    .moon.cresc::after{ background: var(--cresc); }
    .moon.cheia::after{ background: var(--cheia); }
    .moon.ming::after{ background: var(--ming); }

    /* Subtle highlight to make phases readable in print */
    .moon .day{
      background: rgba(15,18,26,.03);
      outline: 1px solid rgba(15,18,26,.10);
      outline-offset: 0px;
    }
    .moon.nova .day{
      background: rgba(15,23,42,.07);
      outline-color: rgba(15,23,42,.18);
    }
    .moon.cresc .day{
      background: rgba(27,77,255,.08);
      outline-color: rgba(27,77,255,.18);
    }
    .moon.cheia .day{
      background: rgba(199,154,18,.10);
      outline-color: rgba(199,154,18,.22);
    }
    .moon.ming .day{
      background: rgba(109,40,217,.08);
      outline-color: rgba(109,40,217,.18);
    }

    footer{
      padding: 10px 18px 16px;
      color: var(--muted);
      font-size: 11px;
      border-top: 1px solid var(--line);
      display:flex;
      justify-content:space-between;
      gap: 12px;
    }

    @media (max-width: 980px){
      .months{ grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 640px){
      header{ flex-direction:column; align-items:flex-start; }
      .print-actions{ width:100%; justify-content:space-between; text-align:left; }
      .months{ grid-template-columns: 1fr; }
      tbody td{ height: 32px; }
    }

    @media print{
      body{ background:#fff; }
      .print-actions{ display:none !important; }
      header{ padding: 0 0 8px; margin-bottom: 8px; border-bottom: 1px solid #cfd6e4; background:#fff; }
      main{ padding: 0; }
      .legend{ margin: 0 0 8px; box-shadow:none; }
      .months{ gap: 8px; }
      .month{ box-shadow:none; }
      footer{ padding: 8px 0 0; }
    }
  </style>
</head>

<body>
  <header>
    <div class="title">
      <h1>Calendário anual — 336 dias (12×28) com fases lunares</h1>
      <p class="subtitle">
        Estrutura fixa: <strong>12 meses</strong> de <strong>28 dias</strong> (4 semanas). Padrão lunar mensal:
        <strong>Dia 1</strong> Lua Nova, <strong>Dia 8</strong> Quarto Crescente, <strong>Dia 15</strong> Lua Cheia,
        <strong>Dia 22</strong> Quarto Minguante. Como 28 é múltiplo de 7, o mês sempre começa no <strong>Domingo</strong>.
      </p>
    </div>

    <div class="print-actions">
      <button type="button" id="btnPrint">Imprimir / Salvar como PDF</button>
      <div class="hint">No navegador: Ctrl+P → Destino “Salvar como PDF”</div>
    </div>
  </header>

  <main>
    <section class="legend" aria-label="Legenda das fases lunares">
      <strong>Legenda</strong>
      <span class="chip"><span class="dot nova" aria-hidden="true"></span>Lua Nova (dia 1)</span>
      <span class="chip"><span class="dot cresc" aria-hidden="true"></span>Quarto Crescente (dia 8)</span>
      <span class="chip"><span class="dot cheia" aria-hidden="true"></span>Lua Cheia (dia 15)</span>
      <span class="chip"><span class="dot ming" aria-hidden="true"></span>Quarto Minguante (dia 22)</span>
    </section>

    <section class="months" id="months" aria-label="Grade de meses do calendário"></section>
  </main>

  <footer>
    <div>48 semanas/ano • Sem dias extras • Fases lunares sincronizadas com meses</div>
    <div>Semana: Dom · Seg · Ter · Qua · Qui · Sex · Sáb</div>
  </footer>

  <script>
    const monthNames = [
      "Janeiro","Fevereiro","Março","Abril","Maio","Junho",
      "Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"
    ];

    const weekdays = ["Dom","Seg","Ter","Qua","Qui","Sex","Sáb"];

    // Fixed lunar phases in this universe:
    // 1 New, 8 First Quarter, 15 Full, 22 Last Quarter
    const moonDays = new Map([
      [1, "nova"],
      [8, "cresc"],
      [15, "cheia"],
      [22, "ming"]
    ]);

    function buildMonthTable() {
      const table = document.createElement("table");

      const thead = document.createElement("thead");
      const trh = document.createElement("tr");
      weekdays.forEach(d => {
        const th = document.createElement("th");
        th.scope = "col";
        th.textContent = d;
        trh.appendChild(th);
      });
      thead.appendChild(trh);
      table.appendChild(thead);

      const tbody = document.createElement("tbody");

      let day = 1;
      for (let r = 0; r < 4; r++) {
        const tr = document.createElement("tr");
        for (let c = 0; c < 7; c++) {
          const td = document.createElement("td");

          // weekend classes
          if (c === 0) td.classList.add("sunday");
          if (c === 6) td.classList.add("saturday");

          // moon phase marker
          if (moonDays.has(day)) {
            td.classList.add("moon", moonDays.get(day));
            const label = ({
              nova: "Lua Nova",
              cresc: "Quarto Crescente",
              cheia: "Lua Cheia",
              ming: "Quarto Minguante"
            })[moonDays.get(day)];
            td.setAttribute("aria-label", `Dia ${day} — ${label}`);
            td.title = `${label} (dia ${day})`;
          } else {
            td.setAttribute("aria-label", `Dia ${day}`);
          }

          const span = document.createElement("span");
          span.className = "day";
          span.textContent = day;

          td.appendChild(span);
          tr.appendChild(td);
          day++;
        }
        tbody.appendChild(tr);
      }

      table.appendChild(tbody);
      return table;
    }

    const monthsEl = document.getElementById("months");
    monthNames.forEach((name, idx) => {
      const wrap = document.createElement("article");
      wrap.className = "month";
      wrap.setAttribute("aria-label", `Mês: ${name}`);

      const header = document.createElement("div");
      header.className = "month-header";

      const h = document.createElement("h2");
      h.className = "month-name";
      h.innerHTML = `<span>${name}</span><span class="month-meta">Mês ${idx+1} • 28 dias</span>`;

      header.appendChild(h);
      wrap.appendChild(header);
      wrap.appendChild(buildMonthTable());
      monthsEl.appendChild(wrap);
    });

    document.getElementById("btnPrint").addEventListener("click", () => window.print());
  </script>
</body>
</html>
