# Quiz System - Generic Content Loader

Este sistema permite criar quizzes de estudo (flashcards + testes) apenas carregando um ficheiro JSON com o conteúdo, sem necessidade de modificar o código HTML.

## 📁 Ficheiros

- **`quiz-template.html`** - Template genérico (use este para todos os novos quizzes)
- **`content-schema.json`** - Esquema de referência para criar novos conteúdos
- **`ciencias-u1-content.json`** - Exemplo: conteúdo de Ciências Naturais Unidade 1
- **`index.html`** - Versão original (mantida para referência)

## 🚀 Como Usar

### Opção 1: Carregar conteúdo por parâmetro URL (Recomendado)

1. Abra `quiz-template.html` com um parâmetro URL:
   ```
   quiz-template.html?content=ciencias-u1-content.json
   ```

2. Para cada novo tema, crie um ficheiro JSON e carregue-o:
   ```
   quiz-template.html?content=historia-u2-content.json
   quiz-template.html?content=matematica-fracoes.json
   ```

### Opção 2: Conteúdo padrão

Se abrir `quiz-template.html` sem parâmetros, ele carrega automaticamente `ciencias-u1-content.json`.

## 📝 Criar Novo Conteúdo

### 1. Copie o ficheiro de exemplo
```bash
cp ciencias-u1-content.json meu-novo-conteudo.json
```

### 2. Edite o JSON com o seu conteúdo

#### Estrutura básica:

```json
{
  "metadata": {
    "title": "Título do Quiz",
    "subtitle": "Subtítulo ou tema",
    "description": "Descrição adicional",
    "unit": "U1",
    "version": "v1",
    "footer": "Texto do rodapé (opcional)"
  },
  "cards": [
    {
      "id": 1,
      "tema": "Nome do Tema",
      "curto": false,
      "q": "Pergunta aqui?",
      "a": "Resposta aqui."
    }
  ],
  "distractors": {
    "1": [
      "Distrator 1 (resposta incorreta mas plausível)",
      "Distrator 2",
      "Distrator 3"
    ]
  },
  "trueFalse": [
    {
      "t": "Afirmação verdadeira ou falsa",
      "v": true,
      "e": "Explicação da resposta"
    }
  ]
}
```

### 3. Campos obrigatórios

#### Metadata
- `title`: Título principal (ex: "Matemática 7.º — Frações")
- `subtitle`: Subtema (ex: "Operações com frações")
- `description`: Descrição mostrada no cabeçalho
- `unit`: Identificador da unidade (ex: "U2", "MAT_FRAC")
- `version`: Versão do conteúdo (ex: "v1")

#### Cards (flashcards)
- `id`: Número único (inteiro)
- `tema`: Categoria/tema (ex: "Frações Próprias", "Soma de Frações")
- `curto`: `true` ou `false` (indica se é pergunta curta)
- `q`: Texto da pergunta
- `a`: Texto da resposta

#### Distractors (opções incorretas para testes)
- Objeto com chaves sendo IDs dos cartões (como string: `"1"`, `"2"`, etc.)
- Cada valor é um array de 1-5 distratores plausíveis
- São usados nos testes de escolha múltipla

#### TrueFalse (afirmações verdadeiro/falso)
- `t`: Texto da afirmação
- `v`: `true` (verdadeiro) ou `false` (falso)
- `e`: Explicação da resposta

## 💡 Dicas para Criar Bons Distratores

1. **Plausíveis**: Devem parecer corretos à primeira vista
2. **Relacionados**: Usar conceitos do mesmo tema
3. **Comprimento similar**: Ter tamanho parecido com a resposta certa
4. **Baseados em erros comuns**: Refletir mal-entendidos típicos

### Exemplo de distratores eficazes:

```json
{
  "id": 10,
  "q": "O que é a fotossíntese?",
  "a": "Processo pelo qual as plantas produzem glicose usando luz solar, água e CO₂."
}

// Distratores:
"10": [
  "Processo pelo qual as plantas absorvem nutrientes do solo através das raízes.",
  "Processo de respiração das plantas que ocorre durante a noite.",
  "Processo pelo qual as plantas produzem oxigénio sem necessidade de luz."
]
```

## 🎯 Funcionalidades

O template inclui automaticamente:

### 1. **Flashcards (Cartões)**
- Sistema de repetição espaçada (Leitner)
- 3 caixas: 1 dia → 3 dias → 7 dias
- Progresso salvo em `localStorage`
- Estatísticas por tema
- Atalhos de teclado:
  - **Espaço**: Revelar resposta
  - **A**: Acertei
  - **E**: Errei

