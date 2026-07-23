#!/usr/bin/env python3
"""Gera /mentoria-implantacao-ia/"""
import sys, json
sys.path.insert(0, "/root/projects/mauricioruiz-com-br/build")
from base import page, breadcrumb, breadcrumb_schema, faq_html, faq_schema, CTA_DIAG, write

BC = [("Início", "/"), ("Mentoria de Implantação de IA", None)]

FAQS = [
    ("A mentoria inclui implantação técnica?",
     "Inclui diagnóstico, planejamento, priorização, desenho dos processos e acompanhamento da implantação. A execução técnica pode fazer parte do escopo ou ser realizada por fornecedores específicos, sob orientação estratégica. A definição depende da complexidade das automações e integrações envolvidas."),
    ("Preciso entender de tecnologia para contratar?",
     "Não. A função da mentoria é traduzir possibilidades técnicas em decisões empresariais compreensíveis. Você precisa conhecer o próprio negócio, os problemas da operação e os resultados que pretende alcançar."),
    ("Quanto tempo leva?",
     "Depende da complexidade do processo. Projetos simples envolvem poucos fluxos e integrações. Projetos avançados exigem mapeamento, organização das informações, testes e treinamento. O prazo é definido depois do diagnóstico — prometer velocidade antes de entender o processo é vender improviso."),
    ("Quanto custa?",
     "O investimento depende do problema, do processo, do volume de uso, das integrações e do nível de personalização. Por isso o preço não é definido antes de compreender o que precisa ser implantado."),
    ("Como os resultados são medidos?",
     "Os indicadores são definidos antes da implantação: tempo de resposta, tarefas manuais reduzidas, leads acompanhados, erros operacionais, tempo economizado pela equipe. Sem situação inicial registrada, não existe comparação confiável entre antes e depois."),
]

