# 🔄 Workflow Guide - Creating Your First Quiz

## 🎯 Two Paths to Choose From

### Path A: Quick Test (5 minutes)
**Goal:** See how it works with existing content

### Path B: Create New Content (15 minutes)
**Goal:** Build your own quiz from scratch

---

## 🅰️ PATH A: Quick Test

```
START
  │
  ▼
1. Open index-launcher.html in browser
  │
  ▼
2. Click "Ciências Naturais 5.º" (or "História")
  │
  ▼
3. Explore the interface:
   ├─ Try flashcards mode
   ├─ Try quiz mode
   ├─ Try true/false mode
   └─ Check progress panel
  │
  ▼
4. Study a few cards, mark as right/wrong
  │
  ▼
5. Refresh page - progress is saved!
  │
  ▼
DONE! ✅ You've seen how it works.

Next: Ready for Path B? →
```

---

## 🅱️ PATH B: Create Your Own Quiz

### Step 1: Prepare Your Content (Paper & Pen)

```
✏️ Write down:
  
  1. Subject & Topic
     Example: "Matemática - Frações"
  
  2. Questions & Answers (at least 5-10)
     Q: O que é uma fração?
     A: Representação de uma parte de um todo.
     
     Q: Como se lê 3/4?
     A: Três quartos.
  
  3. For each question, think of 3 wrong answers
     (that seem right but aren't)
     
     For "O que é uma fração?":
     ❌ Um número decimal com vírgula
     ❌ Uma percentagem maior que 100%
     ❌ Um número negativo
  
  4. Write 5-10 true/false statements
     ✓ Uma fração representa parte de um todo
     ✗ Todas as frações são maiores que 1
```

**Time estimate:** 10-15 minutes  
**Tip:** Start small! 5 cards is better than 50 poorly written ones.

---

### Step 2: Create JSON File

```
Terminal:
$ cd /path/to/quiz/folder
$ cp template-empty.json matematica-fracoes.json

OR

File Explorer:
- Copy template-empty.json
- Rename to matematica-fracoes.json
```

**Time estimate:** 30 seconds

---

### Step 3: Fill in the JSON

Open `matematica-fracoes.json` in any text editor:

```json
{
  "metadata": {
    "title": "Matemática 5.º — Frações",
    "subtitle": "Introdução às frações",
    "description": "Conceitos básicos de frações",
    "unit": "MAT_FRAC",
    "version": "v1"
  },
  
  "cards": [
    {
      "id": 1,
      "tema": "Conceitos",
      "curto": false,
      "q": "O que é uma fração?",
      "a": "Representação de uma parte de um todo."
    },
    {
      "id": 2,
      "tema": "Leitura",
      "curto": true,
      "q": "Como se lê 3/4?",
      "a": "Três quartos."
    }
    // ... add more cards
  ],
  
  "distractors": {
    "1": [
      "Um número decimal com vírgula.",
      "Uma percentagem maior que 100%.",
      "Um número negativo."
    ],
    "2": [
      "Três sobre quatro.",
      "Três dividido quatro.",
      "Três ponto quatro."
    ]
    // ... add more
  },
  
  "trueFalse": [
    {
      "t": "Uma fração representa parte de um todo.",
      "v": true,
      "e": "Definição correta de fração."
    },
    {
      "t": "Todas as frações são maiores que 1.",
      "v": false,
      "e": "Frações próprias são menores que 1."
    }
    // ... add more
  ]
}
```

**Time estimate:** 5-10 minutes  
**Tip:** Use VS Code, Sublime, or even Notepad - just make sure it's plain text!

---

### Step 4: Validate Your JSON

**Option 1: Online Validator**
```
1. Go to jsonlint.com
2. Paste your JSON
3. Click "Validate JSON"
4. Fix any errors shown
```

**Option 2: Browser Console**
```
1. Open quiz-template.html?content=matematica-fracoes.json
2. Press F12 (Developer Tools)
3. Check Console tab for errors
```

**Time estimate:** 2 minutes

---

### Step 5: Test Your Quiz

```
1. Open in browser:
   quiz-template.html?content=matematica-fracoes.json

2. Test each mode:
   ✓ Flashcards - do questions appear correctly?
   ✓ Quiz - are distractors plausible?
   ✓ True/False - do explanations make sense?

3. Check for issues:
   - Typos in text
   - Wrong answers marked as correct
   - Distractors too obvious or too hard
   - Missing explanations
```

**Time estimate:** 3-5 minutes

---

### Step 6: Refine & Publish

```
1. Fix any issues found during testing

2. Add your quiz to index-launcher.html (optional):
   
   <div class="content-card" onclick="loadQuiz('matematica-fracoes.json')">
     <div class="content-info">
       <h2>Matemática 5.º — Frações</h2>
       <p>Introdução às frações • 10 cartões</p>
     </div>
     <div>
       <span class="badge">Matemática</span>
       <span class="arrow">→</span>
     </div>
   </div>

3. Share with students!
```

**Time estimate:** 2 minutes

---

## ✅ Completion Checklist

Before sharing your quiz, verify:

