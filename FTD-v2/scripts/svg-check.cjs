// Mede rótulos de SVG que transbordam: texto fora do viewBox ou mais largo que o <rect> que o contém.
// Compara cada idioma com o PT (mesmo índice de figura/texto) e lista só o que piorou na tradução.
// Uso: BASE_URL=http://127.0.0.1:8941 node scripts/svg-check.cjs
const {chromium}=require(process.env.PLAYWRIGHT_PATH||'/home/nmaldaner/projetos/timesmkt3/node_modules/playwright');
const fs=require('fs'),path=require('path');
const root=process.env.BASE_URL||'http://127.0.0.1:8941';
const C=JSON.parse(fs.readFileSync(path.join(__dirname,'../src/curso.json'),'utf8'));
const pages=['index.html'];
for(const t of C.tracks){pages.push(`curso/trilha${t.n}/index.html`);for(const m of t.modules)pages.push(`curso/trilha${t.n}/modulo-${m.id}.html`);}
function probe(){
 const out=[];
 document.querySelectorAll('svg[role=img]').forEach((svg,fi)=>{
  const vb=svg.viewBox.baseVal;if(!vb||!vb.width)return;
  const rects=[...svg.querySelectorAll('rect')].map(r=>{try{return r.getBBox()}catch(e){return null}}).filter(b=>b&&b.width<vb.width*0.9&&b.height<vb.height*0.9);
  svg.querySelectorAll('text').forEach((t,ti)=>{
   let b;try{b=t.getBBox()}catch(e){return}
   if(!b.width)return;
   let bad=0;
   if(b.x<vb.x-1||b.x+b.width>vb.x+vb.width+1)bad=Math.max(bad,Math.round(Math.max(vb.x-b.x,b.x+b.width-vb.x-vb.width)));
   const cx=b.x+b.width/2,cy=b.y+b.height/2;
   const box=rects.filter(r=>cx>=r.x&&cx<=r.x+r.width&&cy>=r.y&&cy<=r.y+r.height).sort((a,c)=>a.width*a.height-c.width*c.height)[0];
   if(box){const over=Math.max(box.x-b.x,b.x+b.width-box.x-box.width);if(over>2)bad=Math.max(bad,Math.round(over));}
   out.push({fi,ti,bad,txt:t.textContent.trim().slice(0,50)});
  });
 });
 return out;
}
(async()=>{
 const browser=await chromium.launch({headless:true});const page=await browser.newPage({viewport:{width:1440,height:900}});
 let total=0;
 for(const p of pages){
  const res={};
  for(const L of ['','en/','es/']){await page.goto(root+'/'+L+p,{waitUntil:'load'});res[L]=await page.evaluate(probe);}
  for(const L of ['en/','es/']){
   for(const r of res[L]){
    const pt=res[''].find(x=>x.fi===r.fi&&x.ti===r.ti);
    if(r.bad>(pt?pt.bad:0)+2){total++;console.log(`${L}${p} fig${r.fi} +${r.bad}px «${r.txt}»  (PT: «${pt?pt.txt:''}»)`);}
   }
  }
 }
 await browser.close();console.log(total+' rótulos piores que o PT');process.exit(total?1:0);
})().catch(e=>{console.error('FALHOU',e.message);process.exit(2)});
