# 部署指南 (Deployment Guide)

## 🚀 推荐部署方案

### 方案1: Railway.app (最推荐)

**优势:**
- ✅ 每月$5免费额度，低流量网站可用数月
- ✅ 支持Python Flask应用
- ✅ 自动SSL证书和域名
- ✅ GitHub集成，自动部署

**部署步骤:**

1. **准备GitHub仓库**
   ```bash
   cd peptide-research-tools
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin [YOUR_GITHUB_REPO_URL]
   git push -u origin main
   ```

2. **部署肽接枝计算器**
   - 访问 https://railway.app
   - 选择 "Deploy from GitHub repo"
   - 设置根目录为 `peptide-grafting-calculator`
   - Railway自动检测Flask应用并部署

3. **部署肽性质预测器**
   - 创建新项目
   - 同样选择GitHub仓库
   - 设置根目录为 `peptide-property-predictor`
   - 自动部署

### 方案2: Vercel (适合静态部署)

**适用场景:** 如果转换为静态站点或Serverless函数

```bash
# 安装Vercel CLI
npm i -g vercel

# 部署
cd peptide-grafting-calculator
vercel
```

### 方案3: PythonAnywhere

**优势:** 专为Python设计，$5/月或免费版

1. 上传文件到PythonAnywhere
2. 配置Web应用指向app.py
3. 设置虚拟环境和依赖

## 🔧 本地开发测试

### 肽接枝计算器测试
```bash
cd peptide-grafting-calculator
pip install -r requirements.txt
python app.py
# 访问 http://localhost:5000
```

### 肽性质预测器测试
```bash
cd peptide-property-predictor  
pip install -r requirements.txt
python app.py
# 访问 http://localhost:5000
```

### 可视化工具测试
```bash
cd visualization-tools
pip install -r requirements.txt
python selected_visualizations.py
# 检查 outputs/ 目录中的生成图片
```

## 📊 预期访问地址

部署成功后的访问地址示例:

- **Railway**: 
  - 计算器: `https://peptide-grafting-calc-production.railway.app`
  - 预测器: `https://peptide-property-pred-production.railway.app`

- **Vercel**:
  - 计算器: `https://peptide-grafting-calculator.vercel.app`
  - 预测器: `https://peptide-property-predictor.vercel.app`

## 🔍 部署检查清单

### 部署前检查:
- [ ] 所有requirements.txt文件完整
- [ ] Procfile配置正确
- [ ] 模型文件(.pkl)已包含
- [ ] 数据文件(.xlsx)已包含
- [ ] 环境变量PORT已配置

### 部署后验证:
- [ ] 网站可正常访问
- [ ] 计算功能正常工作
- [ ] 预测功能返回结果
- [ ] 可视化图片生成正常
- [ ] 响应时间合理(<5秒)

## 🛠️ 故障排除

### 常见问题:

1. **模型文件找不到**
   - 检查models/目录结构
   - 确认.pkl文件已上传

2. **依赖包安装失败**
   - 检查requirements.txt格式
   - 确认版本兼容性

3. **内存不足**
   - 考虑优化模型大小
   - 使用更高配置的部署方案

4. **端口配置错误**
   - 确认Procfile配置
   - 检查PORT环境变量

## 💰 成本估算

### Railway.app:
- **免费额度**: $5/月
- **预估使用**: 低流量学术网站可用3-6个月
- **超出后**: 按使用量付费

### Vercel:
- **免费版**: 充足的功能限制内使用
- **付费版**: $20/月起

### PythonAnywhere:
- **免费版**: 基础功能
- **付费版**: $5/月起

## 📈 性能优化建议

1. **代码优化**
   - 缓存预加载的模型
   - 优化数据处理流程

2. **资源优化**
   - 压缩静态文件
   - 使用CDN加速

3. **监控设置**
   - 添加错误日志
   - 设置性能监控

---

**推荐部署顺序:**
1. 先部署肽接枝计算器（较简单）
2. 再部署肽性质预测器（包含ML模型）
3. 测试两个应用的功能
4. 优化性能和用户体验
