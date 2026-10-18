# 4 消息渠道

> **新成员须知**  
> RoboCup HSL 是一个处于高度活跃演进中的国际前沿科技竞赛，官方每年都会对规则细节、传感器限制、尺寸比例和裁判系统进行调整。部分开源工具链迭代非常频繁，保持与国际组委会信息同步至关重要。

---

## 4.1 官方核心站点与赛事入口

1. **HSL 联赛官方主站**：[https://hsl.robocup.org/](https://hsl.robocup.org/)  
   联赛最高权威站点，发布年度赛程安排、组别细则、技术挑战赛（Technical Challenge）主题与合格队伍名单。
2. **RoboCup 年度世界赛主站**：`https://202x.robocup.org/`（如 `https://2026.robocup.org/`）  
   由当届主办国（如法国、荷兰、巴西、中国等）搭建的现场赛务平台，提供比赛场馆、草皮测试批次、注册签到与现场网络配置规范。
3. **新参赛队指南（Information for New Teams）**：[https://hsl.robocup.org/information-for-new-teams/](https://hsl.robocup.org/information-for-new-teams/)  
   专为新成立战队准备的参赛指南，涵盖资格申请流程、TDP 编写规范及现场准备事项。
4. **全球入选队伍资料汇总（Qualified Teams）**：[https://hsl.robocup.org/qualified-teams/](https://hsl.robocup.org/qualified-teams/)  
   全球所有审核通过队伍的 TDP 论文、硬件配置规格与参赛展示视频的官方集中库，是进行对手技术调研的第一手富矿。

---

## 4.2 规则与官方开源工具库

1. **HSL 规则开源代码库**：[RoboCup-HumanoidSoccerLeague/HSL-Rules](https://github.com/RoboCup-HumanoidSoccerLeague/HSL-Rules)  
   官方规则以 LaTeX 格式在 GitHub 上协作维护，所有规则修订的 Pull Request 和 Issue 讨论均对外公开透明。
2. **2026 规则中文解析文档**：[飞书知识库规则整理](https://hcnwvqtaepc6.feishu.cn/wiki/PHPCwZCI8iPhDhksyzNcBFKRnlh)  
   由本队核心成员整理的中文核心赛制速查手册。
3. **官方裁判盒系统（GameController）**：[RoboCup-HumanoidSoccerLeague/GameController](https://github.com/RoboCup-HumanoidSoccerLeague/GameController)  
   用 Java / C++ 编写的中央裁判端，支持本地模拟比赛广播协议包。
4. **机器人合规检查工具（RobotInspection）**：[RoboCup-HumanoidSoccerLeague/RobotInspection](https://github.com/RoboCup-HumanoidSoccerLeague/RobotInspection)  
   在进入赛场前，官方裁判会使用专门的量具和检测软件对机器人的物理尺寸、重心、双足投影比例及足底压强进行严苛检录。
5. **官方机器人支持项目**：[https://robotprogram.robocup.org/](https://robotprogram.robocup.org/)  
   RoboCup 联合各大机器人赞助商提供的硬件样机资助与学术支持计划。

---

## 4.3 核心实时公告渠道（必须加入）

> [!IMPORTANT]
> 错过关键公告可能导致队伍无法通过资格审查甚至丧失参赛权！每位战队核心研发成员必须完成以下两项入驻：

### 1. 官方邮件列表（Mailing List · 必须订阅）
- **订阅地址**：[https://lists.robocup.org/mm/lists/robocup-humanoid.lists.robocup.org/](https://lists.robocup.org/mm/lists/robocup-humanoid.lists.robocup.org/)
- **说明**：这是国际技术委员会（TC）与组织委员会（OC）发布规则修改投票、资格申请截止通知、重要 Q&A 裁决的**唯一官方法定通知渠道**。订阅后请务必注意查收来自 `robocup-humanoid` 域名的邮件。

### 2. 官方 Discord 技术交流社群（必须进群）
- **邀请链接**：[https://discord.gg/67qGN8ycwz](https://discord.gg/67qGN8ycwz)
- **说明**：聚集了全球所有参赛高校的技术队长（Team Leader）、主裁判与核心开发者。在赛前沟通交流、现场网络排障、规则边界咨询或约战友谊训练赛时，Discord 是响应最迅速的直接渠道。
