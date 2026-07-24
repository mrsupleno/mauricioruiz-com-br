#!/usr/bin/env python3
"""Gera /sobre/, /diagnostico-de-ia/, /contato/"""
import sys, json
sys.path.insert(0, "/root/projects/mauricioruiz-com-br/build")
from base import page, breadcrumb, breadcrumb_schema, faq_html, faq_schema, CTA_DIAG, write

# ============================================================ SOBRE
BC = [("Início","/"),("Sobre",None)]
MAIN = f"""
{breadcrumb(BC)}

<section style="background:#ffffff;padding:72px 24px 88px;">
  <div style="max-width:1200px;margin:0 auto;display:grid;grid-template-columns:0.85fr 1.15fr;gap:56px;align-items:center;" class="g-sobre">
    <div style="border-radius:16px;overflow:hidden;aspect-ratio:4/5;">
      <img src="/assets/mauricio-ruiz-sobre.webp" srcset="/assets/mauricio-ruiz-sobre.webp 800w, /assets/mauricio-ruiz-sobre@2x.webp 1024w" sizes="(max-width: 899px) 100vw, 40vw" alt="Mauricio Ruiz sentado à mesa em escritório moderno, com laptop" width="1024" height="1280" fetchpriority="high" style="width:100%;height:100%;object-fit:cover;display:block;">
    </div>
    <div>
      <span style="display:inline-block;color:#3A606F;font-size:13px;font-weight:700;margin-bottom:16px;">Estratégia empresarial antes da ferramenta</span>
      <h1 style="font-size:40px;line-height:1.15;font-weight:800;color:#133A58;margin-bottom:24px;">Tecnologia muda processos. Pessoas determinam se a mudança funciona.</h1>
      <p style="font-size:17px;line-height:1.7;color:#475467;margin-bottom:14px;">Mauricio Ruiz atua há mais de 20 anos com desenvolvimento humano, treinamento, comportamento, estratégia, negócios e tomada de decisão.</p>
      <p style="font-size:17px;line-height:1.7;color:#475467;margin-bottom:14px;">Essa experiência é aplicada à implantação prática de Inteligência Artificial, automação e marketing. O trabalho considera três dimensões que não podem ser separadas: pessoas, processos e tecnologia.</p>
      <p style="font-size:17px;line-height:1.7;color:#475467;margin-bottom:28px;">Uma empresa não muda apenas quando instala uma ferramenta. Ela muda quando as pessoas sabem como utilizá-la, os processos estão claros e a tecnologia executa aquilo que foi corretamente definido.</p>
      <a href="/diagnostico-de-ia/" style="display:inline-block;background:#133A58;color:#fff;font-weight:700;font-size:16px;padding:16px 28px;border-radius:8px;">Falar sobre meu projeto</a>
    </div>
  </div>
</section>

<section style="background:#F6F8FA;padding:88px 24px;">
  <div style="max-width:1200px;margin:0 auto;">
    <h2 style="font-size:32px;font-weight:700;color:#133A58;margin-bottom:36px;max-width:680px;">O que essa experiência significa na prática</h2>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:20px;" class="g-4">
      <div style="background:#fff;border:1px solid #B0BDCA;border-radius:12px;padding:26px 22px;">
        <h3 style="font-size:17px;font-weight:700;color:#133A58;margin-bottom:10px;">Comportamento e decisão</h3>
        <p style="font-size:14.5px;line-height:1.6;color:#667085;">Mais de duas décadas modelando como pessoas decidem, aprendem e mudam. IA sem entender pessoas vira prateleira.</p>
      </div>
      <div style="background:#fff;border:1px solid #B0BDCA;border-radius:12px;padding:26px 22px;">
        <h3 style="font-size:17px;font-weight:700;color:#133A58;margin-bottom:10px;">Estratégia e negócios</h3>
        <p style="font-size:14.5px;line-height:1.6;color:#667085;">Projetos orientados a resultado empresarial — não a novidade tecnológica.</p>
      </div>
      <div style="background:#fff;border:1px solid #B0BDCA;border-radius:12px;padding:26px 22px;">
        <h3 style="font-size:17px;font-weight:700;color:#133A58;margin-bottom:10px;">Marketing e processos</h3>
        <p style="font-size:14.5px;line-height:1.6;color:#667085;">Experiência prática em marketing, automação e desenho de processos comerciais e operacionais.</p>
      </div>
      <div style="background:#fff;border:1px solid #B0BDCA;border-radius:12px;padding:26px 22px;">
        <h3 style="font-size:17px;font-weight:700;color:#133A58;margin-bottom:10px;">Treinamento e mentoria</h3>
        <p style="font-size:14.5px;line-height:1.6;color:#667085;">Formação de empresários e equipes — porque a implantação só funciona quando quem usa sabe usar.</p>
      </div>
    </div>
  </div>
</section>

<section style="background:#133A58;padding:88px 24px;">
  <div style="max-width:840px;margin:0 auto;text-align:center;">
    <p style="font-size:26px;line-height:1.4;font-weight:700;color:#fff;margin-bottom:20px;">"IA não é sobre instalar ferramentas. É sobre redesenhar a forma como a empresa trabalha."</p>
    <p style="color:#667085;font-size:15px;">Mauricio Ruiz</p>
  </div>
</section>

<section style="background:#ffffff;padding:88px 24px;">
  <div style="max-width:1200px;margin:0 auto;">
    <h2 style="font-size:32px;font-weight:700;color:#133A58;margin-bottom:28px;">Destaques profissionais</h2>
    <div style="display:flex;flex-wrap:wrap;gap:10px;margin-bottom:36px;">
      <span style="background:#F6F8FA;border:1px solid #B0BDCA;border-radius:100px;padding:8px 16px;font-size:13.5px;color:#344054;">Mais de 20 anos em desenvolvimento humano</span>
      <span style="background:#F6F8FA;border:1px solid #B0BDCA;border-radius:100px;padding:8px 16px;font-size:13.5px;color:#344054;">Treinamento e mentoria</span>
      <span style="background:#F6F8FA;border:1px solid #B0BDCA;border-radius:100px;padding:8px 16px;font-size:13.5px;color:#344054;">Modelagem de comportamento</span>
      <span style="background:#F6F8FA;border:1px solid #B0BDCA;border-radius:100px;padding:8px 16px;font-size:13.5px;color:#344054;">Estratégia empresarial</span>
      <span style="background:#F6F8FA;border:1px solid #B0BDCA;border-radius:100px;padding:8px 16px;font-size:13.5px;color:#344054;">Marketing</span>
      <span style="background:#F6F8FA;border:1px solid #B0BDCA;border-radius:100px;padding:8px 16px;font-size:13.5px;color:#344054;">Automação</span>
      <span style="background:#F6F8FA;border:1px solid #B0BDCA;border-radius:100px;padding:8px 16px;font-size:13.5px;color:#344054;">Inteligência Artificial aplicada</span>
      <span style="background:#F6F8FA;border:1px solid #B0BDCA;border-radius:100px;padding:8px 16px;font-size:13.5px;color:#344054;">Desenvolvimento de pessoas e equipes</span>
    </div>
    <p style="font-size:16.5px;line-height:1.7;color:#475467;max-width:680px;">Atendimento estratégico em Vila Velha, Vitória e Grande Vitória — e projetos para empresas de todo o Brasil por atendimento remoto.</p>
  </div>
</section>

{CTA_DIAG}
"""
PERSON = json.dumps({"@context":"https://schema.org","@type":"Person",
    "name":"Mauricio Ruiz","jobTitle":"Mentor de Inteligência Artificial",
    "url":"https://mauricioruiz.com.br/sobre/",
    "worksFor":{"@type":"ProfessionalService","name":"Mauricio Ruiz | Mentor de Inteligência Artificial"},
    "address":{"@type":"PostalAddress","addressLocality":"Vila Velha","addressRegion":"ES","addressCountry":"BR"}},
    ensure_ascii=False, indent=1)
