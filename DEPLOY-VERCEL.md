# Deploy to Vercel – Step-by-step guide

Get your portfolio live on Vercel and connect your custom domain.

---

## Prerequisites

- A [Vercel account](https://vercel.com/signup) (free; sign up with GitHub, GitLab, Bitbucket, or email).
- Your project folder (this repo) with `index.html`, `auth-check.js`, `assets/`, etc.

---

## Option A: Deploy with Vercel CLI (fastest)

### Step 1: Install Vercel CLI

```bash
npm i -g vercel
```

(Or use `npx vercel` in the project folder without installing globally.)

### Step 2: Log in

```bash
vercel login
```

Follow the prompts (email or GitHub/GitLab/Bitbucket).

### Step 3: Deploy from your project folder

```bash
cd /path/to/sangster
vercel
```

- **Set up and deploy?** → **Y**
- **Which scope?** → Your account (Enter).
- **Link to existing project?** → **N**
- **Project name?** → `sangster` (or whatever you like).
- **In which directory is your code?** → **./** (Enter).

Vercel will build and give you a URL like:

`https://sangster-xxxx.vercel.app`

### Step 4: Production deploy

```bash
vercel --prod
```

Your site is now live at the production URL.

---

## Option B: Deploy with GitHub (recommended for updates)

### Step 1: Put the project on GitHub

1. Create a new repo at [github.com/new](https://github.com/new) (e.g. `sangster`).
2. In your project folder:

```bash
cd /path/to/sangster
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/sangster.git
git push -u origin main
```

(Replace `YOUR_USERNAME` with your GitHub username.)

### Step 2: Import the project in Vercel

1. Go to [vercel.com/new](https://vercel.com/new).
2. Click **Import Git Repository** and select your `sangster` repo (or **Import** if it’s the first time).
3. **Configure Project:**
   - **Framework Preset:** Other (or leave as detected).
   - **Root Directory:** leave as `.` (or the folder that contains `index.html`).
   - **Build Command:** leave empty (static site).
   - **Output Directory:** leave as `.` or leave empty.
   - **Install Command:** leave empty.
4. Click **Deploy**.

### Step 3: Wait for the deploy

Vercel will build and assign a URL like `https://sangster-xxxx.vercel.app`. From now on, every push to `main` will trigger a new deploy.

---

## Add your custom domain

### Step 1: Open domain settings

1. In [Vercel Dashboard](https://vercel.com/dashboard), open your project.
2. Go to **Settings → Domains**.

### Step 2: Add the domain

1. Enter your domain (e.g. `sangster.com` or `www.sangster.com`).
2. Click **Add**.

### Step 3: Configure DNS at your registrar

Vercel will show the records you need. Typical setup:

**For root domain (e.g. sangster.com):**

- Type: **A**
- Name: **@**
- Value: **76.76.21.21**

**For www (e.g. www.sangster.com):**

- Type: **CNAME**
- Name: **www**
- Value: **cname.vercel-dns.com**

(If Vercel shows different values, use those.)

Add these at the place where you manage DNS (e.g. Namecheap, GoDaddy, Cloudflare, your registrar’s DNS).

### Step 4: Wait for DNS and SSL

- DNS can take from a few minutes up to 48 hours.
- Vercel will issue a free SSL certificate automatically; HTTPS will work once the domain is verified.

---

## Checklist after deploy

- [ ] Open your Vercel URL (or custom domain) and confirm the **Ahoy** page loads.
- [ ] Enter password **hello-there** and confirm **Let's go!** appears and you can open About.
- [ ] Click through a few pages (Projects, Design Details, Thanks) and check images/videos.
- [ ] Try opening another page in an incognito window (no password) and confirm you’re redirected to the password page.

---

## Updating the site

- **CLI:** Run `vercel --prod` again from the project folder.
- **Git:** Push to `main`; Vercel will auto-deploy.

---

## Optional: vercel.json

A `vercel.json` in the project root can be used later for redirects or headers. The repo includes an empty one; you can leave it as is. Your `.html` files will be served as-is without any extra config.
