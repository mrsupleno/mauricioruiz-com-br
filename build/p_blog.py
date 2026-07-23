#!/usr/bin/env python3
"""Gera /blog/ provisório — página real para evitar fallback/404 e imagem quebrada."""
import sys, json
sys.path.insert(0, "/root/projects/mauricioruiz-com-br/build")
from base import page, breadcrumb, breadcrumb_schema, CTA_DIAG, write

BC = [("Início","/"),("Blog",None)]
MAIN = f"""
{breadcrumb(BC)}

<section style="background:#ffffff;padding:72px 24px 88px;">
  <div style="max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1.05fr 0.95fr;gap:56px;align-items:center;" class="g-hero">
    <div>
      <span style="display:inline-block;background:#F7F8FA;border:1px solid #E4E7EC;color:#12B76A;font-size:13px;font-weight:700;padding:6px 14px;border-radius:100px;margin-bottom:20px;">Conteúdos</span>
      <h1 style="font-size:44px;line-height:1.15;font-weight:800;color:#101828;margin-bottom:24px;">Inteligência Artificial sem teatro</h1>
      <p style="font-size:18px;line-height:1.7;color:#475467;margin-bottom:30px;max-width:640px;">Conteúdos sobre IA aplicada, automação, agentes inteligentes e processos empresariais — com foco em decisão, implantação e resultado.</p>
      <div style="display:flex;flex-wrap:wrap;gap:14px;">
        <a href="/diagnostico-de-ia/" style="background:#12B76A;color:#101828;font-weight:700;font-size:16px;padding:16px 26px;border-radius:8px;">Solicitar diagnóstico</a>
        <a href="/mentoria-implantacao-ia/" style="background:#fff;border:1px solid #D0D5DD;color:#101828;font-weight:600;font-size:16px;padding:16px 26px;border-radius:8px;">Ver mentoria</a>
      </div>
    </div>
    <div style="border-radius:18px;overflow:hidden;aspect-ratio:4/5;background:#E4E7EC;box-shadow:0 24px 70px rgba(16,24,40,.16);">
      <img src="/assets/mauricio-ruiz-hero.webp" srcset="/assets/mauricio-ruiz-hero.webp 800w, /assets/mauricio-ruiz-hero@2x.webp 889w" sizes="(max-width: 899px) 100vw, 42vw" alt="Mauricio Ruiz em ambiente empresarial, segurando tablet" width="889" height="1112" fetchpriority="high" style="width:100%;height:100%;object-fit:cover;display:block;">
    </div>
  </div>
</section>

<section style="background:#F7F8FA;padding:88px 24px;">
  <div style="max-width:1200px;margin:0 auto;">
    <h2 style="font-size:32px;font-weight:700;color:#101828;margin-bottom:16px;max-width:700px;">Por onde começar</h2>
    <p style="font-size:17px;line-height:1.7;color:#475467;max-width:660px;margin-bottom:40px;">Enquanto os artigos da Fase 2 são produzidos, estes são os conteúdos estruturais já publicados no site.</p>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:22px;" class="g-3">
      <a href="/mentoria-implantacao-ia/" style="display:block;background:#fff;border:1px solid #E4E7EC;border-radius:14px;padding:28px 24px;color:inherit;">
        <h3 style="font-size:19px;font-weight:700;color:#101828;margin-bottom:10px;">Mentoria de Implantação de IA</h3>
        <p style="font-size:14.5px;line-height:1.65;color:#667085;">Como sair da curiosidade e transformar IA em processo real dentro da empresa.</p>
      </a>
      <a href="/agentes-de-ia/" style="display:block;background:#fff;border:1px solid #E4E7EC;border-radius:14px;padding:28px 24px;color:inherit;">
        <h3 style="font-size:19px;font-weight:700;color:#101828;margin-bottom:10px;">Agentes de IA</h3>
        <p style="font-size:14.5px;line-height:1.65;color:#667085;">O que um agente faz além de responder mensagens — e quais limites precisam existir.</p>
      </a>
      <a href="/automacao-atendimento-whatsapp/" style="display:block;background:#fff;border:1px solid #E4E7EC;border-radius:14px;padding:28px 24px;color:inherit;">
        <h3 style="font-size:19px;font-weight:700;color:#101828;margin-bottom:10px;">Atendimento e WhatsApp</h3>
        <p style="font-size:14.5px;line-height:1.65;color:#667085;">Como automatizar o primeiro atendimento sem esconder a IA e sem prender o cliente.</p>
      </a>
    </div>
  </div>
</section>

<section style="background:#101828;padding:88px 24px;">
  <div style="max-width:840px;margin:0 auto;text-align:center;">
    <h2 style="font-size:30px;font-weight:700;color:#fff;margin-bottom:16px;">Artigos completos entram na próxima etapa</h2>
    <p style="font-size:16.5px;line-height:1.7;color:#98A2B3;">Melhor uma página honesta e funcional do que um blog fake cheio de placeholder. Os clusters de SEO da Fase 2 serão publicados aqui.</p>
  </div>
</section>

{CTA_DIAG}
"""
BLOG_SCHEMA = json.dumps({"@context":"https://schema.org","@type":"Blog",
    "name":"Blog Mauricio Ruiz | Mentor de Inteligência Artificial",
    "url":"https://mauricioruiz.com.br/blog/",
    "description":"Conteúdos sobre IA aplicada, automação, agentes inteligentes e processos empresariais."}, ensure_ascii=False, indent=1)
write("blog/index.html", page(
    "Blog | Mauricio Ruiz — IA, Automação e Agentes Inteligentes",
    "Conteúdos sobre Inteligência Artificial aplicada, automação empresarial, agentes de IA e implantação prática em empresas.",
    "/blog/", MAIN, schemas=[BLOG_SCHEMA, breadcrumb_schema(BC)]))
print("OK blog")
