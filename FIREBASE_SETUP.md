# Firebase Leaderboard Setup Guide

## Step 1: Create Firebase Project (5 minutes)

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click **"Add project"** or **"Create a project"**
3. Enter project name: `quiz-epn` (or any name you prefer)
4. Click **Continue**
5. Disable Google Analytics (not needed for leaderboard)
6. Click **Create project**
7. Wait for project creation, then click **Continue**

## Step 2: Register Web App

1. In Firebase Console, click the **Web icon** (`</>`) to add a web app
2. App nickname: `Quiz EPN Web`
3. **Check** "Also set up Firebase Hosting" (optional but recommended)
4. Click **Register app**
5. **Copy the Firebase config** - you'll see something like:

```javascript
const firebaseConfig = {
  apiKey: "AIza...",
  authDomain: "quiz-epn.firebaseapp.com",
  databaseURL: "https://quiz-epn-default-rtdb.firebaseio.com",
  projectId: "quiz-epn",
  storageBucket: "quiz-epn.appspot.com",
  messagingSenderId: "123456789",
  appId: "1:123456789:web:abc123"
};
```

6. **SAVE THIS CONFIG** - you'll need it in Step 4
7. Click **Continue to console**

## Step 3: Enable Realtime Database

1. In the left sidebar, click **Build** → **Realtime Database**
2. Click **Create Database**
3. Select location: **Europe (e.g., `europe-west1`)** (closest to Portugal)
4. Choose **Start in test mode** (we'll add rules in Step 5)
5. Click **Enable**

## Step 4: Add Config to Quiz App

1. Open `firebase-config.js` file in your quiz project (created by this setup)
2. Replace the placeholder config with YOUR config from Step 2
3. Save the file

## Step 5: Set Security Rules

1. In Firebase Console → **Realtime Database** → **Rules** tab
2. Replace the default rules with:

```json
{
  "rules": {
    "leaderboards": {
      "$quizId": {
        ".read": true,
        ".write": true,
        "$scoreId": {
          ".validate": "newData.hasChildren(['name', 'score', 'timestamp', 'quizTitle'])"
        }
      }
    }
  }
}
```

3. Click **Publish**

**What these rules do:**
- Anyone can read leaderboards (public viewing)
- Anyone can write scores (submit after quiz)
- Validates that submissions have required fields
- **Note:** For production, you'd want to add rate limiting and authentication

## Step 6: Test

1. Complete a quiz on your site
2. Enter your name when prompted
3. Check Firebase Console → **Realtime Database** → **Data** tab
4. You should see your score under `leaderboards/[quiz-id]/`

## Free Tier Limits

Firebase Realtime Database free tier includes:
- **1 GB stored**
- **10 GB/month downloaded**
- **100 simultaneous connections**

For a quiz leaderboard, this is **plenty** - you'd need thousands of students before hitting limits.

## Troubleshooting

### "Permission denied" error
- Check that rules are published correctly
- Make sure `databaseURL` in config is correct

### Scores not appearing
- Open browser console (F12) to check for errors
- Verify Firebase config is correct
- Check that database is in Europe region (matches config)

### Want to clear all scores?
- Firebase Console → Realtime Database → Data
- Click the trash icon next to `leaderboards`

## Optional: Add Authentication (Later)

If you want to prevent spam:
1. Enable Firebase Authentication
2. Update security rules to require sign-in
3. Add Google/Email sign-in to quiz

---

**Once you've completed Steps 1-3, let me know and I'll help you add the config to your quiz app!**
