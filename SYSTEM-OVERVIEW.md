# 📐 System Architecture Overview

## 🏗️ How It Works

```
┌─────────────────────────────────────────────────────────────┐
│                     USER OPENS BROWSER                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
         ┌────────────────────────────────────────┐
         │     index-launcher.html (OPTIONAL)     │
         │   ┌──────────────────────────────┐     │
         │   │  📚 Ciências Naturais        │─────┼───┐
         │   │  📚 História                 │─────┼───┤
         │   │  🔧 Custom file...           │─────┼───┤
         │   └──────────────────────────────┘     │   │
         └────────────────────────────────────────┘   │
                              │                       │
                              ▼                       │
         ┌────────────────────────────────────────┐   │
         │       quiz-template.html               │◄──┘
         │    ?content=ciencias-u1-content.json   │
         │                                         │
         │  ┌──────────────────────────────┐      │
         │  │  1. Loads JSON file          │      │
         │  │  2. Validates structure      │      │
         │  │  3. Updates page title/text  │      │
         │  │  4. Initializes quiz engine  │      │
         │  └──────────────────────────────┘      │
         └────────────────────────────────────────┘
                              │
                              ▼
         ┌────────────────────────────────────────┐
         │        Content JSON File                │
         │   (e.g., ciencias-u1-content.json)     │
         │                                         │
         │  {                                      │
         │    "metadata": {...},                   │
         │    "cards": [...],                      │
         │    "distractors": {...},                │
         │    "trueFalse": [...]                   │
         │  }                                      │
         └────────────────────────────────────────┘
                              │
                              ▼
         ┌────────────────────────────────────────┐
         │         QUIZ INTERFACE                  │
         │  ┌──────────────────────────────┐      │
         │  │ 📇 Flashcards Mode           │      │
         │  │ 📝 Quiz Mode                 │      │
         │  │ ✓✗ True/False Mode           │      │
         │  │ 📊 Progress Panel            │      │
         │  │ 🖨️ Print Cards               │      │
         │  └──────────────────────────────┘      │
         └────────────────────────────────────────┘
                              │
                              ▼
         ┌────────────────────────────────────────┐
         │         localStorage                    │
         │   QUIZ_{unit}_{version}_progress       │
         │   QUIZ_{unit}_{version}_stats          │
         └────────────────────────────────────────┘
```

## 📦 File Relationships

```
PROJECT ROOT
│
├── 🌟 START HERE
│   ├── index-launcher.html ────► Launch menu (optional starting point)
│   └── quiz-template.html ─────► Main quiz engine (the core!)
│
├── 📝 CONTENT FILES (JSON)
│   ├── ciencias-u1-content.json ─► Science quiz (your original)
│   ├── example-historia.json ────► History quiz (example)
│   └── [your-new-quiz].json ─────► Your future quizzes!
│
├── 📋 TEMPLATES & SCHEMAS
│   ├── template-empty.json ──────► Copy this to create new content
│   └── content-schema.json ──────► Reference for JSON structure
│
├── 📖 DOCUMENTATION
│   ├── QUICK-START.md ───────────► 5-minute guide to get started
│   ├── README.md ────────────────► Complete documentation
│   ├── CHANGES-SUMMARY.md ───────► What changed from original
│   └── SYSTEM-OVERVIEW.md ───────► This file (architecture)
│
└── 🗂️ LEGACY
    └── index.html ───────────────► Original (kept as backup)
```

## 🔄 Data Flow

### Creating New Quiz
```
1. YOU create/edit JSON file
        │
        ▼
2. Save as my-quiz.json
        │
        ▼
3. Open: quiz-template.html?content=my-quiz.json
        │
        ▼
4. JavaScript fetches & validates JSON
        │
        ▼
5. Quiz loads with your content
        │
        ▼
6. Student uses quiz
        │
        ▼
7. Progress saves to localStorage
```

### Student Progress Flow
```
Student opens quiz
        │
        ▼
Loads from localStorage
(key: QUIZ_{unit}_{version}_progress)
        │
        ▼
Student studies (answers cards)
        │
        ▼
Each answer updates:
  - Box number (1/2/3)
  - Next review date
  - Statistics
        │
        ▼
Saves to localStorage
        │
        ▼
Can export as JSON file
```

