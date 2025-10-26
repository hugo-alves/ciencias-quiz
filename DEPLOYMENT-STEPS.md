# 🚀 Deploy to GitHub Pages - Step by Step

## What You Need to Do Right Now

### Step 1: Enable GitHub Pages
1. Go to: https://github.com/hugo-alves/ciencias-quiz
2. Click **Settings** (top menu)
3. Click **Pages** (left sidebar)
4. Under "Source":
   - Select **Deploy from a branch**
   - Branch: **main**
   - Folder: **/ (root)**
5. Click **Save**

**⏱️ Wait 1-2 minutes** for GitHub to deploy

### Step 2: Test Your Quiz
Open in your browser:
```
https://hugo-alves.github.io/ciencias-quiz/index-launcher.html
```

## That's It! 🎉

Once enabled, your quiz works just like before, but now it:
- ✅ Loads JSON files dynamically
- ✅ Supports multiple quizzes in one system
- ✅ Easy to add new content (just create new JSON files)

## Quick Links After Setup

- **Launcher:** https://hugo-alves.github.io/ciencias-quiz/index-launcher.html
- **Natural Science:** https://hugo-alves.github.io/ciencias-quiz/quiz-template.html?content=ciencias-u1-content.json
- **History Example:** https://hugo-alves.github.io/ciencias-quiz/quiz-template.html?content=example-historia.json

## Adding New Quizzes

1. Create a new JSON file (copy from `template-empty.json`)
2. Commit and push to GitHub
3. GitHub Pages auto-updates!
4. Access: `quiz-template.html?content=your-file.json`

```bash
git add your-new-quiz.json
git commit -m "Add new quiz"
git push origin main
```

