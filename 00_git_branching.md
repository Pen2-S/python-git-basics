# TASK 0: Git Branching & Pull Requests 🌱

Goal:

- Learn how to work with branches
- Understand why we don’t work directly on `main`
- Create a Pull Request (PR) like in real projects

This task is about **Git only**, no Python code yet.

---

## 🧠 Important Concept

- `main` is the **stable branch**
- All work should be done in a **separate branch**
- Changes are merged into `main` via **Pull Requests**

Think of it like this:

```
> main = production
> development = your workspace
```

---

## 🛠 Step-by-step Instructions

### 1️⃣ Check your current branch

```bash
git branch
```

You should see something like:

```
* main
```

The `*` shows the current branch.

---

### 2️⃣ Create a new branch called `development`

```bash
git branch development
```

---

### 3️⃣ Switch to the new branch

```bash
git checkout development
```

(or the shortcut - immediately create and switch)

```bash
git checkout -b development
```

Check again:

```bash
git branch
```

You should now see:

```
* development
  main
```

✅ You are now working on `development`

---

## 🚀 Rule from now on

❌ Do NOT code on `main`

✅ Do ALL tasks on `development`

Every Python task you complete should be:

1. Done on `development`
2. Committed
3. Pushed
4. Merged into `main` via a Pull Request

---

## 📦 First Commit (Git Practice)

Even without code changes, make a first commit:

```bash
git status
git add .
git commit -m "Create development branch and start workflow"
```

---

## ☁️ Push the branch to GitHub

```bash
git push -u origin development
```

Now GitHub knows about your branch.

---

## 🔁 Create a Pull Request (PR)

1. Go to your GitHub repository
2. You should see a message:

   > "Compare & pull request"

3. Click it
4. Base branch: `main`
5. Compare branch: `development`
6. Title:

   ```
   Initial project setup
   ```

7. Description:

   ```
   Created development branch and started proper Git workflow.
   ```

8. Click **Create Pull Request**
9. Merge the PR into `main`

🎉 Congratulations — this is **real-world Git workflow**

---

## 🔄 Repeat This Flow for Every Task

For each new task:

1. Work on `development`
2. Commit changes (commit messages like `TASK X: <short description>`)
3. Push `development`
4. Open a PR with:
   - Base: `main`
   - Compare: `development`
   - Title: `TASK X: <short description>`
   - Description: `Detailed description of changes`
5. Send for review
6. Merge into `main`

---

## 🧪 Optional Challenge

- Create another branch:

  ```bash
  git checkout -b experiment
  ```

- Make a change
- Delete the branch:

  ```bash
  git branch -d experiment
  ```

---

## 🎯 What You Learned

✅ Branches
✅ Switching branches
✅ Pushing branches
✅ Pull Requests
✅ Professional Git workflow

This is how **real teams work**.