## 🧩 Component Breakdown

### quiz-template.html (The Engine)

```
┌─────────────────────────────────────────────────┐
│                 HTML STRUCTURE                   │
│  ┌─────────────────────────────────────────┐   │
│  │ Header (dynamic title/subtitle)         │   │
│  │ Navigation tabs                         │   │
│  │ Main content area (tabs)                │   │
│  │ Footer (dynamic)                        │   │
│  └─────────────────────────────────────────┘   │
│                                                  │
│              JAVASCRIPT MODULES                  │
│  ┌─────────────────────────────────────────┐   │
│  │ 📥 loadContent()                        │   │
│  │    - Fetches JSON                       │   │
│  │    - Validates structure                │   │
│  │    - Populates globals                  │   │
│  │                                          │   │
│  │ 🎴 Flashcard System                     │   │
│  │    - Leitner algorithm                  │   │
│  │    - Card scheduling                    │   │
│  │    - Progress tracking                  │   │
│  │                                          │   │
│  │ 📝 Quiz System                          │   │
│  │    - Distractor generation              │   │
│  │    - Difficulty levels                  │   │
│  │    - Score tracking                     │   │
│  │                                          │   │
│  │ ✓ True/False System                     │   │
│  │    - Random statement selection         │   │
│  │    - Answer validation                  │   │
│  │                                          │   │
│  │ 💾 Storage System                       │   │
│  │    - localStorage read/write            │   │
│  │    - Export/import                      │   │
│  │    - Reset functionality                │   │
│  │                                          │   │
│  │ 📊 Statistics & Dashboard               │   │
│  │    - Progress calculation               │   │
│  │    - Calendar view                      │   │
│  │    - Streak tracking                    │   │
│  └─────────────────────────────────────────┘   │
└─────────────────────────────────────────────────┘
```

### Content JSON Structure

```json
{
  "metadata": {
    // Defines quiz identity and UI text
    "title": "Quiz Title",
    "subtitle": "Topic",
    "description": "Header description",
    "unit": "UNIQUE_ID",     // ← Used for localStorage key
    "version": "v1",         // ← Used for localStorage key
    "footer": "Footer text"
  },
  
  "cards": [
    // Array of flashcards
    {
      "id": 1,               // ← Unique integer
      "tema": "Category",    // ← Groups cards by theme
      "curto": false,        // ← Short/long form indicator
      "q": "Question?",
      "a": "Answer."
    }
  ],
  
  "distractors": {
    // Wrong answers for multiple choice
    "1": [                   // ← String key matches card ID
      "Plausible wrong answer 1",
      "Plausible wrong answer 2",
      "Plausible wrong answer 3"
    ]
  },
  
  "trueFalse": [
    // True/False statements
    {
      "t": "Statement text",
      "v": true,             // ← true or false
      "e": "Explanation"
    }
  ]
}
```

## 🎯 Key Design Decisions

### 1. **URL Parameter Loading**
**Why:** Allows one HTML file to serve all content
```
quiz-template.html?content=file1.json  ← Quiz 1
quiz-template.html?content=file2.json  ← Quiz 2
```

### 2. **Async Content Loading**
**Why:** Clean separation, can load from server later
```javascript
async function loadContent(jsonPath) {
  const response = await fetch(jsonPath);
  const data = await response.json();
  // ... validate and initialize
}
```

### 3. **Dynamic localStorage Keys**
**Why:** Independent progress per quiz
```javascript
const CONTENT_KEY = `QUIZ_${unit}_${version}`;
// Example: QUIZ_U1_v2_progress
```

### 4. **Fallback Distractor Generation**
**Why:** Works even if JSON has few distractors
```javascript
1. Try handcrafted (from JSON)
2. Try same-theme answers (smart)
3. Try any-theme answers (fallback)
```

### 5. **Preserved Original Logic**
**Why:** Proven system, no need to change
- Same Leitner intervals (1/3/7 days)
- Same progress structure
- Same keyboard shortcuts
- Same UI/UX