### 2. **Teste Rápido**
- Escolha múltipla com 4 opções
- Usa distratores do JSON + gerados automaticamente
- 3 níveis de dificuldade:
  - **Fácil**: Distratores mais óbvios
  - **Médio**: Distratores balanceados
  - **Difícil**: Distratores muito semelhantes
- Histórico de resultados

### 3. **Verdadeiro/Falso**
- Afirmações com explicações
- Atalhos de teclado:
  - **V**: Verdadeiro
  - **F**: Falso
  - **Espaço**: Nova afirmação

### 4. **Painel de Progresso**
- Total de cartões estudados
- Cartões dominados (caixa 3)
- Tempo total de estudo
- Streak diário (≥10 cartões/dia)
- Calendário de revisões (14 dias)

### 5. **Exportar/Importar**
- Exportar progresso como JSON
- Importar progresso anterior
- Repor tudo

## 🔧 Personalização Avançada

### Mudar cores e estilos
Edite as variáveis CSS no início do `<style>` em `quiz-template.html`:

```css
:root{
  --bg:#0f172a;      /* Cor de fundo */
  --card:#111827;    /* Cor dos cartões */
  --fg:#e5e7eb;      /* Cor do texto */
  --accent:#22c55e;  /* Cor de destaque */
  /* ... */
}
```

### Ajustar intervalos de revisão
Na função `schedule()`, altere os intervalos:

```javascript
const interval = s.box===1?1:(s.box===2?3:7);  // atual: 1/3/7 dias
// exemplo para 2/5/10 dias:
const interval = s.box===1?2:(s.box===2?5:10);
```

## 📊 Progresso e Dados

### Armazenamento local
- Chave: `QUIZ_{unit}_{version}_progress`
- Exemplo: `QUIZ_U1_v2_progress`
- Cada conteúdo tem progresso independente

### Formato do progresso exportado:
```json
{
  "progress": {
    "1": {
      "box": 2,
      "seen": 3,
      "right": 2,
      "wrong": 1,
      "next": "2025-10-27",
      "last": "2025-10-26"
    }
  },
  "stats": {
    "timeSec": 1200,
    "streak": 5,
    "lastDay": "2025-10-26",
    "quiz": [...]
  },
  "contentKey": "QUIZ_U1_v2"
}
```

## 🐛 Resolução de Problemas

### Erro: "JSON inválido"
- Verifique se todos os campos obrigatórios estão presentes
- Use um validador JSON online (jsonlint.com)
- Compare com `ciencias-u1-content.json`

### Distratores não aparecem
- Certifique-se que as chaves em `distractors` são strings (`"1"` não `1`)
- Verifique se os IDs correspondem aos cartões

### Progresso não salva
- Verifique se o navegador permite `localStorage`
- Modo privado/incógnito não salva dados

### Conteúdo não carrega
- Verifique o caminho do ficheiro JSON
- Abra o Console do navegador (F12) para ver erros
- Certifique-se que o ficheiro está na mesma pasta

## 📚 Exemplo Completo Mínimo

```json
{
  "metadata": {
    "title": "Teste Simples",
    "subtitle": "Exemplo mínimo",
    "description": "Um quiz básico",
    "unit": "TEST",
    "version": "v1"
  },
  "cards": [
    {
      "id": 1,
      "tema": "Básico",
      "curto": true,
      "q": "Quanto é 2+2?",
      "a": "4"
    },
    {
      "id": 2,
      "tema": "Básico",
      "curto": true,
      "q": "Capital de Portugal?",
      "a": "Lisboa"
    }
  ],
  "distractors": {
    "1": ["3", "5", "22"],
    "2": ["Porto", "Coimbra", "Faro"]
  },
  "trueFalse": [
    {
      "t": "2+2 é igual a 4",
      "v": true,
      "e": "Matemática básica"
    },
    {
      "t": "Lisboa fica no norte de Portugal",
      "v": false,
      "e": "Lisboa fica no centro-sul"
    }
  ]
}
```

## 🎓 Workflow Recomendado

1. **Preparar conteúdo**: 
   - Organize perguntas e respostas num documento
   - Agrupe por temas
   
2. **Criar JSON**:
   - Use `content-schema.json` como referência
   - Valide o JSON antes de usar

3. **Criar distratores**:
   - Pelo menos 2-3 por pergunta importante
   - Baseie-se em erros comuns dos alunos

4. **Testar**:
   - Abra o quiz e teste todas as funcionalidades
   - Verifique se distratores fazem sentido

5. **Ajustar**:
   - Refine distratores que sejam muito óbvios
   - Adicione mais afirmações V/F se necessário

## 📞 Suporte

Para dúvidas sobre a estrutura JSON, consulte `content-schema.json` que documenta todos os campos aceites.

---

**Criado para facilitar a criação de materiais de estudo interativos! 🚀**

