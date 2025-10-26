# 🚀 Quick Start Guide

## Para Começar AGORA (3 passos)

### 1️⃣ Abrir o Quiz
Abra `index-launcher.html` no seu navegador e escolha um conteúdo existente.

**OU**

Abra `quiz-template.html?content=ciencias-u1-content.json` diretamente.

### 2️⃣ Criar Novo Conteúdo (5 minutos)

```bash
# 1. Copie o template vazio
cp template-empty.json meu-quiz.json

# 2. Edite com as suas perguntas e respostas
# (use qualquer editor de texto)

# 3. Abra no navegador
# quiz-template.html?content=meu-quiz.json
```

### 3️⃣ Estrutura Mínima do JSON

```json
{
  "metadata": {
    "title": "Meu Quiz",
    "subtitle": "Tema",
    "description": "Descrição",
    "unit": "ID",
    "version": "v1"
  },
  "cards": [
    {
      "id": 1,
      "tema": "Categoria",
      "curto": false,
      "q": "Pergunta?",
      "a": "Resposta."
    }
  ],
  "distractors": {
    "1": ["Errada 1", "Errada 2", "Errada 3"]
  },
  "trueFalse": [
    {
      "t": "Afirmação",
      "v": true,
      "e": "Explicação"
    }
  ]
}
```

## ✅ Checklist para Novo Conteúdo

- [ ] Metadata preenchida (title, subtitle, unit, version)
- [ ] Cada cartão tem ID único
- [ ] Cada cartão tem tema, pergunta e resposta
- [ ] Distratores têm chave como string ("1", "2", não 1, 2)
- [ ] Pelo menos 2-3 distratores por cartão importante
- [ ] Afirmações V/F têm explicações
- [ ] JSON validado (use jsonlint.com se tiver dúvidas)

## 🎯 Dicas Rápidas

### Bons Distratores
✅ "Passagem de gasoso a líquido" (quando a certa é "líquido a gasoso")  
❌ "Maçã" (quando a pergunta é sobre química)

### Organização
- Use IDs espaçados (1, 10, 20...) para facilitar adicionar depois
- Agrupe cartões por tema
- Temas consistentes ajudam no progresso

### Testes
- Abra o Console (F12) se algo não funcionar
- Valide o JSON antes de testar
- Compare com `ciencias-u1-content.json` se tiver dúvidas

## 📂 Ficheiros Importantes

| Ficheiro | O Que É |
|----------|---------|
| `quiz-template.html` | Template genérico (use este!) |
| `index-launcher.html` | Menu de seleção de conteúdos |
| `template-empty.json` | Template vazio para copiar |
| `content-schema.json` | Documentação completa dos campos |
| `README.md` | Guia completo detalhado |

## 💡 Exemplos Prontos

- `ciencias-u1-content.json` - Ciências Naturais (34 cartões)
- `example-historia.json` - História (10 cartões, exemplo simples)

## 🆘 Problemas Comuns

**Erro: "JSON inválido"**
→ Use jsonlint.com para validar

**Distratores não aparecem**
→ Chaves devem ser strings: `"1"` não `1`

**Página em branco**
→ Verifique Console (F12) e caminho do ficheiro

**Progresso não salva**
→ Cada conteúdo tem progresso separado (baseado em unit + version)

## 🎓 Workflow Ideal

1. **Prepare** perguntas num documento
2. **Copie** `template-empty.json`
3. **Preencha** com seu conteúdo
4. **Valide** o JSON
5. **Teste** abrindo no navegador
6. **Refine** distratores conforme necessário

## 🔗 Próximos Passos

- Leia `README.md` para detalhes completos
- Veja `content-schema.json` para todos os campos
- Experimente criar um quiz pequeno (3-5 cartões) primeiro
- Depois expanda para conteúdo completo

---

**Dica**: Comece pequeno! Um quiz com 5 cartões bem feitos é melhor que 50 cartões apressados. Pode sempre adicionar mais depois! 🚀