### Content Quality
- [ ] Questions are clear and unambiguous
- [ ] Answers are concise but complete
- [ ] Distractors are plausible (not too easy/hard)
- [ ] No typos or grammatical errors
- [ ] True/False explanations are helpful

### Technical Validation
- [ ] JSON is valid (checked with validator)
- [ ] All card IDs are unique
- [ ] Distractor keys match card IDs (as strings!)
- [ ] Each card has at least 2 distractors
- [ ] Metadata is filled in correctly

### Testing
- [ ] Opened quiz in browser - no errors
- [ ] Tested flashcard mode
- [ ] Tested quiz mode (all difficulty levels)
- [ ] Tested true/false mode
- [ ] Progress saves and loads correctly
- [ ] Mobile view looks good

---

## 🔄 Ongoing Workflow

### When Adding Content

```
1. Student feedback: "We need more about topic X"
   │
   ▼
2. Open your JSON file
   │
   ▼
3. Add new cards to "cards" array
   │
   ▼
4. Add distractors to "distractors" object
   │
   ▼
5. Add true/false if applicable
   │
   ▼
6. Validate JSON
   │
   ▼
7. Test new questions
   │
   ▼
8. Save & share updated file
   │
   ▼
DONE! Students see new content immediately.
```

### When Fixing Mistakes

```
1. Spot typo or error
   │
   ▼
2. Open JSON in editor
   │
   ▼
3. Fix the mistake
   │
   ▼
4. Save file
   │
   ▼
5. Refresh browser
   │
   ▼
DONE! Fixed in seconds.
```

### When Creating New Version

```
1. Copy existing JSON
   matematica-fracoes-v2.json
   │
   ▼
2. Update "version": "v2" in metadata
   │
   ▼
3. Make changes
   │
   ▼
4. Students can:
   - Keep using v1 (old content)
   - Switch to v2 (new content)
   - Both have independent progress!
```

---

## 💡 Pro Tips

### Efficiency Tips

1. **Use templates for similar cards**
   ```json
   // Pattern for definitions
   {"q": "Define X", "a": "X is..."}
   
   // Pattern for examples
   {"q": "Give an example of X", "a": "Example: ..."}
   ```

2. **Batch create in spreadsheet, convert to JSON**
   - Use Google Sheets or Excel
   - Export as CSV
   - Convert CSV to JSON (online tools available)

3. **Reuse distractors across similar questions**
   - Create a "distractor bank"
   - Copy/paste appropriate ones

4. **Use incremental IDs (1, 10, 20, 30...)**
   - Makes it easier to insert cards later
   - Better organization

### Quality Tips

1. **Good distractor = based on common mistake**
   ```
   Q: What is 2 + 2?
   ✅ Good: "5" (off by one error)
   ❌ Bad: "elephant" (nonsensical)
   ```

2. **Test on someone else**
   - Ask a friend to try the quiz
   - Watch where they get confused
   - Refine based on feedback

3. **Mix difficulty levels**
   - Some easy cards (confidence boost)
   - Some hard cards (challenge)
   - Progression in complexity

4. **Group by theme logically**
   - Makes studying more coherent
   - Students can focus on weak themes

---

## 📊 Time Investment Summary

| Task | First Time | After Practice |
|------|-----------|----------------|
| Prepare content | 10-15 min | 5-10 min |
| Create JSON | 5-10 min | 2-3 min |
| Validate | 2 min | 30 sec |
| Test | 3-5 min | 1-2 min |
| **TOTAL** | **20-30 min** | **8-15 min** |

Compare to original method:
- Editing HTML: 30-60 minutes
- Risk of breaking code
- Hard to maintain

**New method is 2-4× faster!** ⚡

---

## 🎯 Next Steps After Your First Quiz

1. **Gather feedback**
   - Ask students what works
   - Identify confusing questions
   - Find gaps in coverage

2. **Iterate**
   - Add more cards
   - Improve distractors
   - Expand true/false section

3. **Create more quizzes**
   - Different subjects
   - Different difficulty levels
   - Different styles (vocabulary vs concepts)

4. **Share & collaborate**
   - Share JSON files with colleagues
   - Version control (Git)
   - Build a content library

---

## 🆘 Troubleshooting Common Issues

### "Page is blank"
```
1. Check browser console (F12)
2. Look for error message
3. Common causes:
   - JSON file not found (check filename)
   - Invalid JSON syntax (use validator)
   - Wrong file path
```

### "Distractors don't appear"
```
1. Check distractor keys are STRINGS
   ✅ "1": [...]
   ❌ 1: [...]
   
2. Check keys match card IDs
   Card ID 5 → Distractor key "5"
```

### "Progress doesn't save"
```
1. Check if localStorage is enabled
2. Not in private/incognito mode?
3. Browser has storage space?
```

### "JSON is invalid"
```
1. Copy entire JSON to jsonlint.com
2. Look at line number of error
3. Common issues:
   - Missing comma
   - Extra comma
   - Missing quote
   - Wrong bracket type
```

---

## 🎓 You're Ready!

You now have everything you need to:
- ✅ Create unlimited quizzes
- ✅ Maintain them easily
- ✅ Share with students
- ✅ Iterate based on feedback

**Start with Path A to see how it works, then try Path B to create your own!**

Good luck! 🚀

