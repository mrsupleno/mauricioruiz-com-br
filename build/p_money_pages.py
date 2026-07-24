#!/usr/bin/env python3
"""Gera money pages SEO entregues pelo Link Flow para mauricioruiz.com.br."""
import sys, json, html, re
from pathlib import Path
sys.path.insert(0, "/root/projects/mauricioruiz-com-br/build")
from base import page, breadcrumb, breadcrumb_schema, faq_html, faq_schema, CTA_DIAG, write

DATA_PATH = Path("/root/link-flow/projetos/mauricio-ruiz-mentor-ia/entregas/money-pages.json")
DATA = json.loads(DATA_PATH.read_text(encoding="utf-8"))
WA = DATA.get("nap", {}).get("whatsapp", "https://wa.me/5527920000167")
TEL = DATA.get("nap", {}).get("telefone", "+55-27-92000-0167")
ADDR = DATA.get("nap", {})

AREA_NACIONAL = ["Brasil"]
AREA_GRANDE_VITORIA = ["Vila Velha", "Vitória", "Serra", "Cariacica", "Viana", "Grande Vitória", "Espírito Santo"]


def _inline_md(text):
    text = html.escape(text or "")
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    return text


def md_to_html(md):
    parts = re.split(r"\n\s*\n", (md or "").strip())
    out = []
    for part in parts:
        lines = [ln.strip() for ln in part.splitlines() if ln.strip()]
        if not lines:
            continue
        if all(ln.startswith(("- ", "• ")) for ln in lines):
            items = "".join(f"<li>{_inline_md(ln[2:].strip())}</li>" for ln in lines)
            out.append(f'<ul style="margin:0 0 18px 20px;color:#475467;font-size:16.5px;line-height:1.75;">{items}</ul>')
        else:
            out.append(f'<p style="font-size:16.5px;line-height:1.75;color:#475467;margin:0 0 18px;">{_inline_md(" ".join(lines))}</p>')
    return "\n".join(out)


def clean_slug(slug):
    return "/" + slug.strip("/") + "/"


def area_for(item):
    if clean_slug(item["slug"]) == "/consultoria-de-ia-vila-velha-es/":
        return AREA_GRANDE_VITORIA
    return AREA_NACIONAL


def service_schema(item):
    slug = clean_slug(item["slug"])
    area = area_for(item)
    provider = {
        "@type": "ProfessionalService",
        "@id": "https://mauricioruiz.com.br/#profissional",
        "name": "Mauricio Ruiz | Mentor de Inteligência Artificial",
        "url": "https://mauricioruiz.com.br/",
        "telephone": TEL,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": ADDR.get("endereco", "Rua Marajó, 77, Unidade 402"),
            "addressLocality": ADDR.get("cidade", "Vila Velha"),
            "addressRegion": ADDR.get("uf", "ES"),
            "postalCode": ADDR.get("cep", "29101-250"),
            "addressCountry": "BR"
        },
        "openingHours": ADDR.get("opening_hours", "Mo-Fr 09:00-18:00"),
        "areaServed": area,
    }
    service = {
        "@type": "Service",
        "@id": f"https://mauricioruiz.com.br{slug}#servico",
        "name": item["h1"],
        "description": item["meta_description"],
        "provider": {"@id": "https://mauricioruiz.com.br/#profissional"},
        "areaServed": area,
        "url": f"https://mauricioruiz.com.br{slug}",
    }
    return json.dumps({"@context":"https://schema.org", "@graph":[provider, service]}, ensure_ascii=False, indent=1)