write("sobre/index.html", page(
    "Sobre Mauricio Ruiz | Mentor de Inteligência Artificial",
    "Mais de 20 anos em desenvolvimento humano, estratégia e negócios aplicados à implantação prática de Inteligência Artificial, automação e marketing.",
    "/sobre/", MAIN, schemas=[PERSON, breadcrumb_schema(BC)]))
print("OK sobre")

# ============================================================ DIAGNÓSTICO (form enxuto)
DIAG_FAQS = [
    ("O diagnóstico de IA é uma consultoria completa?",
     "Não. O diagnóstico é a etapa inicial para entender processos, riscos e prioridades. A implantação vem depois, quando existe clareza sobre o que deve ser automatizado."),
    ("Preciso já saber qual ferramenta de IA usar?",
     "Não. Escolher ferramenta antes de entender o processo costuma gerar desperdício. A ferramenta entra depois da prioridade definida."),
    ("O atendimento pode ser presencial?",
     "Sim, especialmente para empresas de Vila Velha e Grande Vitória. Projetos nacionais também podem ser conduzidos por atendimento remoto."),
]
DIAG_SERVICE = json.dumps({"@context":"https://schema.org", "@graph":[
    {"@type":"ProfessionalService","@id":"https://mauricioruiz.com.br/#profissional",
     "name":"Mauricio Ruiz | Mentor de Inteligência Artificial",
     "url":"https://mauricioruiz.com.br/","telephone":"+55-27-92000-0167",
     "address":{"@type":"PostalAddress","streetAddress":"Rua Marajó, 77, Unidade 402",
                "addressLocality":"Vila Velha","addressRegion":"ES","postalCode":"29101-250","addressCountry":"BR"},
     "openingHours":"Mo-Fr 09:00-18:00",
     "areaServed":["Vila Velha","Vitória","Grande Vitória","Espírito Santo","Brasil"]},
    {"@type":"Service","@id":"https://mauricioruiz.com.br/diagnostico-de-ia/#servico",
     "name":"Diagnóstico de IA para Empresas",
     "description":"Diagnóstico para identificar processos, riscos, prioridades e oportunidades de implantação de Inteligência Artificial em empresas.",
     "provider":{"@id":"https://mauricioruiz.com.br/#profissional"},
     "areaServed":["Vila Velha","Vitória","Grande Vitória","Espírito Santo","Brasil"],
     "url":"https://mauricioruiz.com.br/diagnostico-de-ia/"}
]}, ensure_ascii=False, indent=1)
BC = [("Início","/"),("Diagnóstico de IA",None)]
MAIN = f"""
{breadcrumb(BC)}

<section style="background:#B0BDCA;padding:88px 24px;border-top:8px solid #2C4964;border-bottom:8px solid #2C4964;">
  <div style="max-width:900px;margin:0 auto;text-align:center;">
    <h1 style="font-size:40px;line-height:1.15;font-weight:800;color:#133A58;margin-bottom:20px;">Descubra onde a IA realmente pode gerar resultado na sua empresa</h1>
    <p style="font-size:17px;line-height:1.7;color:#383D44;max-width:640px;margin:0 auto 44px;">O diagnóstico identifica os processos mais promissores, os riscos, as prioridades e os primeiros projetos que podem ser implantados.</p>

    <div style="background:#fff;border:1px solid #B0BDCA;border-radius:18px;padding:36px;text-align:left;max-width:640px;margin:0 auto;box-shadow:0 24px 70px rgba(19,58,88,.22);">
      <form id="diagForm" style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">
        <input type="hidden" name="_subject" value="Diagnóstico de IA — mauricioruiz.com.br">
        <input type="hidden" name="_template" value="table">
        <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
        <label style="display:flex;flex-direction:column;gap:6px;font-size:13.5px;color:#133A58;font-weight:700;">Nome
          <input type="text" name="nome" required style="background:#F6F8FA;border:1px solid #B0BDCA;border-radius:8px;padding:12px 14px;color:#383D44;font-size:15px;font-family:'Inter',sans-serif;">
        </label>
        <label style="display:flex;flex-direction:column;gap:6px;font-size:13.5px;color:#133A58;font-weight:700;">Empresa
          <input type="text" name="empresa" required style="background:#F6F8FA;border:1px solid #B0BDCA;border-radius:8px;padding:12px 14px;color:#383D44;font-size:15px;font-family:'Inter',sans-serif;">
        </label>
        <label style="display:flex;flex-direction:column;gap:6px;font-size:13.5px;color:#133A58;font-weight:700;">Telefone / WhatsApp
          <input type="tel" name="telefone" required style="background:#F6F8FA;border:1px solid #B0BDCA;border-radius:8px;padding:12px 14px;color:#383D44;font-size:15px;font-family:'Inter',sans-serif;">
        </label>
        <label style="display:flex;flex-direction:column;gap:6px;font-size:13.5px;color:#133A58;font-weight:700;">E-mail
          <input type="email" name="email" required style="background:#F6F8FA;border:1px solid #B0BDCA;border-radius:8px;padding:12px 14px;color:#383D44;font-size:15px;font-family:'Inter',sans-serif;">
        </label>
        <label style="display:flex;flex-direction:column;gap:6px;font-size:13.5px;color:#133A58;font-weight:700;grid-column:1 / -1;">Segmento da empresa
          <input type="text" name="segmento" required style="background:#F6F8FA;border:1px solid #B0BDCA;border-radius:8px;padding:12px 14px;color:#383D44;font-size:15px;font-family:'Inter',sans-serif;">
        </label>
        <label style="display:flex;flex-direction:column;gap:6px;font-size:13.5px;color:#133A58;font-weight:700;grid-column:1 / -1;">Qual tarefa sua empresa ainda faz manualmente apenas porque ninguém parou para redesenhar o processo?
          <textarea name="tarefa" rows="3" style="background:#F6F8FA;border:1px solid #B0BDCA;border-radius:8px;padding:12px 14px;color:#383D44;font-size:15px;font-family:'Inter',sans-serif;resize:vertical;"></textarea>
        </label>
        <button type="submit" data-label="Solicitar diagnóstico de IA" style="grid-column:1 / -1;background:#3A606F;color:#fff;font-weight:800;font-size:16px;padding:16px;border-radius:8px;border:none;cursor:pointer;font-family:'Inter',sans-serif;box-shadow:0 10px 24px rgba(58,96,111,.28);">Solicitar diagnóstico de IA</button>
        <p style="grid-column:1 / -1;color:#383D44;font-size:12.5px;text-align:center;">Seus dados são usados apenas para retorno deste contato. <a href="/politica-de-privacidade/" style="color:#2C4964;text-decoration:underline;font-weight:700;">Política de Privacidade</a></p>
      </form>
    </div>

    <div style="margin-top:28px;">
      <a href="https://wa.me/5527920000167" target="_blank" rel="noopener" style="color:#133A58;font-weight:800;font-size:15px;">Prefere falar direto? Falar pelo WhatsApp →</a>
    </div>
  </div>
</section>

<section style="background:#ffffff;padding:88px 24px;">
  <div style="max-width:1200px;margin:0 auto;">
    <h2 style="font-size:32px;font-weight:700;color:#133A58;margin-bottom:36px;max-width:680px;">O que acontece depois do envio</h2>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:22px;" class="g-3">
      <div style="border-top:3px solid #3A606F;padding-top:16px;">
        <span style="font-size:13px;font-weight:700;color:#3A606F;">01</span>
        <h3 style="font-size:17px;font-weight:700;color:#133A58;margin:6px 0 8px;">Análise inicial</h3>
        <p style="font-size:14.5px;line-height:1.6;color:#667085;">Suas respostas são analisadas no contexto do seu segmento e da sua operação.</p>
      </div>
      <div style="border-top:3px solid #3A606F;padding-top:16px;">
        <span style="font-size:13px;font-weight:700;color:#3A606F;">02</span>
        <h3 style="font-size:17px;font-weight:700;color:#133A58;margin:6px 0 8px;">Conversa estratégica</h3>
        <p style="font-size:14.5px;line-height:1.6;color:#667085;">Contato dentro do horário comercial para entender o cenário e as prioridades.</p>
      </div>
      <div style="border-top:3px solid #3A606F;padding-top:16px;">
        <span style="font-size:13px;font-weight:700;color:#3A606F;">03</span>
        <h3 style="font-size:17px;font-weight:700;color:#133A58;margin:6px 0 8px;">Direção clara</h3>
        <p style="font-size:14.5px;line-height:1.6;color:#667085;">Você sai sabendo o que automatizar, o que reorganizar antes e o que deixar humano.</p>
      </div>
    </div>
  </div>
</section>

{faq_html(DIAG_FAQS)}
"""
write("diagnostico-de-ia/index.html", page(
    "Diagnóstico de IA para Empresas | Mauricio Ruiz",
    "Identifique onde a Inteligência Artificial pode gerar resultado na sua empresa: processos promissores, riscos, prioridades e primeiros projetos.",
    "/diagnostico-de-ia/", MAIN, schemas=[DIAG_SERVICE, breadcrumb_schema(BC), faq_schema(DIAG_FAQS)]))
