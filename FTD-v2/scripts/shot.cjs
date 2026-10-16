// Captura de tela para conferência visual (não vai para produção).
// Uso: BASE_URL=http://127.0.0.1:8941 node scripts/shot.cjs <saida-dir> <pagina> [<pagina> ...]
// Gera <nome>-desk-dark.png, -desk-light.png e -mob-dark.png (só a primeira tela + um trecho do meio).
const {chromium}=require(process.env.PLAYWRIGHT_PATH||'/home/nmaldaner/projetos/timesmkt3/node_modules/playwright');
const fs=require('fs'),path=require('path');
const base=(process.env.BASE_URL||'http://127.0.0.1:8941')+'/';
const [out,...pages]=process.argv.slice(2);
(async()=>{
 fs.mkdirSync(out,{recursive:true});
 const browser=await chromium.launch({headless:true});
 for(const p of pages){
  const name=p.replace(/[\/.]/g,'_');
  for(const [tag,vp,theme] of [['desk-dark',{width:1440,height:900},'inema-dark'],['desk-light',{width:1440,height:900},'claro'],['mob-dark',{width:390,height:844},'inema-dark']]){
   const ctx=await browser.newContext({viewport:vp});
   await ctx.addInitScript(t=>{try{localStorage.setItem('inema.prefs',JSON.stringify({theme:t}))}catch(e){}},theme);
   const page=await ctx.newPage();const errs=[];page.on('pageerror',e=>errs.push(e.message));
   await page.goto(base+p,{waitUntil:'networkidle'});await page.waitForTimeout(400);
   const ov=await page.evaluate(()=>document.documentElement.scrollWidth-innerWidth);
   await page.screenshot({path:path.join(out,`${name}-${tag}.png`)});
   const y=process.env.SCROLL_Y; if(y){await page.evaluate(v=>scrollTo(0,+v),y);await page.waitForTimeout(200);await page.screenshot({path:path.join(out,`${name}-${tag}-y${y}.png`)});}
   console.log(p,tag,'overflow',ov,'erros',errs.length?errs:0);
   await ctx.close();
  }
 }
 await browser.close();
})().catch(e=>{console.error('FALHOU',e.message);process.exit(1)});
