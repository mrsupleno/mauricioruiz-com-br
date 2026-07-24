#!/usr/bin/env python3
"""Base compartilhada das páginas internas — extraída da home publicada."""
import re, pathlib

HOME = pathlib.Path("/root/projects/mauricioruiz-com-br/index.html").read_text(encoding="utf-8")

# CSS completo do segundo <style> no head (o primeiro é o reset inline do head_extra)
_css_blocks = re.findall(r"<style>(.*?)</style>", HOME, re.S)
CSS = max(_css_blocks, key=len)

# Header
HEADER = re.search(r"(<header.*?</header>)", HOME, re.S).group(1)
# Nos links internos do menu, âncoras passam a apontar para a home
HEADER = HEADER.replace('href="#confronto"', 'href="/#confronto"')
HEADER = HEADER.replace('href="#mentoria"', 'href="/mentoria-implantacao-ia/"')
HEADER = HEADER.replace('href="#agentes"', 'href="/agentes-de-ia/"')
HEADER = HEADER.replace('href="#servicos"', 'href="/#servicos"')
HEADER = HEADER.replace('href="#sobre"', 'href="/sobre/"')
HEADER = HEADER.replace('href="#conteudos"', 'href="/#conteudos"')
HEADER = HEADER.replace('href="#contato"', 'href="/contato/"')
HEADER = HEADER.replace('href="#diagnostico"', 'href="/diagnostico-de-ia/"')
HEADER = HEADER.replace('href="#topo"', 'href="/"')

# Footer
FOOTER = re.search(r'(<footer.*?</footer>)', HOME, re.S).group(1)

# JS compartilhado (menu mobile + form), adaptado p/ subject configurável
JS_MENU = """
(function(){
  var burger=document.getElementById('burgerBtn');
  var menu=document.getElementById('mobileMenu');
  burger.addEventListener('click',function(){
    var open=menu.style.display==='flex';
    menu.style.display=open?'none':'flex';
    burger.setAttribute('aria-expanded',String(!open));
  });
  menu.querySelectorAll('a').forEach(function(a){
    a.addEventListener('click',function(){
      menu.style.display='none';
      burger.setAttribute('aria-expanded','false');
    });
  });
})();
"""

JS_FORM = """
(function(){
  var form=document.getElementById('diagForm');
  if(!form){return;}
  form.addEventListener('submit',function(e){
    e.preventDefault();
    var f=e.target;
    if(f.querySelector('[name=_honey]').value){return;}
    var btn=f.querySelector('button[type=submit]');
    btn.disabled=true;btn.textContent='Enviando...';
    var fd=new FormData(f);
    fd.delete('_honey');
    fetch('https://formsubmit.co/ajax/mauricio@sucesso.com.br',{
      method:'POST',headers:{'Accept':'application/json'},body:fd
    }).then(function(r){
      if(!r.ok){throw new Error('HTTP '+r.status);}
      f.innerHTML='<div style="text-align:center;padding:24px 0;grid-column:1/-1;"><p style="color:#3A606F;font-size:20px;font-weight:700;margin-bottom:10px;">Solicitação recebida.</p><p style="color:#B0BDCA;font-size:15px;">Entraremos em contato dentro do horário comercial: segunda a sexta, das 9h às 18h.</p></div>';
    }).catch(function(){
      btn.disabled=false;btn.textContent=btn.dataset.label||'Solicitar diagnóstico de IA';
      alert('Não foi possível enviar agora. Tente novamente ou fale direto pelo WhatsApp (27) 92000-0167.');
    });
  });
})();
"""

