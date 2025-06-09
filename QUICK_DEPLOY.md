# 🚀 快速部署指南

## ⚠️ Python 3.12 兼容性说明

**重要更新：** 项目已升级至Python 3.12兼容性，包含以下修复：
- ✅ 解决了 `distutils` 模块在Python 3.12中的兼容性问题
- ✅ 添加了 `SETUPTOOLS_USE_DISTUTILS=stdlib` 环境变量
- ✅ 更新了所有依赖包版本以支持Python 3.12
- ✅ 创建了兼容性层和错误处理机制

## 当前状态 ✅
- ✅ GitHub仓库: https://github.com/linkersea/peptide-research-tools
- ✅ 两个Flask应用已准备就绪
- ✅ Python 3.12兼容性修复完成
- ✅ Railway部署配置优化

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

**1. "ModuleNotFoundError: No module named 'distutils'" 错误：**
- ✅ **已修复**: 更新了依赖版本以兼容Python 3.12
- ✅ **已添加**: nixpacks.toml和runtime.txt文件强制使用Python 3.11
- ✅ **新版本依赖**: numpy 1.26.4, pandas 2.2.2, scikit-learn 1.4.2

**2. "No start command could be found" 错误：**
- ✅ 确保设置了正确的Root Directory
- ✅ 检查对应目录下是否有Procfile、railway.json和start.py文件
- ✅ 尝试手动触发重新部署
- ✅ 如果问题持续，请检查构建日志中的具体错误信息

**解决方案：**
1. 确认Root Directory设置：`peptide-grafting-calculator` 或 `peptide-property-predictor`
2. 确保railway.json中有正确的startCommand
3. 如果仍然失败，可以尝试在Railway设置中手动添加启动命令：`python start.py`

**2. Root Directory设置位置（重要！）：**
- 在Railway项目页面，点击项目名称进入详情页
- 点击 "Settings" 标签页
- 滚动到 "Source Repo" 部分
- 找到 "Root Directory" 字段
- 输入相应的目录名：
  - 对于肽接枝计算器：`peptide-grafting-calculator`
  - 对于肽性质预测器：`peptide-property-predictor`
- 点击保存
- 返回 "Deployments" 标签，点击 "Redeploy" 

**3. 如果部署仍然失败：**
- 检查GitHub仓库是否为Public
- 确认requirements.txt文件存在且正确
- 检查构建日志中的详细错误信息
- 尝试删除项目重新创建
- 联系Railway支持或使用其他部署平台

### 故障排除指导

### 常见问题及解决方案

#### 1. "ModuleNotFoundError: No module named 'distutils'" 错误
**原因：** Python 3.12移除了distutils模块
**解决方案：**
- 项目已包含修复，使用 `SETUPTOOLS_USE_DISTUTILS=stdlib`
- 如仍有问题，在Railway项目设置中添加环境变量：
  - `SETUPTOOLS_USE_DISTUTILS` = `stdlib`

#### 2. 构建失败或依赖安装错误
**解决方案：**
- 检查Python版本是否为3.12
- 确保使用最新的setuptools和wheel版本
- 项目已配置自动安装兼容版本

#### 3. 应用启动失败
**检查步骤：**
1. 查看Railway日志面板
2. 确认环境变量设置正确
3. 验证Root Directory路径设置
4. 检查端口配置（默认使用PORT环境变量）

#### 4. 部署超时
**解决方案：**
- Railway有时需要更长时间构建Python 3.12环境
- 等待3-5分钟，或重新触发部署
- 检查构建日志中的具体错误信息

### 调试技巧

1. **查看详细日志：**
   - 在Railway项目面板点击 "View Logs"
   - 查找具体的错误信息

2. **重新部署：**
   - 点击 "Redeploy" 按钮
   - 或推送新的代码提交触发自动部署

3. **检查配置文件：**
   - `nixpacks.toml` - Python版本和依赖配置
   - `requirements.txt` - Python包版本
   - `start.py` - 启动脚本和错误处理

---
*部署完成后，请在README.md中更新实际的网站链接* 📝
