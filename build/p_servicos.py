#!/usr/bin/env python3
"""Gera /agentes-de-ia/, /automacao-empresarial/, /automacao-atendimento-whatsapp/"""
import sys, json
sys.path.insert(0, "/root/projects/mauricioruiz-com-br/build")
from base import page, breadcrumb, breadcrumb_schema, faq_html, faq_schema, CTA_DIAG, write

def service_schema(name, desc):
    return json.dumps({"@context":"https://schema.org","@type":"Service","name":name,
        "provider":{"@type":"ProfessionalService","name":"Mauricio Ruiz | Mentor de Inteligência Artificial","url":"https://mauricioruiz.com.br/"},
        "areaServed":["Vila Velha","Vitória","Grande Vitória","Espírito Santo","Brasil"],
        "description":desc}, ensure_ascii=False, indent=1)

def hero(selobg, selo, h1, sub, cta_label, cta_href="/diagnostico-de-ia/"):
    return f"""
<section style="background:#ffffff;padding:72px 24px 80px;">
  <div style="max-width:1200px;margin:0 auto;">
    <span style="display:inline-block;background:#F6F8FA;border:1px solid #B0BDCA;color:{selobg};font-size:13px;font-weight:700;padding:6px 14px;border-radius:100px;margin-bottom:20px;">{selo}</span>
    <h1 style="font-size:44px;line-height:1.15;font-weight:800;color:#133A58;margin-bottom:24px;max-width:820px;">{h1}</h1>
    <p style="font-size:19px;line-height:1.6;color:#475467;max-width:680px;margin-bottom:32px;">{sub}</p>
    <div style="display:flex;flex-wrap:wrap;gap:14px;">
      <a href="{cta_href}" style="background:#3A606F;color:#133A58;font-weight:700;font-size:16px;padding:16px 26px;border-radius:8px;">{cta_label}</a>
      <a href="https://wa.me/5527920000167" target="_blank" rel="noopener" style="background:#fff;border:1px solid #B0BDCA;color:#133A58;font-weight:600;font-size:16px;padding:16px 26px;border-radius:8px;">Falar pelo WhatsApp</a>
    </div>
  </div>
</section>"""

def cards_grid(items, bg="#F6F8FA", cols="g-3", repeat="repeat(3,1fr)"):
    cards = "\n".join(f'''      <div style="background:#fff;border:1px solid #B0BDCA;border-radius:14px;padding:30px 26px;">
        <h3 style="font-size:19px;font-weight:700;color:#133A58;margin-bottom:12px;">{t}</h3>
        <p style="font-size:14.5px;line-height:1.65;color:#667085;">{d}</p>
      </div>''' for t, d in items)
    return f'''<div style="display:grid;grid-template-columns:{repeat};gap:22px;" class="{cols}">
{cards}
    </div>'''

