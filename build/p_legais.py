#!/usr/bin/env python3
"""Gera páginas legais, robots.txt, sitemap.xml, 404.html"""
import sys, pathlib
sys.path.insert(0, "/root/projects/mauricioruiz-com-br/build")
from base import page, breadcrumb, write

ROOT = pathlib.Path("/root/projects/mauricioruiz-com-br")

def legal_page(title, h1, sections, canonical):
    BC = [("Início","/"),(h1,None)]
    body = "\n".join(f"""
    <h2 style="font-size:22px;font-weight:700;color:#101828;margin:36px 0 12px;">{t}</h2>
    <p style="font-size:15.5px;line-height:1.7;color:#475467;">{p}</p>""" for t, p in sections)
    MAIN = f"""
{breadcrumb(BC)}
<section style="background:#ffffff;padding:72px 24px 88px;">
  <div style="max-width:840px;margin:0 auto;">
    <h1 style="font-size:36px;font-weight:800;color:#101828;margin-bottom:8px;">{h1}</h1>
    <p style="font-size:14px;color:#667085;margin-bottom:20px;">Última atualização: julho de 2026</p>
    {body}
    <h2 style="font-size:22px;font-weight:700;color:#101828;margin:36px 0 12px;">Contato</h2>
    <p style="font-size:15.5px;line-height:1.7;color:#475467;">Mauricio Ruiz | Mentor de Inteligência Artificial — Rua Marajó, 77, Unidade 402, Praia da Costa, Vila Velha – ES, CEP 29101-250. WhatsApp: (27) 92000-0167.</p>
  </div>
</section>"""
    write(canonical.strip("/") + "/index.html", page(title, f"{h1} do site mauricioruiz.com.br.", canonical, MAIN))

# ---------- PRIVACIDADE
legal_page(
    "Política de Privacidade | Mauricio Ruiz",
    "Política de Privacidade",
    [
        ("Dados coletados","Este site coleta apenas os dados que você fornece voluntariamente pelo formulário de diagnóstico (nome, empresa, telefone, e-mail, segmento e descrição da necessidade) ou em conversas pelo WhatsApp."),
        ("Uso dos dados","Os dados são utilizados exclusivamente para retorno do contato solicitado, elaboração de propostas e continuidade do atendimento. Não são vendidos, alugados ou compartilhados com terceiros para fins de marketing."),
        ("Base legal","O tratamento segue a Lei Geral de Proteção de Dados (Lei nº 13.709/2018), com base no legítimo interesse e no consentimento fornecido no momento do envio."),
        ("Armazenamento e segurança","As informações são armazenadas em canais controlados pelo responsável pelo site, com acesso restrito. Medidas razoáveis de segurança são adotadas para evitar acesso não autorizado."),
        ("Seus direitos","Você pode solicitar a confirmação, o acesso, a correção ou a exclusão dos seus dados a qualquer momento pelo WhatsApp (27) 92000-0167."),
        ("Retenção","Os dados são mantidos apenas pelo tempo necessário para o atendimento e obrigações legais. Após esse período, são eliminados."),
    ],
    "/politica-de-privacidade/")
print("OK privacidade")

# ---------- COOKIES
legal_page(
    "Política de Cookies | Mauricio Ruiz",
    "Política de Cookies",
    [
        ("O que são cookies","Cookies são pequenos arquivos armazenados no seu navegador para lembrar preferências e entender como o site é utilizado."),
        ("Cookies utilizados neste site","Este site utiliza apenas cookies estritamente necessários ao funcionamento técnico das páginas. Não utilizamos cookies de publicidade nem rastreamento de terceiros para remarketing."),
        ("Ferramentas de medição","Caso ferramentas de análise de audiência sejam ativadas no futuro, você será informado e poderá gerenciar seu consentimento."),
        ("Como gerenciar","Você pode bloquear ou excluir cookies nas configurações do seu navegador. A navegação no site continuará funcional."),
    ],
    "/politica-de-cookies/")
print("OK cookies")

# ---------- TERMOS
legal_page(
    "Termos de Uso | Mauricio Ruiz",
    "Termos de Uso",
    [
        ("Objeto","Estes termos regulam o uso do site mauricioruiz.com.br, de propriedade de Mauricio Ruiz | Mentor de Inteligência Artificial."),
        ("Conteúdo informativo","Os conteúdos deste site têm caráter informativo e educativo. Não constituem proposta comercial vinculante, promessa de resultado nem diagnóstico técnico definitivo."),
        ("Propriedade intelectual","Textos, marca, layout e materiais deste site são protegidos. A reprodução sem autorização prévia é proibida."),
        ("Responsabilidades","Decisões empresariais tomadas com base em conteúdos do site são de responsabilidade do visitante. Projetos de implantação são regidos por proposta e contrato específicos."),
        ("Links externos","Este site pode conter links para serviços de terceiros (como WhatsApp). Não nos responsabilizamos pelas políticas desses serviços."),
        ("Alterações","Estes termos podem ser atualizados a qualquer momento. A versão vigente é sempre a publicada nesta página."),
    ],
    "/termos-de-uso/")
print("OK termos")

# ---------- robots.txt
(ROOT/"robots.txt").write_text("""User-agent: *
Allow: /

Sitemap: https://mauricioruiz.com.br/sitemap.xml
""", encoding="utf-8")
print("OK robots.txt")

# ---------- sitemap.xml
urls = [
    ("/", "1.0", "weekly"),
    ("/mentoria-implantacao-ia/", "0.9", "monthly"),
    ("/agentes-de-ia/", "0.9", "monthly"),
    ("/automacao-empresarial/", "0.9", "monthly"),
    ("/automacao-atendimento-whatsapp/", "0.9", "monthly"),
    ("/sobre/", "0.7", "monthly"),
    ("/diagnostico-de-ia/", "0.9", "monthly"),
    ("/contato/", "0.6", "yearly"),
    ("/politica-de-privacidade/", "0.2", "yearly"),
    ("/politica-de-cookies/", "0.2", "yearly"),
    ("/termos-de-uso/", "0.2", "yearly"),
]
items = "\n".join(f"""  <url>
    <loc>https://mauricioruiz.com.br{u}</loc>
    <lastmod>2026-07-23</lastmod>
    <changefreq>{c}</changefreq>
    <priority>{p}</priority>
  </url>""" for u, p, c in urls)
(ROOT/"sitemap.xml").write_text(f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{items}
</urlset>
""", encoding="utf-8")
print("OK sitemap.xml")

# ---------- 404.html
MAIN_404 = """
<section style="background:#ffffff;padding:120px 24px;text-align:center;">
  <div style="max-width:640px;margin:0 auto;">
    <p style="font-size:64px;font-weight:800;color:#12B76A;margin-bottom:12px;">404</p>
    <h1 style="font-size:32px;font-weight:700;color:#101828;margin-bottom:16px;">Esta página não existe</h1>
    <p style="font-size:16.5px;color:#475467;margin-bottom:32px;">O endereço pode ter mudado ou foi digitado incorretamente.</p>
    <a href="/" style="display:inline-block;background:#12B76A;color:#101828;font-weight:700;font-size:16px;padding:16px 28px;border-radius:8px;">Voltar para o início</a>
  </div>
</section>"""
(ROOT/"404.html").write_text(page(
    "Página não encontrada | Mauricio Ruiz",
    "A página solicitada não foi encontrada.",
    "/404.html", MAIN_404), encoding="utf-8")
print("OK 404.html")
