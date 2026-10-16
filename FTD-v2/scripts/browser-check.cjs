// Verificação de navegador do FTD v2, por idioma: sem erro JS, sem recurso local 404, total de tópicos do curso,
// 7 tópicos + 7 links de TOC por módulo, jornada abre, sem overflow horizontal a 390px em TODAS as páginas.
// Uso: BASE_URL=http://127.0.0.1:8941 [LANG_PREFIX=en/] node scripts/browser-check.cjs
const {chromium}=require(process.env.PLAYWRIGHT_PATH||'/home/nmaldaner/projetos/timesmkt3/node_modules/playwright');
const fs=require('fs'),path=require('path');
const root=process.env.BASE_URL||'http://127.0.0.1:8941';
const pre=process.env.LANG_PREFIX||'';
const base=root+'/'+pre;
const C=JSON.parse(fs.readFileSync(path.join(__dirname,'../src/curso.json'),'utf8'));
const pages=['index.html'];
for(const t of C.tracks){pages.push(`curso/trilha${t.n}/index.html`);for(const m of t.modules)pages.push(`curso/trilha${t.n}/modulo-${m.id}.html`);}
(async()=>{
 const browser=await chromium.launch({headless:true});
 const fails=[];
 for(const [vp,label] of [[{width:1440,height:900},'desk'],[{width:390,height:844},'mob']]){
  const ctx=await browser.newContext({viewport:vp});
  const page=await ctx.newPage();
  let cur='';
  page.on('pageerror',e=>fails.push(`${label} ${cur}: JS ${e.message}`));
  page.on('response',r=>{const u=r.url();if(u.startsWith(root)&&r.status()>=400)fails.push(`${label} ${cur}: ${r.status()} ${u.slice(root.length)}`);});
  for(const p of pages){
   cur=p;
   await page.goto(base+p,{waitUntil:'load'});await page.waitForTimeout(150);
   const ov=await page.evaluate(()=>document.documentElement.scrollWidth-innerWidth);
   if(ov>1)fails.push(`${label} ${p}: overflow ${ov}px`);
   if(label==='mob')continue;
   const lang=await page.evaluate(()=>document.documentElement.lang);
   const want=pre?pre.slice(0,2):'pt-BR';if(lang!==want)fails.push(`${p}: html lang=${lang}`);
   if(p==='index.html'){
    const tot=await page.evaluate(()=>window.INEMA&&INEMA.progress('curso').total);
    if(tot!==C.tracks.length*9*7)fails.push(`landing: total de tópicos ${tot}`);
    await page.click('[data-inema-journey-open] >> nth=0');await page.waitForTimeout(200);
    if(!await page.locator('[role=dialog][aria-modal=true]').first().isVisible())fails.push('jornada não abriu');
    await page.keyboard.press('Escape');
   }
   if(/modulo-/.test(p)){
    const n=await page.locator('[data-inema-topic]').count();if(n!==7)fails.push(`${p}: ${n} tópicos`);
    const toc=await page.locator('[data-inema-toc] a').count();if(toc!==7)fails.push(`${p}: TOC ${toc}`);
   }
  }
  await ctx.close();
 }
 await browser.close();
 if(fails.length){console.error('FALHOU',pre||'pt/',fails.length,'\n'+fails.slice(0,60).join('\n'));process.exit(1);}
 console.log(`OK ${pre||'pt/'}: ${pages.length} páginas × 2 telas, sem erro JS, sem 404, sem overflow; tópicos e TOC conferidos.`);
})().catch(e=>{console.error('FALHOU',e.message);process.exit(1)});