# ============================================================ AGENTES DE IA
BC = [("Início","/"),("Agentes de IA",None)]
FAQS = [
    ("Qual a diferença entre chatbot e agente de IA?",
     "Um chatbot tradicional responde com base em caminhos predefinidos. Um agente de IA interpreta solicitações, consulta informações, segue regras, executa tarefas dentro de limites definidos, atualiza sistemas e encaminha situações para pessoas."),
    ("Um agente de IA substitui funcionários?",
     "O objetivo inicial não é substituir pessoas. Na maioria dos casos, o agente reduz tarefas repetitivas, organiza informações e aumenta a capacidade da equipe. A redistribuição de funções depende de cada operação."),
    ("O agente pode acessar informações da empresa?",
     "Pode, desde que exista autorização, estrutura técnica adequada e regras claras. O agente consulta apenas as informações necessárias para sua função. Dados confidenciais exigem controle, critérios de segurança e definição de responsabilidades."),
    ("Quando o agente encaminha para uma pessoa?",
     "Sempre que a situação exigir análise, negociação ou decisão humana. O limite é definido no desenho do processo — o agente não deve prender o cliente em respostas inúteis."),
]
MAIN = f"""
{breadcrumb(BC)}
{hero("#3A606F","Agentes de Inteligência Artificial","Um agente de IA não é apenas um chatbot","Desenvolvimento e implantação de agentes para atendimento, vendas, suporte e processos internos — com regras, limites e integração aos seus sistemas.","Quero avaliar um agente de IA")}

<section style="background:#F6F8FA;padding:88px 24px;">
  <div style="max-width:1200px;margin:0 auto;">
    <h2 style="font-size:34px;font-weight:700;color:#133A58;margin-bottom:16px;max-width:700px;">O que um agente pode fazer</h2>
    <p style="font-size:17px;line-height:1.7;color:#475467;max-width:640px;margin-bottom:44px;">Dentro de limites definidos no desenho do processo, um agente executa o trabalho repetitivo e organiza o que precisa de decisão humana.</p>
    {cards_grid([
        ("Atendimento","Recebe contatos, responde perguntas frequentes, faz triagem e encaminha exceções para pessoas."),
        ("Vendas","Qualifica leads, coleta informações, agenda conversas e mantém o acompanhamento em dia."),
        ("Suporte","Consulta a base de conhecimento, orienta o cliente e registra o histórico completo."),
        ("Processos internos","Organiza solicitações, consulta documentos, atualiza sistemas e apoia a equipe no dia a dia."),
        ("Agendamento","Marca horários, confirma presença e remarca quando necessário, sem vai-e-volta de mensagens."),
        ("Acompanhamento","Faz follow-up de contatos e oportunidades que hoje dependem da memória de alguém."),
    ])}
  </div>
</section>

<section style="background:#133A58;padding:88px 24px;">
  <div style="max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:start;" class="g-2">
    <div>
      <h2 style="font-size:32px;font-weight:700;color:#fff;margin-bottom:20px;">Como um agente responde</h2>
      <p style="font-size:16.5px;line-height:1.7;color:#98A2B3;margin-bottom:14px;">Cada etapa é definida no desenho do processo. Nada fica por conta do improviso.</p>
      <div style="background:#383D44;border-radius:12px;padding:24px;margin-top:24px;">
        <p style="font-size:18px;font-weight:700;color:#fff;line-height:1.4;">Seu funcionário precisa responder à mesma pergunta cinquenta vezes por semana?</p>
        <p style="font-size:18px;font-weight:700;color:#3A606F;line-height:1.4;margin-top:6px;">Talvez o problema não seja falta de equipe.</p>
      </div>
    </div>
    <div style="background:#383D44;border-radius:16px;padding:32px;">
      <div style="display:flex;flex-direction:column;gap:0;">
        <div style="display:flex;gap:16px;align-items:flex-start;"><div style="display:flex;flex-direction:column;align-items:center;"><div style="width:28px;height:28px;border-radius:50%;background:#3A606F;color:#133A58;font-weight:700;font-size:13px;display:flex;align-items:center;justify-content:center;flex-shrink:0;">1</div><div style="width:2px;flex:1;background:#344054;min-height:24px;"></div></div><p style="color:#B0BDCA;font-size:15px;padding-bottom:24px;">Cliente envia mensagem</p></div>
        <div style="display:flex;gap:16px;align-items:flex-start;"><div style="display:flex;flex-direction:column;align-items:center;"><div style="width:28px;height:28px;border-radius:50%;background:#3A606F;color:#133A58;font-weight:700;font-size:13px;display:flex;align-items:center;justify-content:center;flex-shrink:0;">2</div><div style="width:2px;flex:1;background:#344054;min-height:24px;"></div></div><p style="color:#B0BDCA;font-size:15px;padding-bottom:24px;">Agente interpreta a solicitação</p></div>
        <div style="display:flex;gap:16px;align-items:flex-start;"><div style="display:flex;flex-direction:column;align-items:center;"><div style="width:28px;height:28px;border-radius:50%;background:#3A606F;color:#133A58;font-weight:700;font-size:13px;display:flex;align-items:center;justify-content:center;flex-shrink:0;">3</div><div style="width:2px;flex:1;background:#344054;min-height:24px;"></div></div><p style="color:#B0BDCA;font-size:15px;padding-bottom:24px;">Consulta os dados necessários</p></div>
        <div style="display:flex;gap:16px;align-items:flex-start;"><div style="display:flex;flex-direction:column;align-items:center;"><div style="width:28px;height:28px;border-radius:50%;background:#3A606F;color:#133A58;font-weight:700;font-size:13px;display:flex;align-items:center;justify-content:center;flex-shrink:0;">4</div><div style="width:2px;flex:1;background:#344054;min-height:24px;"></div></div><p style="color:#B0BDCA;font-size:15px;padding-bottom:24px;">Responde e registra</p></div>
        <div style="display:flex;gap:16px;align-items:flex-start;"><div style="display:flex;flex-direction:column;align-items:center;"><div style="width:28px;height:28px;border-radius:50%;background:#3A606F;color:#133A58;font-weight:700;font-size:13px;display:flex;align-items:center;justify-content:center;flex-shrink:0;">5</div></div><p style="color:#B0BDCA;font-size:15px;">Encaminha para uma pessoa quando necessário</p></div>
      </div>
    </div>
  </div>
</section>

<section style="background:#ffffff;padding:88px 24px;">
  <div style="max-width:1200px;margin:0 auto;">
    <h2 style="font-size:32px;font-weight:700;color:#133A58;margin-bottom:28px;max-width:680px;">Regras antes da tecnologia</h2>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;max-width:900px;" class="g-pqi">
      <div style="display:flex;gap:10px;align-items:flex-start;font-size:15px;color:#344054;line-height:1.5;"><span style="color:#3A606F;flex-shrink:0;">✓</span>O agente informa que é um atendimento automatizado</div>
      <div style="display:flex;gap:10px;align-items:flex-start;font-size:15px;color:#344054;line-height:1.5;"><span style="color:#3A606F;flex-shrink:0;">✓</span>Acessa apenas as informações necessárias para sua função</div>
      <div style="display:flex;gap:10px;align-items:flex-start;font-size:15px;color:#344054;line-height:1.5;"><span style="color:#3A606F;flex-shrink:0;">✓</span>Não promete prazo nem preço sem escopo definido</div>
      <div style="display:flex;gap:10px;align-items:flex-start;font-size:15px;color:#344054;line-height:1.5;"><span style="color:#3A606F;flex-shrink:0;">✓</span>Encaminha para pessoas quando a situação exige</div>
      <div style="display:flex;gap:10px;align-items:flex-start;font-size:15px;color:#344054;line-height:1.5;"><span style="color:#3A606F;flex-shrink:0;">✓</span>Registra o contexto para continuidade humana</div>
      <div style="display:flex;gap:10px;align-items:flex-start;font-size:15px;color:#344054;line-height:1.5;"><span style="color:#3A606F;flex-shrink:0;">✓</span>Opera 24 horas; o atendimento humano segue o horário comercial</div>
    </div>
  </div>
</section>

{faq_html(FAQS)}
{CTA_DIAG}
"""
write("agentes-de-ia/index.html", page(
    "Agentes de IA para Atendimento e Vendas | Mauricio Ruiz",
    "Desenvolvimento e implantação de agentes de Inteligência Artificial para atendimento, vendas, suporte e processos internos.",
    "/agentes-de-ia/", MAIN,
    schemas=[service_schema("Desenvolvimento de Agentes de Inteligência Artificial","Agentes de IA para atendimento, vendas, suporte, consulta de informações e processos internos."), breadcrumb_schema(BC), faq_schema(FAQS)]))
