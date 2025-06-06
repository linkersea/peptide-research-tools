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

**步骤详解：**
1. 点击 "New Project" → "Deploy from GitHub repo"
2. 选择 `peptide-research-tools` 仓库
3. **重要：点击 "Configure" 或 "Settings"**
4. 在 "Source Repo" 部分找到 "Root Directory" 字段
5. 输入：`peptide-grafting-calculator`
6. 保存设置
7. 点击 "Deploy" 或 "Redeploy"

### 4. 部署第二个应用 - 肽性质预测器

**步骤详解：**
1. 再次点击 "New Project" → "Deploy from GitHub repo"  
2. 选择 `peptide-research-tools` 仓库
3. **重要：点击 "Configure" 或 "Settings"**
4. 在 "Source Repo" 部分找到 "Root Directory" 字段
5. 输入：`peptide-property-predictor`
6. 保存设置
7. 点击 "Deploy" 或 "Redeploy"

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

### 常见问题解决

**1. "No start command could be found" 错误：**
- ✅ 确保设置了正确的Root Directory
- ✅ 检查对应目录下是否有Procfile文件
- ✅ 重新部署项目

**2. Root Directory设置位置：**
- 项目创建后，点击项目名称进入详情页
- 点击 "Settings" 标签
- 在 "Source Repo" 部分找到 "Root Directory" 字段
- 输入相应的目录名并保存

**3. 如果部署失败：**
- 检查GitHub仓库是否为Public
- 确认requirements.txt文件存在且正确
- 检查Procfile配置是否正确
- 尝试删除项目重新创建

### 部署检查清单

如遇到部署问题，请检查：
1. ✅ GitHub仓库是否为Public
2. ✅ Root Directory是否正确设置
3. ✅ requirements.txt是否存在
4. ✅ Procfile配置是否正确
5. ✅ railway.json配置是否已提交

---
*部署完成后，请在README.md中更新实际的网站链接* 📝