print("OK diagnostico")

# ============================================================ CONTATO
BC = [("Início","/"),("Contato",None)]
MAIN = f"""
{breadcrumb(BC)}

<section style="background:#ffffff;padding:72px 24px 88px;">
  <div style="max-width:1200px;margin:0 auto;">
    <h1 style="font-size:40px;line-height:1.15;font-weight:800;color:#133A58;margin-bottom:20px;max-width:720px;">Contato</h1>
    <p style="font-size:17px;line-height:1.7;color:#475467;max-width:640px;margin-bottom:44px;">Atendimento humano de segunda a sexta-feira, das 9h às 18h. Fora desse horário, o assistente de IA pode registrar sua necessidade e deixar o atendimento preparado.</p>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:22px;" class="g-3">
      <div style="background:#F6F8FA;border:1px solid #B0BDCA;border-radius:14px;padding:30px 26px;">
        <h2 style="font-size:17px;font-weight:700;color:#133A58;margin-bottom:14px;">WhatsApp e telefone</h2>
        <p style="font-size:15px;color:#475467;margin-bottom:10px;">(27) 92000-0167</p>
        <a href="https://wa.me/5527920000167" target="_blank" rel="noopener" style="color:#3A606F;font-weight:600;font-size:14.5px;">Iniciar conversa →</a>
      </div>
      <div style="background:#F6F8FA;border:1px solid #B0BDCA;border-radius:14px;padding:30px 26px;">
        <h2 style="font-size:17px;font-weight:700;color:#133A58;margin-bottom:14px;">Diagnóstico de IA</h2>
        <p style="font-size:15px;color:#475467;margin-bottom:10px;">Conte onde sua empresa perde tempo e receba uma direção.</p>
        <a href="/diagnostico-de-ia/" style="color:#3A606F;font-weight:600;font-size:14.5px;">Solicitar diagnóstico →</a>
      </div>
      <div style="background:#F6F8FA;border:1px solid #B0BDCA;border-radius:14px;padding:30px 26px;">
        <h2 style="font-size:17px;font-weight:700;color:#133A58;margin-bottom:14px;">Endereço</h2>
        <p style="font-size:15px;color:#475467;line-height:1.6;">Rua Marajó, 77, Unidade 402<br>Praia da Costa, Vila Velha – ES<br>CEP 29101-250</p>
      </div>
    </div>
  </div>
</section>

<section style="background:#F6F8FA;padding:88px 24px;">
  <div style="max-width:840px;margin:0 auto;text-align:center;">
    <h2 style="font-size:28px;font-weight:700;color:#133A58;margin-bottom:16px;">Área de atendimento</h2>
    <p style="font-size:16.5px;line-height:1.7;color:#475467;">Vila Velha, Vitória e Grande Vitória — Espírito Santo.<br>Empresas de todo o Brasil por atendimento remoto.</p>
  </div>
</section>
"""
LOCAL = json.dumps({"@context":"https://schema.org","@type":"ProfessionalService",
    "name":"Mauricio Ruiz | Mentor de Inteligência Artificial",
    "url":"https://mauricioruiz.com.br/","telephone":"+55-27-92000-0167",
    "address":{"@type":"PostalAddress","streetAddress":"Rua Marajó, 77, Unidade 402",
               "addressLocality":"Vila Velha","addressRegion":"ES","postalCode":"29101-250","addressCountry":"BR"},
    "openingHours":"Mo-Fr 09:00-18:00",
    "areaServed":["Vila Velha","Vitória","Grande Vitória","Espírito Santo","Brasil"]},
    ensure_ascii=False, indent=1)
write("contato/index.html", page(
    "Contato | Mauricio Ruiz — Mentor de Inteligência Artificial",
    "Fale com Mauricio Ruiz: WhatsApp (27) 92000-0167, diagnóstico de IA e atendimento em Vila Velha, Grande Vitória e todo o Brasil.",
    "/contato/", MAIN, schemas=[LOCAL, breadcrumb_schema(BC)]))
print("OK contato")