print("OK agentes")

# ============================================================ AUTOMAÇÃO EMPRESARIAL
BC = [("Início","/"),("Automação Empresarial",None)]
FAQS = [
    ("Por onde começar uma automação?",
     "Identificando onde a empresa perde mais tempo: tarefas repetidas, respostas atrasadas, informações copiadas entre sistemas, oportunidades sem acompanhamento. O diagnóstico separa o que deve ser automatizado, o que precisa ser reorganizado antes e o que deve permanecer humano."),
    ("Preciso trocar os sistemas que já uso?",
     "Nem sempre. Em muitos projetos a automação é integrada às ferramentas existentes. A viabilidade depende dos sistemas, das permissões e das integrações disponíveis."),
    ("O que não deve ser automatizado?",
     "Processos mal definidos, decisões que exigem julgamento, situações de exceção e relacionamentos que dependem de pessoas. Automatizar um processo ruim só faz o erro acontecer mais rápido."),
    ("Como o resultado é medido?",
     "Com indicadores definidos antes da implantação: tempo gasto em tarefas repetitivas, erros operacionais, tempo de resposta, capacidade da equipe. Sem situação inicial registrada, não existe comparação confiável."),
]
MAIN = f"""
{breadcrumb(BC)}
{hero("#3A606F","Automação de processos","Automação empresarial com Inteligência Artificial","Redução de tarefas repetitivas, organização das informações e aumento da capacidade da equipe — começando pelo processo, não pela ferramenta.","Identificar oportunidades")}

<section style="background:#F6F8FA;padding:88px 24px;">
  <div style="max-width:1200px;margin:0 auto;">
    <h2 style="font-size:34px;font-weight:700;color:#133A58;margin-bottom:16px;max-width:700px;">Onde a automação gera resultado</h2>
    <p style="font-size:17px;line-height:1.7;color:#475467;max-width:640px;margin-bottom:44px;">A tecnologia entra onde existe um problema claro, uma regra definida e um resultado que pode ser acompanhado.</p>
    {cards_grid([
        ("Cadastros e formulários","Dados entram uma vez e chegam onde precisam estar — sem digitação repetida."),
        ("Propostas e documentos","Montagem, envio e acompanhamento de propostas comerciais sem montar cada arquivo do zero."),
        ("Relatórios","Consolidação automática de informações que hoje consomem horas de planilha."),
        ("Comunicação interna","Distribuição de informações para as pessoas certas, no momento certo, com registro."),
        ("Cobranças e lembretes","Acompanhamento sistemático que não depende de alguém lembrar."),
        ("Atualização de sistemas","Sincronização entre CRM, ERP, planilhas e bancos de dados, sem retrabalho."),
    ])}
  </div>
</section>

<section style="background:#0B3B2E;padding:88px 24px;">
  <div style="max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:24px;" class="g-2">
    <div style="background:#101B3D;border:1px solid #1E4636;border-radius:14px;padding:26px;">
      <h3 style="color:#F97066;font-size:15px;font-weight:700;margin-bottom:16px;">Sem processo</h3>
      <p style="color:#D2D9DE;font-size:14.5px;padding:8px 0;border-bottom:1px solid #1E4636;">Informação espalhada em planilhas e mensagens</p>
      <p style="color:#D2D9DE;font-size:14.5px;padding:8px 0;border-bottom:1px solid #1E4636;">Tarefas copiadas entre sistemas</p>
      <p style="color:#D2D9DE;font-size:14.5px;padding:8px 0;border-bottom:1px solid #1E4636;">Acompanhamento dependente de memória</p>
      <p style="color:#D2D9DE;font-size:14.5px;padding:8px 0;">Operação travada em poucas pessoas</p>
    </div>
    <div style="background:#101B3D;border:1px solid #3A606F;border-radius:14px;padding:26px;">
      <h3 style="color:#3A606F;font-size:15px;font-weight:700;margin-bottom:16px;">Com automação bem implantada</h3>
      <p style="color:#B0BDCA;font-size:14.5px;padding:8px 0;border-bottom:1px solid #1E4636;">Informação centralizada e consultável</p>
      <p style="color:#B0BDCA;font-size:14.5px;padding:8px 0;border-bottom:1px solid #1E4636;">Dados fluindo entre sistemas</p>
      <p style="color:#B0BDCA;font-size:14.5px;padding:8px 0;border-bottom:1px solid #1E4636;">Acompanhamento sistemático e registrado</p>
      <p style="color:#B0BDCA;font-size:14.5px;padding:8px 0;">Processo funcionando independente de quem está presente</p>
    </div>
  </div>
</section>

<section style="background:#ffffff;padding:88px 24px;">
  <div style="max-width:1200px;margin:0 auto;text-align:center;">
    <h2 style="font-size:32px;font-weight:700;color:#133A58;margin-bottom:16px;max-width:720px;margin-left:auto;margin-right:auto;">A ferramenta executa. O processo define se ela vai ajudar.</h2>
    <p style="font-size:17px;color:#475467;max-width:640px;margin:0 auto 36px;">Por isso a automação começa com mapeamento e priorização — não com instalação.</p>
    <a href="/mentoria-implantacao-ia/" style="color:#2C4964;font-weight:600;font-size:15px;">Ver como funciona a mentoria de implantação →</a>
  </div>
</section>

{faq_html(FAQS)}
{CTA_DIAG}
"""
write("automacao-empresarial/index.html", page(
    "Automação Empresarial com Inteligência Artificial | Mauricio Ruiz",
    "Automação de processos empresariais para reduzir tarefas repetitivas, organizar informações e aumentar a capacidade da equipe.",
    "/automacao-empresarial/", MAIN,
    schemas=[service_schema("Automação de Processos Empresariais com IA","Automação de tarefas, cadastros, propostas, relatórios, acompanhamentos e comunicação."), breadcrumb_schema(BC), faq_schema(FAQS)]))