## 🔐 Security & Limitations

### Current Limitations
- ⚠️ Files must be served from same origin (CORS)
- ⚠️ No server-side validation
- ⚠️ localStorage can be cleared by user
- ⚠️ No user authentication
- ⚠️ Progress is local to browser

### Future Enhancements (Optional)
- 🔮 Server-side storage for progress
- 🔮 User accounts and sync
- 🔮 Content validation service
- 🔮 Quiz editor interface
- 🔮 Analytics dashboard
- 🔮 Collaborative features

## 📱 Compatibility

### Browsers
- ✅ Chrome 60+
- ✅ Firefox 55+
- ✅ Safari 11+
- ✅ Edge 79+

### Features Required
- ✅ ES6 (arrow functions, async/await)
- ✅ Fetch API
- ✅ localStorage
- ✅ CSS Grid & Flexbox
- ✅ CSS Variables

### Mobile
- ✅ Responsive design
- ✅ Touch-friendly
- ✅ Adjusts layout < 768px
- ✅ Works offline (after first load)

## 🚀 Performance

### Load Time
```
1. HTML parse: ~50ms
2. JSON fetch: ~10-100ms (depends on file size)
3. Validation & init: ~20ms
4. Total: < 200ms for typical quiz
```

### Memory Usage
```
- Small quiz (10 cards): ~100KB
- Medium quiz (50 cards): ~300KB
- Large quiz (200 cards): ~1MB
- Very reasonable for modern browsers
```

### localStorage Size
```
- Progress data: ~1KB per 10 cards
- Stats: ~2-5KB
- Well within 5-10MB limit
```

## 🎓 Educational Design

### Learning Science Principles Applied

1. **Spaced Repetition (Leitner)**
   - Box 1: Review tomorrow (new/wrong)
   - Box 2: Review in 3 days (getting it)
   - Box 3: Review in 7 days (mastered)

2. **Active Recall**
   - Question first, answer hidden
   - Forces memory retrieval
   - More effective than passive review

3. **Immediate Feedback**
   - Mark right/wrong instantly
   - See correct answer immediately
   - Reinforces learning

4. **Varied Practice**
   - Flashcards (recall)
   - Multiple choice (recognition)
   - True/False (judgment)

5. **Progress Tracking**
   - Visible mastery percentage
   - Motivates continued study
   - Shows improvement over time

## 💪 Advantages of This Architecture

### For Content Creators
- ✅ No coding needed
- ✅ Simple JSON format
- ✅ Quick iteration
- ✅ Easy to version control
- ✅ Collaborative editing

### For Students
- ✅ Consistent experience
- ✅ Progress always saved
- ✅ Multiple subjects supported
- ✅ Works offline
- ✅ Mobile friendly

### For Developers
- ✅ Clean separation of concerns
- ✅ Easy to maintain
- ✅ Extensible design
- ✅ Well documented
- ✅ Modern JavaScript

### For System
- ✅ Scalable (add unlimited quizzes)
- ✅ Maintainable (fix code once)
- ✅ Testable (validate JSON)
- ✅ Portable (just files, no database)

## 🎨 Customization Points

### Easy (no code changes)
- ✅ Create new content (JSON)
- ✅ Adjust colors (CSS variables)
- ✅ Change text/labels (in JSON)

### Medium (small code edits)
- ⚙️ Adjust review intervals
- ⚙️ Change difficulty formulas
- ⚙️ Add new keyboard shortcuts
- ⚙️ Customize scoring

### Advanced (architecture changes)
- 🔧 Add new quiz modes
- 🔧 Integrate with backend
- 🔧 Add gamification
- 🔧 Multi-user features

---

## 📝 Summary

This is a **content-driven learning system** where:
- **One codebase** (`quiz-template.html`) powers all quizzes
- **Multiple JSON files** provide the content
- **localStorage** tracks individual progress
- **No server required** (static files only)
- **Scales effortlessly** to unlimited subjects

The architecture is **simple, maintainable, and effective** for creating educational flashcard systems! 🎓

