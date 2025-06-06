# 🚀 快速部署指南

## 当前状态 ✅
- ✅ GitHub仓库: https://github.com/linkersea/peptide-research-tools
- ✅ 两个Flask应用已准备就绪

## 一键部署链接

### Railway.app 部署 (推荐)

**肽接枝计算器 (Peptide Grafting Calculator):**
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/linkersea/peptide-research-tools&envs=&envs=&envs=&envs=)

**肽性质预测器 (Peptide Property Predictor):**
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/linkersea/peptide-research-tools&envs=&envs=&envs=&envs=)

## 手动部署步骤

### 1. 访问Railway.app
🔗 https://railway.app

### 2. 登录GitHub账号
点击"Login with GitHub"

### 3. 部署第一个应用 - 肽接枝计算器
- New Project → Deploy from GitHub repo
- 选择 `peptide-research-tools` 仓库
- 设置Root Directory: `peptide-grafting-calculator`
- 点击Deploy

### 4. 部署第二个应用 - 肽性质预测器
- New Project → Deploy from GitHub repo  
- 选择 `peptide-research-tools` 仓库
- 设置Root Directory: `peptide-property-predictor`
- 点击Deploy

## 预期结果

部署成功后，您将获得：

1. **肽接枝时间计算器**
   - URL: `https://[app-name].railway.app`
   - 功能: 实时计算肽接枝时间

2. **肽性质预测器**
   - URL: `https://[app-name].railway.app`
   - 功能: ML驱动的肽性质预测

## 备用部署方案

### Heroku
- 需要信用卡验证
- 每月免费额度较少

### Vercel
- 适合前端应用
- 需要转换为Serverless函数

### PythonAnywhere
- 免费账户有限制
- 适合小型应用

## 技术支持

如遇到部署问题，请检查：
1. GitHub仓库是否为Public
2. requirements.txt是否正确
3. Procfile配置是否正确
4. Railway项目Root Directory设置

---
*部署完成后，请在README.md中更新实际的网站链接* 📝