MAIN = f"""
{breadcrumb(BC)}

<section style="background:#ffffff;padding:72px 24px 80px;">
  <div style="max-width:1200px;margin:0 auto;">
    <span style="display:inline-block;background:#F4F8FB;border:1px solid #E4E7EC;color:#00A3D7;font-size:13px;font-weight:700;padding:6px 14px;border-radius:100px;margin-bottom:20px;">Serviço principal</span>
    <h1 style="font-size:44px;line-height:1.15;font-weight:800;color:#0B1026;margin-bottom:24px;max-width:820px;">Implantar Inteligência Artificial não começa escolhendo uma ferramenta</h1>
    <p style="font-size:19px;line-height:1.6;color:#475467;max-width:680px;margin-bottom:32px;">Começa identificando onde sua empresa perde tempo, dinheiro, informação e oportunidades. A mentoria transforma a intenção de usar IA em um plano de implantação.</p>
    <div style="display:flex;flex-wrap:wrap;gap:14px;">
      <a href="/diagnostico-de-ia/" style="background:#00A3D7;color:#0B1026;font-weight:700;font-size:16px;padding:16px 26px;border-radius:8px;">Quero avaliar minha empresa</a>
      <a href="https://wa.me/5527920000167" target="_blank" rel="noopener" style="background:#fff;border:1px solid #D0D5DD;color:#0B1026;font-weight:600;font-size:16px;padding:16px 26px;border-radius:8px;">Falar pelo WhatsApp</a>
    </div>
  </div>
</section>

<section style="background:#F4F8FB;padding:88px 24px;">
  <div style="max-width:1200px;margin:0 auto;">
    <h2 style="font-size:34px;font-weight:700;color:#0B1026;margin-bottom:20px;max-width:720px;">O erro mais comum começa antes da compra</h2>
    <p style="font-size:17px;line-height:1.7;color:#475467;max-width:680px;margin-bottom:16px;">A maioria dos projetos de IA fracassa por motivos que nada têm a ver com tecnologia:</p>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:36px;" class="g-4">
      <div style="background:#fff;border:1px solid #E4E7EC;border-radius:12px;padding:26px 22px;">
        <h3 style="font-size:17px;font-weight:700;color:#0B1026;margin-bottom:10px;">Ferramenta antes do problema</h3>
        <p style="font-size:14.5px;line-height:1.6;color:#667085;">A empresa compra a solução e depois procura onde encaixá-la. O resultado é assinatura sem uso.</p>
      </div>
      <div style="background:#fff;border:1px solid #E4E7EC;border-radius:12px;padding:26px 22px;">
        <h3 style="font-size:17px;font-weight:700;color:#0B1026;margin-bottom:10px;">Automação do caos</h3>
        <p style="font-size:14.5px;line-height:1.6;color:#667085;">Automatizar um processo ruim só faz o erro acontecer mais rápido — e em escala.</p>
      </div>
      <div style="background:#fff;border:1px solid #E4E7EC;border-radius:12px;padding:26px 22px;">
        <h3 style="font-size:17px;font-weight:700;color:#0B1026;margin-bottom:10px;">Projeto sem dono</h3>
        <p style="font-size:14.5px;line-height:1.6;color:#667085;">Sem liderança envolvida e critérios definidos, a implantação vira experimento eterno.</p>
      </div>
      <div style="background:#fff;border:1px solid #E4E7EC;border-radius:12px;padding:26px 22px;">
        <h3 style="font-size:17px;font-weight:700;color:#0B1026;margin-bottom:10px;">Consultoria de apresentação</h3>
        <p style="font-size:14.5px;line-height:1.6;color:#667085;">Relatório bonito que termina em slide não é implantação. Nada muda na operação.</p>
      </div>
    </div>
  </div>
</section>

<section style="background:#ffffff;padding:88px 24px;">
  <div style="max-width:1200px;margin:0 auto;">
    <h2 style="font-size:34px;font-weight:700;color:#0B1026;margin-bottom:16px;max-width:720px;">O que é a mentoria</h2>
    <p style="font-size:17px;line-height:1.7;color:#475467;max-width:680px;margin-bottom:16px;">Diagnóstico, planejamento e acompanhamento da implantação de Inteligência Artificial dentro da empresa. O trabalho começa pelo negócio, pelos processos e pelos resultados esperados. Só depois são escolhidas as ferramentas.</p>
    <p style="font-size:20px;font-weight:700;color:#0B1026;max-width:640px;margin-bottom:52px;">IA sem direção vira despesa. Com processo, pode virar capacidade operacional.</p>
    <div style="display:grid;grid-template-columns:repeat(7,1fr);gap:14px;" class="g-7">
      <div style="border-top:3px solid #00A3D7;padding-top:16px;"><span style="font-size:13px;font-weight:700;color:#00A3D7;">01</span><h3 style="font-size:15.5px;font-weight:700;color:#0B1026;margin:6px 0 8px;">Diagnóstico</h3><p style="font-size:13.5px;line-height:1.55;color:#667085;">Gargalos, desperdícios, riscos e oportunidades identificados.</p></div>
      <div style="border-top:3px solid #00A3D7;padding-top:16px;"><span style="font-size:13px;font-weight:700;color:#00A3D7;">02</span><h3 style="font-size:15.5px;font-weight:700;color:#0B1026;margin:6px 0 8px;">Mapeamento</h3><p style="font-size:13.5px;line-height:1.55;color:#667085;">Como as tarefas realmente acontecem dentro da empresa.</p></div>
      <div style="border-top:3px solid #00A3D7;padding-top:16px;"><span style="font-size:13px;font-weight:700;color:#00A3D7;">03</span><h3 style="font-size:15.5px;font-weight:700;color:#0B1026;margin:6px 0 8px;">Priorização</h3><p style="font-size:13.5px;line-height:1.55;color:#667085;">O que parece moderno separado do que gera resultado.</p></div>
      <div style="border-top:3px solid #00A3D7;padding-top:16px;"><span style="font-size:13px;font-weight:700;color:#00A3D7;">04</span><h3 style="font-size:15.5px;font-weight:700;color:#0B1026;margin:6px 0 8px;">Planejamento</h3><p style="font-size:13.5px;line-height:1.55;color:#667085;">Objetivos, responsabilidades, ferramentas e critérios.</p></div>
      <div style="border-top:3px solid #00A3D7;padding-top:16px;"><span style="font-size:13px;font-weight:700;color:#00A3D7;">05</span><h3 style="font-size:15.5px;font-weight:700;color:#0B1026;margin:6px 0 8px;">Implantação</h3><p style="font-size:13.5px;line-height:1.55;color:#667085;">Agentes, automações, integrações e processos construídos.</p></div>
      <div style="border-top:3px solid #00A3D7;padding-top:16px;"><span style="font-size:13px;font-weight:700;color:#00A3D7;">06</span><h3 style="font-size:15.5px;font-weight:700;color:#0B1026;margin:6px 0 8px;">Treinamento</h3><p style="font-size:13.5px;line-height:1.55;color:#667085;">Empresários e equipes preparados para a nova estrutura.</p></div>
      <div style="border-top:3px solid #00A3D7;padding-top:16px;"><span style="font-size:13px;font-weight:700;color:#00A3D7;">07</span><h3 style="font-size:15.5px;font-weight:700;color:#0B1026;margin:6px 0 8px;">Medição</h3><p style="font-size:13.5px;line-height:1.55;color:#667085;">Tempo, eficiência, resposta, custo e qualidade comparados.</p></div>
    </div>
  </div>
</section>

<section style="background:#F4F8FB;padding:88px 24px;">
  <div style="max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1.4fr 1fr;gap:56px;" class="g-pq">
    <div>
      <h2 style="font-size:32px;font-weight:700;color:#0B1026;margin-bottom:28px;">O que você recebe</h2>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;" class="g-pqi">
        <div style="display:flex;gap:10px;align-items:flex-start;font-size:15px;color:#344054;line-height:1.5;"><span style="color:#00A3D7;flex-shrink:0;">✓</span>Diagnóstico inicial</div>
        <div style="display:flex;gap:10px;align-items:flex-start;font-size:15px;color:#344054;line-height:1.5;"><span style="color:#00A3D7;flex-shrink:0;">✓</span>Mapa de oportunidades</div>
        <div style="display:flex;gap:10px;align-items:flex-start;font-size:15px;color:#344054;line-height:1.5;"><span style="color:#00A3D7;flex-shrink:0;">✓</span>Priorização de projetos</div>
        <div style="display:flex;gap:10px;align-items:flex-start;font-size:15px;color:#344054;line-height:1.5;"><span style="color:#00A3D7;flex-shrink:0;">✓</span>Plano de implantação</div>
        <div style="display:flex;gap:10px;align-items:flex-start;font-size:15px;color:#344054;line-height:1.5;"><span style="color:#00A3D7;flex-shrink:0;">✓</span>Definição das ferramentas</div>
        <div style="display:flex;gap:10px;align-items:flex-start;font-size:15px;color:#344054;line-height:1.5;"><span style="color:#00A3D7;flex-shrink:0;">✓</span>Desenho dos fluxos</div>
        <div style="display:flex;gap:10px;align-items:flex-start;font-size:15px;color:#344054;line-height:1.5;"><span style="color:#00A3D7;flex-shrink:0;">✓</span>Orientação para agentes de IA</div>
        <div style="display:flex;gap:10px;align-items:flex-start;font-size:15px;color:#344054;line-height:1.5;"><span style="color:#00A3D7;flex-shrink:0;">✓</span>Plano de treinamento</div>
        <div style="display:flex;gap:10px;align-items:flex-start;font-size:15px;color:#344054;line-height:1.5;"><span style="color:#00A3D7;flex-shrink:0;">✓</span>Critérios de medição</div>
        <div style="display:flex;gap:10px;align-items:flex-start;font-size:15px;color:#344054;line-height:1.5;"><span style="color:#00A3D7;flex-shrink:0;">✓</span>Acompanhamento estratégico</div>
      </div>
    </div>
    <div style="background:#0B1026;border-radius:16px;padding:32px;">
      <h3 style="color:#fff;font-size:19px;font-weight:700;margin-bottom:8px;">Limites claros</h3>
      <p style="color:#98A2B3;font-size:14px;margin-bottom:20px;">A mentoria não promete:</p>
      <div style="display:flex;flex-direction:column;gap:10px;">
        <div style="display:flex;gap:10px;align-items:flex-start;font-size:14.5px;color:#D2D9DE;line-height:1.5;"><span style="color:#F97066;flex-shrink:0;">–</span>Resultado garantido sem diagnóstico</div>
        <div style="display:flex;gap:10px;align-items:flex-start;font-size:14.5px;color:#D2D9DE;line-height:1.5;"><span style="color:#F97066;flex-shrink:0;">–</span>Automação total da operação</div>
        <div style="display:flex;gap:10px;align-items:flex-start;font-size:14.5px;color:#D2D9DE;line-height:1.5;"><span style="color:#F97066;flex-shrink:0;">–</span>Implantação instantânea</div>
        <div style="display:flex;gap:10px;align-items:flex-start;font-size:14.5px;color:#D2D9DE;line-height:1.5;"><span style="color:#F97066;flex-shrink:0;">–</span>Substituição indiscriminada de pessoas</div>
        <div style="display:flex;gap:10px;align-items:flex-start;font-size:14.5px;color:#D2D9DE;line-height:1.5;"><span style="color:#F97066;flex-shrink:0;">–</span>Solução pronta copiada de outra empresa</div>
      </div>
    </div>
  </div>
</section>

<section style="background:#ffffff;padding:88px 24px;">
  <div style="max-width:1200px;margin:0 auto;">
    <h2 style="font-size:32px;font-weight:700;color:#0B1026;margin-bottom:12px;max-width:680px;">Para quem é</h2>
    <p style="font-size:17px;color:#475467;margin-bottom:36px;max-width:640px;">Empresas que querem começar a usar IA com direção — ou que já usam ferramentas, mas sem processo, sem integração e sem critério.</p>
    <h2 style="font-size:32px;font-weight:700;color:#0B1026;margin-bottom:12px;max-width:680px;">O que será analisado</h2>
    <p style="font-size:17px;color:#475467;margin-bottom:36px;max-width:680px;">Atendimento, vendas, marketing, operações, informações internas e tomada de decisão. Onde existe repetição, espera, retrabalho ou dependência de memória, existe candidato a melhoria.</p>
    <div style="background:#0B3B2E;border-radius:16px;padding:36px;text-align:center;">
      <p style="font-size:22px;font-weight:700;color:#00A3D7;line-height:1.4;max-width:760px;margin:0 auto;">Nem todo processo precisa de Inteligência Artificial. Alguns precisam apenas de clareza e disciplina operacional.</p>
    </div>
  </div>
</section>

{faq_html(FAQS)}

{CTA_DIAG}
"""

SERVICE_SCHEMA = json.dumps({
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "Mentoria de Implantação de Inteligência Artificial",
    "provider": {"@type": "ProfessionalService", "name": "Mauricio Ruiz | Mentor de Inteligência Artificial",
                 "url": "https://mauricioruiz.com.br/"},
    "areaServed": ["Vila Velha", "Vitória", "Grande Vitória", "Espírito Santo", "Brasil"],
    "description": "Diagnóstico, planejamento e acompanhamento da implantação de Inteligência Artificial com prioridade, processo e critérios de resultado."
}, ensure_ascii=False, indent=1)

write("mentoria-implantacao-ia/index.html", page(
    "Mentoria de Inteligência Artificial para Empresas | Mauricio Ruiz",
    "Diagnóstico, planejamento e acompanhamento para implantar Inteligência Artificial com prioridade, processo e critérios de resultado.",
    "/mentoria-implantacao-ia/",
    MAIN,
    schemas=[SERVICE_SCHEMA, breadcrumb_schema(BC), faq_schema(FAQS)]
))
print("OK mentoria")
