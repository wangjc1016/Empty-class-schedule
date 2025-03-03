# 📅 空课表

**空课表** 是一个 Web 应用，用于统计和展示同学们在一周内的空闲课时。项目会从 CSV 文件中读取同学的姓名和 ICS 订阅链接，通过解析 ICS 日历数据，计算每个工作日（周一至周五）各个时段空闲与有课的情况，并以表格形式展示。用户还可以切换不同周次查看课表，并将当前周的数据导出为 Excel 文件。

---

## ✨ 功能特性

- **CSV 导入**：从 CSV 文件中读取同学的姓名及 ICS 订阅链接。
- **ICS 数据解析**：使用 [ical.js](https://github.com/mozilla-comm/ical.js/) 库解析 ICS 日历数据。
- **课表计算**：统计每个工作日（周一至周五）每个时段的空闲和有课信息。
- **进度条提示**：在首次导入时依次请求每位同学的课表数据，并显示实时进度条。
- **周次切换**：支持切换不同周次查看课表数据，切换时直接使用首次请求获得的数据，无需重复请求。
- **Excel 导出**：将当前周的课表数据导出为 Excel 文件，内容包括空闲同学与有课同学（及所上课程）。
- **自定义模态弹窗**：点击表格中对应时段可查看详细的空闲与有课同学信息。
- **Docker 部署**：项目可通过 Docker 容器部署，前后端代码均包含在内，并通过代理解决 ICS 数据跨域问题。

---

## 🚀 项目结构

```
myapp/
├── app.py                     # Flask 后端入口，提供前端页面和 ICS 代理接口
├── requirements.txt           # Python 依赖列表（Flask、flask-cors、requests 等）
├── Dockerfile                 # 构建 Docker 镜像的配置文件
├── docker-compose.yml         # Docker Compose 配置，方便启动容器
├── README.md                  # 本文档
├── CSV_Template.csv           # CSV 模板文件，详见下文说明
├── templates/
│   └── index.html             # 前端页面模板，包含所有前端逻辑和样式
└── static/                    # 静态资源目录（如额外的 CSS、JavaScript 文件等）
```

---

## 🏃 快速开始

你可以直接使用已部署好的链接：[已部署链接地址](http://124.222.16.229:5013/)，但由于链接随时可能失效，且由于跨域问题，获取ICS的过程必须通过服务器代理，所以建议本地部署。

### 1. 本地运行

1. **克隆仓库**

   ```bash
   git clone https://github.com/wangjc1016/Empty-class-schedule
   cd Empty-class-schedule
   ```

2. **安装依赖**

   请确保安装了 Python 3.9 或更高版本，然后运行：

   ```bash
   pip install -r requirements.txt
   ```

3. **启动应用**

   运行 Flask 应用：

   ```bash
   python app.py
   ```

   应用默认监听 `http://0.0.0.0:5013`，在浏览器中访问 [http://localhost:5013/](http://localhost:5013/) 即可查看页面。

### 2. 使用 Docker 部署

1. **构建 Docker 镜像**

   在项目根目录下执行：

   ```bash
   docker-compose build
   ```

2. **启动容器**

   执行：

   ```bash
   docker-compose up
   ```

   应用将运行在 [http://localhost:5013/](http://localhost:5013/)。

---

## 📄 CSV 模板

项目中提供了 `CSV_Template.csv` 文件，请按照以下格式填写同学的姓名和 ICS 订阅链接（以逗号分隔）：

```csv
姓名,ICS链接
张三,https://example.com/zhangsan.ics
李四,https://example.com/lisi.ics
```

**注意：** ICS 链接可以通过“杭电助手”的课表订阅功能获得，具体获取方式可以关注“杭电助手”微信公众号或者联系项目开发者提供指导。🔗

---

## 📝 开源协议

本项目采用 [MIT License](LICENSE) 开源许可证。您可以在遵循许可证条款的前提下自由使用、复制、修改和分发本项目的代码。许可证文件中包含完整的版权和许可信息。

---

## 💡 贡献

欢迎大家提出建议或提交代码改进！如果您发现问题或希望增加新功能，请通过 GitHub 提交 Issue 或 Pull Request。🙏

---

## 📞 联系方式

如有任何疑问，请联系项目维护者：2955647536@qq.com

