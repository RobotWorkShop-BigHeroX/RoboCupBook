# 1.2 RoboCup的历史强队

> **新成员阅读导引**  
> 在机器人世界杯中，不要闭门造车，站在世界顶级队伍的肩膀上是快速入门与技术突破的关键路径。本篇系统归纳了合并后目前 Humanoid Soccer League（包括 Large / Middle / Small 及并入的 SPL 历史传奇）的全球标杆强队，附带其核心开源代码库、技术文档体系与历史战绩。

---

## 1 全球历史强队总览

| 队伍名称 | 所属高校/科研机构 | 国家/地区 | 参赛组别/历史背景 | 核心开源仓库 / 技术文档 | 历史战绩与技术特长 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **B-Human** | 不来梅大学 / 德国人工智能研究中心 (DFKI) | 德国 | SPL 霸主 / HSL 核心基石 | [CodeRelease](https://github.com/bhuman/BHumanCodeRelease) / [Docs](https://docs.b-human.de/coderelease2026/) | 10+ 次世界冠军；全球代码质量最高；模块化框架、卡尔曼滤波、快速视觉、踢球动作生成 |
| **Rhoban FC** | 波尔多大学 (Univ. of Bordeaux) / CNRS | 法国 | KidSize / 综合强队 | [Rhoban/RhobanHardware](https://github.com/Rhoban) / [Docs](https://rhoban.com/) | 4次世界冠军；以样条曲线步态规划、逆运动学（IK）、Cartesian 控制与稳健鲁棒性著称 |
| **NimbRo** | 波恩大学 (Univ. of Bonn) | 德国 | AdultSize / TeenSize 霸主 | [NimbRo-OP-ROS](https://github.com/AIS-Bonn/nimbro_robotics) | 多届成人组/青少年组世界冠军；3D 打印人形构型、全自主全身动平衡、复杂姿态恢复 |
| **CIT Brains** | 千叶工业大学 (Chiba Inst. of Tech.) | 日本 | KidSize / 资深强队 | [citbrains](https://github.com/citbrains) | 多届冠亚军；极具工程耐操度的高精度动力学模型、高刚度关节控制、快速直塞射门 |
| **Hephaestus** | 清华大学 (Tsinghua University) | 中国 | KidSize / AdultSize | [TDP 归档文档](https://hsl.robocup.org/qualified-teams/) | 国内顶尖强队，多次杀入全球四强；高精位姿估计、视觉网络轻量化部署、强鲁棒性防跌倒 |
| **Mountain Sea** | 中国农业大学 (CAU) | 中国 | KidSize / 成人组 | [CAU_Mountain_Sea TDP](https://hsl.robocup.org/qualified-teams/) | 长期征战 RoboCup 的资深队伍；精细化步态规划、多传感器信息融合感知 |
| **RoMeLa** | 加州大学洛杉矶分校 (UCLA) | 美国 | AdultSize / 硬件先驱 | [RoMeLa UCLA](https://www.romela.org/) | 创造了著名的 DARwIn-OP 开源平台与 ARTEMIS 高动态本体激振控制算法 |
| **HERoEHS** | 汉阳大学 (Hanyang University) | 韩国 | AdultSize | [HERoEHS TDP](https://hsl.robocup.org/qualified-teams/) | 亚太地区资深大组强队，在结构轻量化与机械安全性上具备成熟规范 |

---

## 2 标杆队伍重点分析与代码参考

### 2.1 B-Human（德国不来梅大学 · 世界标杆）
B-Human 是全球机器人足球界最负盛名的常胜之师，每年他们都会在赛事结束后向全球开源其整套参赛系统代码并配有极尽详实的技术报告（Code Release Report）。

```
B-Human 软件系统分层结构：
┌────────────────────────────────────────────────────────┐
│   Behavior Control（行为控制：基于 CABSL 层次状态机）     │
├────────────────────────────────────────────────────────┤
│   Modeling（环境建模：球滤波、自定位、障碍物栅格、队伍世界模型） │
├────────────────────────────────────────────────────────┤
│   Perception（感知：快速图像扫描线、YOLO目标检测、线特征提取）│
├────────────────────────────────────────────────────────┤
│   Motion Control（运动控制：行走步态规划、逆运动学、动量补偿）  │
├────────────────────────────────────────────────────────┤
│   Hardware Layer（底层硬件适配与总线通信）                │
└────────────────────────────────────────────────────────┘
```

- **官方技术文档**：[https://docs.b-human.de/coderelease2026/](https://docs.b-human.de/coderelease2026/)
- **GitHub 开源代码**：[https://github.com/bhuman/BHumanCodeRelease](https://github.com/bhuman/BHumanCodeRelease)
- **环境搭建与初学教程**：[https://docs.b-human.de/coderelease2026/getting-started/initial-setup/](https://docs.b-human.de/coderelease2026/getting-started/initial-setup/)
- **借鉴重点**：
  - 学习其高度解耦的**Blackboard（黑板机制）**与流水线数据交换。
  - 学习其基于样条插值的摆动腿轨迹生成与压力中心（CoP）闭环平衡。
  - 学习其如何将自定位（Self-Localization）与多机通信共享信息相融合。

---

### 2.2 Rhoban Football Club（法国波尔多大学）
Rhoban 团队以深厚的应用数学与动力学控制功底闻名。对于想要深入步态与全身控制的队员，Rhoban 是绝佳的教材。

- **代码架构特点**：
  - **IKWalk 步态引擎**：基于逆运动学解析解的快速参数化步态发生器。
  - **Spline 样条控制**：将复杂的踢球、起伏、扑救动作参数化为 3 阶或 5 阶多项式曲线。
  - **鲁棒防跌倒**：利用机载 IMU 的角加速度差分迅速计算恢复力矩。
- **仓库参考**：[Rhoban Team GitHub](https://github.com/Rhoban)

---

### 2.3 国内重点队伍（清华 Hephaestus 与中国农大 Mountain Sea）
作为本队国内交流与竞技的主要标杆，这两支队伍在适应实际场地光照变化、强化学习步态在国产人形硬件上的落地调优方面积累了丰富的一手经验。
- 详情可参考本项目内归档的 [CAU_Mountain_Sea-tdp-67d3896715fb9.pdf](file:///f:/RoboCupBook/public-resource/othersTDP/CAU_Mountain_Sea-tdp-67d3896715fb9.pdf) 和 [Tsinghua_Hephaestus-tdp-6788f534a4752.pdf](file:///f:/RoboCupBook/public-resource/othersTDP/Tsinghua_Hephaestus-tdp-6788f534a4752.pdf)。

---

## 3 新人如何阅读与消化开源代码

1. **先读 TDP，再看代码**：各队伍的 TDP（Team Description Paper）相当于系统架构说明书，阅读 10 页的论文能为你建立全局观，避免一头扎进数十万行 C++ 代码的细节泥潭中。
2. **重点分析状态机与接口协议**：先弄懂感知模块输出给决策模块的格式（通常为球的局部坐标 $(x,y)$ 与置信度），以及决策输出给运动控制的期望速度向量 $(v_x, v_y, \omega_z)$。
3. **利用仿真回放数据学习**：B-Human 与 Rhoban 均支持将真实比赛记录的 Log 文件在电脑上回放模拟（SimRobot），这是无需实体机器人也能调试算法的最佳工具。
