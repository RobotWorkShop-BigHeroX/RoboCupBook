# 5 消息渠道

规则修订、赛程调整和报名通知分散在多个官方渠道。建议将以下入口加入队内资料库，并指定专人定期检查。

## 5.1 优先关注的两个渠道

1. **官方邮件列表**  
   技术委员会（TC）与执行委员会（EC）通常通过邮件列表发布规则修订征集、报名资格审查通知与技术决议。
   - 订阅地址：[robocup-humanoid 邮件列表](https://lists.robocup.org/mm/lists/robocup-humanoid.lists.robocup.org/)
   - 建议使用队内公共邮箱统一订阅，避免因个人毕业离队造成信息断档。
2. **官方 Discord 核心社区**  
   技术委员会、裁判组与全球参赛队日常技术交流与答疑平台。现场比赛期间常用于发布临时网络调整与规则解释。
   - 加入链接：[RoboCup HSL Discord 邀请链接](https://discord.gg/67qGN8ycwz)
   - 提问前先检索频道历史消息，咨询技术问题时附上复现步骤、日志信息与软件环境。

## 5.2 官方信息入口

| 站点地址 | 主要功能 | 查阅频度 |
| :--- | :--- | :--- |
| [hsl.robocup.org](https://hsl.robocup.org/) | 人形足球联赛官网：赛程规划、组别划分、技术挑战说明与入选名单公布 | 每月查阅 |
| `202x.robocup.org` | 当届世界总决赛主办方官网：场地场馆、注册缴费、赛场网络与草皮规格 | 赛前每周核验 |
| [/information-for-new-teams](https://hsl.robocup.org/information-for-new-teams/) | 新参赛队指南：资格申请流程、TDP 编写规范与现场准备指引 | 准备报名前查阅 |
| [/qualified-teams](https://hsl.robocup.org/qualified-teams/) | 参赛队公开材料库：全球入选队伍的 TDP、实战展示视频与硬件配置表 | 备赛必读 |
| [robotprogram.robocup.org](https://robotprogram.robocup.org/) | 官方人形机器人支持项目：硬件平台技术支持与样机支持计划 | 评估换代平台时 |

## 5.3 代码与工具仓库

| 仓库名称 | 适用场景 |
| :--- | :--- |
| [HSL-Rules](https://github.com/RoboCup-HumanoidSoccerLeague/HSL-Rules) | 官方规则 LaTeX 源码与发布版 PDF；查阅条款修订历史与具体年份变更记录 |
| [GameController](https://github.com/RoboCup-HumanoidSoccerLeague/GameController) | 裁判盒官方软件源码与二进制运行包；本地联调与验证网络数据包字段结构 |
| [RobotInspection](https://github.com/RoboCup-HumanoidSoccerLeague/RobotInspection) | 机器人赛前检录规范与计算检查工具；提前核验身高、体重与足底面积参数 |

核对规则时，应确认查阅的 Rules.pdf 与仓库源文件对应的 release 标签或 commit 哈希，避免使用过时草案。

## 5.4 一个赛季的节奏

| 阶段 | 核心任务 |
| :--- | :--- |
| **赛后复盘与冬训期** | 全面复盘当季比赛暴露的技术缺陷，确定下一赛季架构改动，整理交接文档 |
| **年初准备期** | 关注官方网站发布的报名通知与资格审查细则，组织撰写并完善 TDP 技术报告 |
| **春季资格审查期** | 提交 TDP、录制并剪辑资格展示视频；按新赛季规则修订软件逻辑并完成自检 |
| **赛前两个月集成期** | 开展整机系统联调，全流程模拟赛场真实对抗；演练裁判盒网络通信与极端状态跳转 |
| **比赛现场执行期** | 现场标定光照与网络配置；每日赛后坚持复盘并记录改动详情 |

## 5.5 队内信息维护流程

订阅信息渠道后，需要建立固定维护责任以防遗漏重要通知：

- 指定一名成员负责关注邮件列表，定期检索规则与赛制相关邮件并通报队内。
- 指定一名成员关注 Discord 中的规则讨论（rules）与赛事公告频道。
- 规则仓库保持定期检查，官方仓库合并重大 pull request 或发布 release 时记录变更点。
- 赛季结束后对当届规则版本及 commit 哈希进行本地归档，供后续查验使用。