print("OK automacao")

# ============================================================ WHATSAPP
BC = [("Início","/"),("Automação de Atendimento e WhatsApp",None)]
FAQS = [
    ("É possível automatizar o atendimento pelo WhatsApp?",
     "Sim. O agente recebe contatos, identifica a necessidade, responde perguntas frequentes, coleta informações, qualifica oportunidades, faz triagens, agenda horários e encaminha o atendimento para a pessoa responsável. A automação não deve esconder que existe uma IA no atendimento — nem impedir o acesso a uma pessoa quando a situação exigir."),
    ("O atendimento funciona 24 horas?",
     "Os agentes podem receber e organizar contatos 24 horas por dia. O atendimento humano ocorre de segunda a sexta, das 9h às 18h. Fora desse horário, o agente responde dúvidas iniciais e deixa o atendimento preparado para continuidade humana."),
    ("O cliente percebe que está falando com uma IA?",
     "Sim — e deve perceber. O agente se apresenta como atendimento automatizado. Esconder a IA destrói a confiança; ser transparente organiza a expectativa e melhora a experiência."),
    ("Integra com o CRM que já uso?",
     "Em muitos casos, sim. A viabilidade depende de o sistema oferecer integração por API, conectores ou automações. Quando não há integração direta, avaliamos alternativas sem criar estrutura frágil."),
]
MAIN = f"""
{breadcrumb(BC)}
{hero("#3A606F","Atendimento e WhatsApp","Seu primeiro atendimento pode acontecer em segundos","Agentes de IA para receber contatos, responder dúvidas, qualificar oportunidades e organizar o atendimento pelo WhatsApp — 24 horas por dia.","Avaliar atendimento com IA")}

<section style="background:#F6F8FA;padding:88px 24px;">
  <div style="max-width:1200px;margin:0 auto;">
    <h2 style="font-size:34px;font-weight:700;color:#133A58;margin-bottom:16px;max-width:700px;">O que o agente faz no seu WhatsApp</h2>
    <p style="font-size:17px;line-height:1.7;color:#475467;max-width:640px;margin-bottom:44px;">Triagem, respostas iniciais, qualificação, agendamento e encaminhamento inteligente.</p>
    {cards_grid([
        ("Recepção imediata","Nenhum contato fica sem resposta — nem fora do horário, nem no fim de semana."),
        ("Triagem inteligente","O agente identifica o que o cliente precisa e coleta as informações essenciais."),
        ("Qualificação de leads","Perguntas certas separam curiosos de oportunidades reais, com registro."),
        ("Agendamento","Marcação de horários sem vai-e-volta de mensagens."),
        ("Encaminhamento com contexto","O atendimento humano recebe o histórico organizado — o cliente não repete tudo."),
        ("Acompanhamento","Follow-up de contatos que hoje esfriam e desaparecem."),
    ])}
  </div>
</section>

<section style="background:#0B3B2E;padding:88px 24px;">
  <div style="max-width:1200px;margin:0 auto;">
    <h2 style="font-size:34px;font-weight:700;color:#fff;margin-bottom:40px;max-width:700px;">A diferença entre ser ignorado e ser atendido</h2>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;" class="g-2">
      <div style="background:#101B3D;border:1px solid #1E4636;border-radius:14px;padding:26px;">
        <h3 style="color:#F97066;font-size:15px;font-weight:700;margin-bottom:16px;">Sem automação</h3>
        <p style="color:#D2D9DE;font-size:14.5px;padding:8px 0;border-bottom:1px solid #1E4636;">Cliente envia mensagem</p>
        <p style="color:#D2D9DE;font-size:14.5px;padding:8px 0;border-bottom:1px solid #1E4636;">Aguarda</p>
        <p style="color:#D2D9DE;font-size:14.5px;padding:8px 0;border-bottom:1px solid #1E4636;">Desiste</p>
        <p style="color:#D2D9DE;font-size:14.5px;padding:8px 0;">Procura concorrente</p>
      </div>
      <div style="background:#101B3D;border:1px solid #3A606F;border-radius:14px;padding:26px;">
        <h3 style="color:#3A606F;font-size:15px;font-weight:700;margin-bottom:16px;">Com agente de IA</h3>
        <p style="color:#B0BDCA;font-size:14.5px;padding:8px 0;border-bottom:1px solid #1E4636;">Cliente envia mensagem</p>
        <p style="color:#B0BDCA;font-size:14.5px;padding:8px 0;border-bottom:1px solid #1E4636;">Recebe orientação inicial</p>
        <p style="color:#B0BDCA;font-size:14.5px;padding:8px 0;border-bottom:1px solid #1E4636;">Informa sua necessidade e é qualificado</p>
        <p style="color:#B0BDCA;font-size:14.5px;padding:8px 0;">Atendimento humano recebe o contexto organizado</p>
      </div>
    </div>
    <p style="font-size:17px;line-height:1.7;color:#B7E4CD;max-width:720px;margin-top:36px;">A IA não substitui automaticamente o relacionamento humano. Ela evita que o cliente seja ignorado enquanto ninguém está disponível.</p>
  </div>
</section>

{faq_html(FAQS)}
{CTA_DIAG}
"""
write("automacao-atendimento-whatsapp/index.html", page(
    "Automação de WhatsApp com Inteligência Artificial | Mauricio Ruiz",
    "Agentes de IA para receber contatos, responder dúvidas, qualificar oportunidades e organizar o atendimento pelo WhatsApp.",
    "/automacao-atendimento-whatsapp/", MAIN,
    schemas=[service_schema("Automação de Atendimento e WhatsApp","Triagem, respostas iniciais, qualificação, agendamento e encaminhamento inteligente no WhatsApp."), breadcrumb_schema(BC), faq_schema(FAQS)]))
print("OK whatsapp")