def head(title, desc, canonical, extra_css="", schemas=None):
    schema_html = ""
    for s in (schemas or []):
        schema_html += f'\n<script type="application/ld+json">\n{s}\n</script>'
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://mauricioruiz.com.br{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://mauricioruiz.com.br{canonical}">
<meta property="og:locale" content="pt_BR">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="192x192" href="/assets/favicon-logo-c-192.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon-logo-c.png">
<meta property="og:image" content="https://mauricioruiz.com.br/assets/mauricio-ruiz-og-miniatura-final.jpg">
<meta property="og:image:secure_url" content="https://mauricioruiz.com.br/assets/mauricio-ruiz-og-miniatura-final.jpg">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1280">
<meta property="og:image:height" content="672">
<meta property="og:image:alt" content="Mauricio Ruiz — Mentor de Inteligência Artificial e Automação Empresarial">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Mauricio Ruiz | IA e Automação Empresarial">
<meta name="twitter:description" content="Estratégia antes da ferramenta. Mentoria, agentes de IA e automações para reduzir tarefas repetitivas e transformar tecnologia em resultado.">
<meta name="twitter:image" content="https://mauricioruiz.com.br/assets/mauricio-ruiz-og-miniatura-final.jpg">
<meta name="theme-color" content="#133A58">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>{CSS}
{extra_css}</style>{schema_html}
</head>
<body>
<a href="#conteudo" class="skip-link">Pular para o conteúdo</a>
"""

def breadcrumb(items):
    """items: lista de (label, url|None). Último é a página atual."""
    lis = []
    for i, (label, url) in enumerate(items):
        if url:
            lis.append(f'<a href="{url}" style="color:#667085;">{label}</a><span style="color:#B0BDCA;margin:0 8px;">/</span>')
        else:
            lis.append(f'<span style="color:#133A58;font-weight:600;">{label}</span>')
    return f'''<nav aria-label="Breadcrumb" style="background:#F6F8FA;border-bottom:1px solid #B0BDCA;padding:12px 24px;font-size:13.5px;">
  <div style="max-width:1200px;margin:0 auto;">{''.join(lis)}</div>
</nav>'''

def breadcrumb_schema(items):
    import json
    els = []
    for i, (label, url) in enumerate(items):
        els.append({"@type":"ListItem","position":i+1,"name":label,
                    **({"item":f"https://mauricioruiz.com.br{url}"} if url else {})})
    return json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":els}, ensure_ascii=False, indent=1)

def faq_html(faqs, bg="#F6F8FA"):
    items = "\n".join(f'''<details style="background:#fff;border:1px solid #B0BDCA;border-radius:12px;overflow:hidden;">
  <summary style="text-align:left;padding:20px 22px;font-size:16px;font-weight:600;color:#133A58;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:16px;list-style:none;">
    <span>{q}</span><span class="faq-icon" style="color:#3A606F;font-size:18px;flex-shrink:0;">+</span>
  </summary>
  <p style="padding:0 22px 22px;font-size:15px;line-height:1.7;color:#475467;margin:0;">{a}</p>
</details>''' for q, a in faqs)
    return f'''<section style="background:{bg};padding:88px 24px;">
  <div style="max-width:840px;margin:0 auto;">
    <h2 style="font-size:34px;font-weight:700;color:#133A58;margin-bottom:36px;">Perguntas frequentes</h2>
    <div style="display:flex;flex-direction:column;gap:12px;">
{items}
    </div>
  </div>
</section>'''

def faq_schema(faqs):
    import json
    return json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs
    ]}, ensure_ascii=False, indent=1)

CTA_DIAG = """
<section style="background:#133A58;padding:88px 24px;">
  <div style="max-width:900px;margin:0 auto;text-align:center;">
    <h2 style="font-size:32px;font-weight:700;color:#fff;margin-bottom:18px;">Antes de contratar outra ferramenta, descubra onde a IA realmente pode gerar resultado</h2>
    <p style="font-size:17px;line-height:1.7;color:#98A2B3;max-width:640px;margin:0 auto 36px;">O diagnóstico identifica os processos mais promissores, os riscos, as prioridades e os primeiros projetos que podem ser implantados.</p>
    <a href="/diagnostico-de-ia/" style="display:inline-block;background:#133A58;color:#fff;font-weight:700;font-size:16px;padding:16px 30px;border-radius:8px;">Solicitar diagnóstico de IA</a>
    <div style="margin-top:24px;">
      <a href="https://wa.me/5527920000167" target="_blank" rel="noopener" style="color:#fff;font-weight:700;font-size:15px;">Prefere falar direto? Falar pelo WhatsApp →</a>
    </div>
  </div>
</section>"""

def page(title, desc, canonical, main_html, schemas=None, extra_css=""):
    return (head(title, desc, canonical, extra_css, schemas)
            + HEADER
            + f'<main id="conteudo">\n{main_html}\n</main>\n'
            + FOOTER
            + f"\n<script>{JS_MENU}</script>\n<script>{JS_FORM}</script>\n</body>\n</html>\n")

def write(path, content):
    p = pathlib.Path("/root/projects/mauricioruiz-com-br") / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    print(f"  {path} ({len(content)} b)")
