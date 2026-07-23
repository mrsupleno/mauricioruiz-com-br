# mauricioruiz.com.br — Mauricio Ruiz | Mentor de Inteligência Artificial

Site institucional estático. **Hospedagem: Cloudflare Pages** (projeto `mauricioruiz`).

## ⚠️ Deploy NÃO é automático

Este repo **não está conectado** ao Cloudflare Pages. Nenhum `git push` publica nada sozinho.

Circuito oficial (padrão do ecossistema):

1. **Link Flow / Claude** edita e commita neste repo (branch própria ou `main`, conforme combinado)
2. **MRdigital (Hermes)** puxa, valida o diff (WhatsApp, canonical, páginas removidas, fatos inventados, telefone oficial)
3. **MRdigital** faz o deploy: `npx wrangler pages deploy . --project-name mauricioruiz --branch main`

- Branch `main` = produção (`mauricioruiz.com.br`)
- Outras branches = preview (`<branch>.mauricioruiz.pages.dev`)
- Sem build step — publish direto da raiz

## Dados oficiais (imutáveis — NÃO alterar sem o Maurício)

- Telefone/WhatsApp: **(27) 92000-0167** · `wa.me/5527920000167` (0166 é o número da TERAPIA — erro nos docs originais do projeto)
- Endereço: Rua Marajó, 77, Unidade 402, Praia da Costa, Vila Velha – ES, CEP 29101-250
- Horário humano: seg–sex, 9h–18h (agentes de IA 24h não contam como horário humano)
- Formulário: FormSubmit → `mauricio@sucesso.com.br`

## Estrutura

```
index.html                     Home (gerada uma vez a partir do Design Component; editar direto)
<pagina>/index.html            Páginas internas — NÃO editar direto: editar build/p_*.py e rodar
build/                         Geradores Python (fonte de verdade das páginas internas)
assets/                        Imagens WebP otimizadas
robots.txt / sitemap.xml       SEO técnico (atualizar sitemap ao criar página)
404.html                       Página de erro
```

## Páginas internas: como editar

```bash
cd build
python3 p_mentoria.py        # regenera mentoria-implantacao-ia/index.html
python3 p_servicos.py        # regenera agentes/automacao/whatsapp
python3 p_institucional.py   # regenera sobre/diagnostico/contato
python3 p_legais.py          # regenera legais + robots + sitemap + 404
```

Header/footer/CSS/menu são extraídos da `index.html` (home) automaticamente por `build/base.py`.
Mudou a home → rode os 4 geradores para propagar.

## Fase 2 (pendente)

- `/automacao-marketing-vendas/`, `/integracao-ia-sistemas/`, `/treinamento-inteligencia-artificial/`
- `/blog/` + artigos (clusters do doc 05)
- Cards da home que hoje apontam para `/diagnostico-de-ia/` devem apontar para as páginas reais quando existirem
