# 🚀 Deployment Guide

## 🌐 GitHub Pages (Recommended)

Your quiz system works perfectly on GitHub Pages! Here's how to deploy:

### Step 1: Push to GitHub
```bash
git add .
git commit -m "Update quiz content"
git push origin main
```

### Step 2: Enable GitHub Pages
1. Go to your repo: https://github.com/hugo-alves/ciencias-quiz
2. Click **Settings** → **Pages**
3. Select source: **Deploy from a branch**
4. Branch: **main**
5. Folder: **/ (root)**
6. Click **Save**

### Step 3: Access Your Quiz
Your quizzes will be available at:
- Launcher: `https://hugo-alves.github.io/ciencias-quiz/index-launcher.html`
- Natural Science: `https://hugo-alves.github.io/ciencias-quiz/quiz-template.html?content=ciencias-u1-content.json`

✨ **That's it!** The JSON files load via `fetch()` which works perfectly on GitHub Pages.

---

## 💻 Local Development

Open the launcher locally:
```bash
open index-launcher.html
```

**Note:** For local development, you need a web server to avoid CORS errors:
```bash
python3 -m http.server 8000
# Then open: http://localhost:8000/index-launcher.html
```

---

## 📝 Create New Quiz (3 Steps)

1. Copy template: `cp template-empty.json my-quiz.json`
2. Edit with your content
3. Test locally or push to GitHub Pages

---

## 📚 Documentation

- Complete Guide: `README.md`
- Quick Start: `QUICK-START.md`
- Workflows: `WORKFLOW.md`

## 🎉 You're All Set!

Start creating quizzes! 🚀
