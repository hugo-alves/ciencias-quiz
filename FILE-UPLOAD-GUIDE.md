# 📁 File Upload Feature Guide

## ✨ What's New

You can now **upload JSON quiz files directly** from your computer without needing to push them to GitHub first!

## 🎯 How to Use

### Method 1: Upload from Your Computer

1. Open the launcher: `index-launcher.html`
2. Scroll to "Carregar Ficheiro Personalizado"
3. Click **"📁 Upload JSON File"**
4. Select your JSON file from your computer
5. Click **"▶️ Abrir Quiz Carregado"** when it appears

**That's it!** Your quiz loads instantly.

### Method 2: Use Existing Server Files

1. Open the launcher
2. Type the filename in the text box (e.g., `ciencias-u1-content.json`)
3. Click **"Carregar"**

## 🔍 What Happens Behind the Scenes

- Your uploaded file is **validated** automatically
- It's stored temporarily in **localStorage** (private to your browser)
- You can use it immediately without any GitHub setup
- Your progress is **still saved separately** for each quiz

## 💡 Best Use Cases

**Upload method is perfect for:**
- ✅ Quick testing of new quiz content
- ✅ Trying out quiz ideas before committing
- ✅ Sharing quizzes with others (send them the JSON file)
- ✅ Offline usage (once uploaded, works without internet)

**Server method is better for:**
- ✅ Official, permanent quiz content
- ✅ Sharing via GitHub Pages URLs
- ✅ Content that others should easily access

## 📝 Creating JSON Files

Use the template: `template-empty.json`

```json
{
  "metadata": {
    "title": "My Quiz",
    "subtitle": "Topic",
    "unit": "MY1",
    "version": "v1"
  },
  "cards": [...],
  "distractors": {...},
  "trueFalse": [...]
}
```

See `content-schema.json` for the full schema.

## 🎉 Summary

You now have **TWO ways** to load quizzes:
1. **Upload** (instant, no setup)
2. **Server files** (permanent, shareable)

Both work perfectly! 🚀

