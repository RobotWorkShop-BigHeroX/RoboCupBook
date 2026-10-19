# RoboCup HSL 新人入门手册与知识图谱

**A Comprehensive Onboarding Handbook & Engineering Roadmap for RoboCup Humanoid Soccer League (HSL)**

湖南大学 Robot 工作坊 · BigHeroX 战队

[最新发布版本 (v1.2.0)](https://github.com/RobotWorkShop-BigHeroX/RoboCupBook/releases) · [在线阅读站点](https://robotworkshop-bigherox.github.io/RoboCupBook/) · [下载标准 PDF (v1.2.0)](RoboCup_HSL_Handbook_v1.2.0.pdf) · [MIT 开源许可证](LICENSE)

---

## 项目定位与说明

本项目建设一套面向完全不了解 RoboCup（机器人世界杯）及 HSL（Humanoid Soccer League，人形机器人足球联赛）的新成员的入门知识体系。

读者可能没有参加过 RoboCup，不了解人形机器人足球比赛，也可能没有深入使用过 ROS 2、Git 或机器人感知与控制算法。手册帮助读者建立清晰的工程认识与开发方法：

1. **RoboCup 与 HSL 基本情况**：赛事演进历史、合并重组脉络、核心规则与裁判盒（GameController）机制。
2. **本队使用的技术与平台**：T4 机器人硬件参数、核心器件（IMU、足式里程计）、中联重科（Zvalley）开源生态及本队历年公开技术成果（TDP、资格赛视频）。
3. **技术进阶递进路线**：从 Git、ROS 2、Linux 工具，到 YOLO 视觉、行为树/状态机决策、粒子滤波全局定位，直至前沿深度强化学习。
4. **权威一手信息渠道**：赛事官方站点、Rules 仓库、必订邮件列表与 Discord 核心开发者社区。
5. **实验室操作安全守则**：吊机悬挂要求、防空转自锁规范、三人协作测试制、“进阻尼”操作记忆与复位流程。

---

## 手册目录全景导航

手册包含 7 个核心技术章节与 6 个参考附录，正文与标准 PDF（v1.2.0）保持内容同步。

| 章节模块                                     | 核心内容概述                                                                                                                           |           在线查阅链接           |
| :------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------: |
| **01. RoboCup 与 HSL**                 | 赛事目标、组别收敛脉络、一场比赛全流程、场地元素影响、写代码相关的六条规则、裁判盒联调                                                 |   [查阅章节](docs/01-robocup.md)   |
| **02. 强队与开源资产**                 | 八支国际队伍技术特色、B-Human 五层软件架构解剖、阅读陌生代码仓库四步法、TDP 阅读策略                                                   |    [查阅章节](docs/02-teams.md)    |
| **03. 机器人平台：T4 与 Zvalley 生态** | T4 平台参数与实测、单腿关节自由度分配、IMU 姿态估计与排坑、足式里程计误差、机载软件频率、电气接口与 Zvalley 生态                       |  [查阅章节](docs/03-platform.md)  |
| **04. 学习路线与开发基础**             | Git 团队协作约定、ROS 2 核心机制与时延分析、Linux 现场排查命令、视觉检测流程与排坑、行为树与状态机分工、粒子滤波定位、深度强化学习范围 |  [查阅章节](docs/04-learning.md)  |
| **05. 消息渠道**                       | 必订官方邮件列表与 Discord 核心社区、官方网站信息地图、代码与工具仓库、赛季时间节奏、队内信息维护流程                                  |  [查阅章节](docs/05-channels.md)  |
| **06. 实验室安全守则**                 | 上电前六项口头确认检查、保护吊架调节规范、三人协作测试分工、进阻尼与拍急停边界、三类常见危险状态、跌倒处理与上下电顺序                 |   [查阅章节](docs/06-safety.md)   |
| **07. 第一次参赛：从报名到上场**       | 资格审查与报名材料准备、出发前设备工具打包清单、抵达赛场后四项核验、比赛日全天流程安排、现场参数变更冻结纪律、赛后结构化复盘模板       | [查阅章节](docs/07-competition.md) |
| **全球队伍：参赛队伍汇总档案**         | Small、Middle 与 Large/AdultSize 组别各队伍 Video、TDP、Robots、Software 资产及开源主页                                                |   [查阅档案](docs/teams-list.md)   |
| **附录 A–F：参考手册与速查**          | 常用技术术语表、新成员 90 天培养计划、常见运行故障排查速查表、待补事实核实清单、队内口头黑话对照表、官方与经典文献延伸阅读             |  [查阅章节](docs/08-appendix.md)  |

---

## 私有仓库与敏感资料说明（Submodule）

本项目采用公开与私有分层管理结构：

- **公开资料（`public-resource/`）**：存放本队公开 TDP 报告、比赛视频与硬件参数表。
- **私有资料（`Zvalley-resource/`）**：以 **Git Submodule** 形式独立接入内部私有仓库 [`RobotWorkShop-BigHeroX/robocup-zvalley-resource`](https://github.com/RobotWorkShop-BigHeroX/robocup-zvalley-resource)，托管 T4 机器人内部硬件手册与未公开技术资产。

### 克隆与拉取完整仓库

若已获得战队内部授权，请在克隆主仓库时加入 `--recurse-submodules` 参数：

```bash
# 完整递归克隆（包含私有子模块）
git clone --recurse-submodules https://github.com/RobotWorkShop-BigHeroX/RoboCupBook.git

# 若之前已单独克隆，可通过如下命令初始化拉取子模块
git submodule update --init --recursive
```

---

## 本地编译与构建标准 PDF

本项目参考国际官方 [RoboCup HSL Rules.tex](https://github.com/RoboCup-HumanoidSoccerLeague/HSL-Rules/blob/main/Rules.tex) 设计了 LaTeX 排版工程。

### 1. 环境准备

- **Python 环境**：推荐使用包管理工具 [uv](https://github.com/astral-sh/uv)。
- **LaTeX 编译环境**：安装 [MiKTeX](https://miktex.org/) 或 [TeX Live](https://www.tug.org/texlive/)（需包含 `xelatex` 引擎）。

### 2. 一键编译 PDF

通过项目内置的自动化构建脚本即可完成检测与双遍编译：

```bash
# 通过 uv 直接运行构建脚本
uv run python scripts/build_pdf.py

# 编译完成后清理中间辅助文件
uv run python scripts/build_pdf.py --clean
```

编译成功后，将在项目根目录下生成最新版的标准手册：`RoboCup_HSL_Handbook_v1.2.0.pdf`。

---

## 作者与贡献者

- **编著者（Author）**：**hongli** ([2868014836@qq.com](mailto:2868014836@qq.com))
- **贡献者（Contributor）**：**hanxu chen**
- **所属战队与机构**：
  - [湖南大学 Robot 工作坊](https://github.com/RobotWorkShop-BigHeroX)
  - **BigHeroX 战队**

---

## 开源许可证

本项目文档与代码采用 [MIT License](LICENSE) 授权开源。