def hero(item):
    escopo = "Consultoria nacional" if item.get("escopo") == "nacional" else "Grande Vitória"
    vol = item.get("volume_mes")
    diff = item.get("dificuldade")
    metric = ""
    if vol not in (None, ""):
        metric = f" · {vol} buscas/mês" + (f" · dificuldade {diff}" if diff not in (None, "") else "")
    return f'''
<section style="background:#ffffff;padding:72px 24px 82px;">
  <div style="max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1.05fr .95fr;gap:48px;align-items:center;" class="g-hero">
    <div>
      <span style="display:inline-block;background:#F6F8FA;border:1px solid #B0BDCA;color:#3A606F;font-size:13px;font-weight:800;padding:7px 14px;border-radius:100px;margin-bottom:20px;">{html.escape(escopo + metric)}</span>
      <h1 style="font-size:44px;line-height:1.14;font-weight:800;color:#133A58;margin-bottom:24px;max-width:820px;">{html.escape(item['h1'])}</h1>
      <div style="font-size:18px;line-height:1.7;color:#475467;max-width:720px;margin-bottom:32px;">{md_to_html(item.get('introducao_md',''))}</div>
      <div style="display:flex;flex-wrap:wrap;gap:14px;">
        <a href="/diagnostico-de-ia/" style="background:#133A58;color:#fff;font-weight:800;font-size:16px;padding:16px 26px;border-radius:8px;box-shadow:0 10px 24px rgba(19,58,88,.24);">Solicitar diagnóstico de IA</a>
        <a href="{html.escape(WA)}" target="_blank" rel="noopener" style="background:#fff;border:1px solid #B0BDCA;color:#133A58;font-weight:700;font-size:16px;padding:16px 26px;border-radius:8px;">Falar pelo WhatsApp</a>
      </div>
    </div>
    <aside style="background:linear-gradient(135deg,#133A58 0%,#2C4964 52%,#3A606F 100%);border-radius:20px;padding:34px;box-shadow:0 24px 70px rgba(19,58,88,.22);">
      <p style="font-size:13px;font-weight:800;color:#B0BDCA;text-transform:uppercase;letter-spacing:.06em;margin-bottom:14px;">Estratégia antes da ferramenta</p>
      <p style="font-size:24px;line-height:1.38;font-weight:800;color:#fff;margin-bottom:18px;">IA não começa escolhendo software. Começa decidindo qual problema merece ser resolvido.</p>
      <p style="font-size:15px;line-height:1.65;color:#B0BDCA;">Diagnóstico, priorização, implantação e treinamento para transformar inteligência artificial em processo de negócio.</p>
    </aside>
  </div>
</section>'''


def section_html(sec, idx):
    h2 = html.escape(sec.get("h2", ""))
    body = md_to_html(sec.get("conteudo_md", ""))
    if idx % 3 == 1:
        return f'''
<section style="background:#F6F8FA;padding:78px 24px;">
  <div style="max-width:920px;margin:0 auto;">
    <h2 style="font-size:32px;line-height:1.22;font-weight:800;color:#133A58;margin-bottom:22px;">{h2}</h2>
    {body}
  </div>
</section>'''
    if idx % 3 == 2:
        return f'''
<section style="background:#fff;padding:78px 24px;">
  <div style="max-width:980px;margin:0 auto;border-left:6px solid #B0BDCA;padding-left:28px;">
    <h2 style="font-size:31px;line-height:1.24;font-weight:800;color:#133A58;margin-bottom:22px;">{h2}</h2>
    {body}
  </div>
</section>'''
    return f'''
<section style="background:#133A58;padding:78px 24px;">
  <div style="max-width:980px;margin:0 auto;background:#fff;border:1px solid #B0BDCA;border-radius:18px;padding:34px;box-shadow:0 20px 60px rgba(19,58,88,.18);">
    <h2 style="font-size:31px;line-height:1.24;font-weight:800;color:#133A58;margin-bottom:22px;">{h2}</h2>
    {body}
  </div>
</section>'''


def links_section(links):
    labels = {
        "/mentoria-implantacao-ia/":"Mentoria de implantação de IA",
        "/agentes-de-ia/":"Agentes de IA",
        "/automacao-empresarial/":"Automação empresarial",
        "/automacao-atendimento-whatsapp/":"Automação de WhatsApp",
        "/consultoria-de-ia/":"Consultoria de IA",
    }
    if not links:
        return ""
    cards = "\n".join(f'''<a href="{html.escape(link)}" style="display:block;background:#fff;border:1px solid #B0BDCA;border-radius:12px;padding:18px 20px;color:#133A58;font-weight:800;">{html.escape(labels.get(link, link.strip('/').replace('-', ' ').title()))} →</a>''' for link in links)
    return f'''
<section style="background:#F6F8FA;padding:72px 24px;">
  <div style="max-width:920px;margin:0 auto;">
    <h2 style="font-size:28px;font-weight:800;color:#133A58;margin-bottom:24px;">Próximos passos relacionados</h2>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:14px;" class="g-3">{cards}</div>
  </div>
</section>'''


def build_page(item):
    slug = clean_slug(item["slug"])
    label = item["h1"].split(":")[0]
    BC = [("Início","/"),(label,None)]
    faqs = [(f["pergunta"], f["resposta"]) for f in item.get("faq", [])]
    sections = "\n".join(section_html(sec, idx+1) for idx, sec in enumerate(item.get("secoes", [])))
    main = f"""
{breadcrumb(BC)}
{hero(item)}
{sections}
{links_section(item.get('links_internos', []))}
{faq_html(faqs)}
{CTA_DIAG}
"""
    schemas = [service_schema(item), breadcrumb_schema(BC), faq_schema(faqs)]
    write(slug.strip("/") + "/index.html", page(item["meta_title"], item["meta_description"], slug, main, schemas=schemas))

for item in sorted(DATA["paginas"], key=lambda x: x.get("prioridade", 99)):
    build_page(item)
print("OK money pages")
