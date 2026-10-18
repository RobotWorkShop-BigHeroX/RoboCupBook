面向对于RoboCup HSL完全不了解的人的手册
本手册下面还有两个文件夹
一个是公开的文件夹
一个是私有的文件夹（通过创建一个私有仓库来实现）
1 RoboCup介绍
1.1 涵盖有RoboCup的历史（尤其是HSL在近期的更改线路） 比如合并了SPL。取消了MSL，明年将取消仿真，home等等，集中精力去做HSL
1.2 RoboCup的历史强队，主要是合并后的目前 HS large/middle/small 几支队伍 附上仓库主页比如重点的仓库源码 和简介（地区，大学或机构，历史成绩） （能收集到的所有队伍另起一个文件）
下面是一个仓库资源的例子
B-Human 2026 技术文档：https://docs.b-human.de/coderelease2026/
B-Human 开源代码：https://github.com/bhuman/BHumanCodeRelease
B-Human 环境搭建教程：https://docs.b-human.de/coderelease2026/getting-started/initial-setup/

1.3 对目前赛事规则简单的介绍 比如7人制标准，比赛时长，半场时长，换人规则，（附上我自己做的规则链接(https://hcnwvqtaepc6.feishu.cn/wiki/PHPCwZCI8iPhDhksyzNcBFKRnIh?from=from_copylink)以及官方的Rules.pdf）记得时刻拉取最新源码
1.4 裁判盒的程序源码 记得时刻拉取最新源码

2 本队伍介绍的机器人平台和网站平台介绍（按照旧版T4型号，新版出来之后会更新）
2.1 T4型号机器人的介绍（好像有个手册），这种手册都放到一个本项目一个私有仓库下面，在私有仓库下面放着这些文件
除了机器人一些相关参数，需要了解的器件（IMU（该传感器提供什么信息，怎么用），里程计，
2.2 网站平台的介绍（有个PPT），简单介绍一下就行了也是放到私有仓库下面
2.3 中联重科 Zvalley的资源 
【中联重科 Zvalley】
开放资料总站：https://eai.zvalley.com/openSource
中联重科SDK说明网站：https://eai.zvalley.com/openSource/detail/2087512650565427200
中联重科SDK-GitHub网站：http://github.com/Zvalley-Robotics/zv_robot_sdk
Z01 机器人仿真资产网站：https://eai.zvalley.com/openSource/detail/2109932634205204480
Zlab_Gym开发手册：https://eai.zvalley.com/openSource/detail/2109922358609195008
2.4 本队伍的TDP。Vedio（https://www.youtube.com/watch?v=z3zi2sfMBm4），Robots，Software （https://hsl.robocup.org/qualified-teams/这里是详细的网址）这些东西附上链接（链接指向公开的文件夹下）

3 如何入手学习
有些内容不需要详细学习，比如ROS2，Linux，了解其思想即可，比如ROS2的DDS框架）
(禁止完全许愿式编程，但也不必转向一行行了解代码，这就像从一个低效走向另一个低效
                                                    ---- andinm_hong)
3.0 必学
Git（如果没用过GitHub，是新号建议开几个仓库刷一下Action）
 3.1 ros2 
- 1. DDS / RTPS 通信中间件
- 2. 节点与通信模型
- 3. QoS（服务质量策略）
- 4. Executor（执行器）与回调调度
- 5. Lifecycle Node（生命周期节点）
- 6. Node Composition（节点组合）与进程内通信
- 7. TF2（坐标变换系统）
- 8. rosbag2（数据录制与回放）
3.2 Linux
学习网址 https://labex.io/LinuxJourney?utm_source
`pwd`、`ls`、`cd`、`find`、`grep`、`tail`、`ps`、`source`、`git`、`cmake`
3.3 视觉（Yolo11（最稳定），Yolo26(最新，不做强制要求看个人兴趣)）
怎么用
用途
3.4 行为树和状态机（策略组 重点）
3.5 粒子滤波算法   （感知组 重点）
重点是了解怎么将该算法和TF转换结合实现全局定位（鉴于官方禁止使用雷达且深度相机是灰色地带）
3.6 深度强化学习（不做任何要求，看个人能力）
Bellman Optimization
BOE
TD
蒙特卡洛
policy Network
Actor-Critic
Q-learning
DDPG
PPO


4 消息渠道
官方网站开源工具和内容 时刻更新消息渠道，部分工具更新速度很快注意不用
https://hsl.robocup.org/  
202x.robocup.org 【HSL 官方入口】
HSL 官网：https://hsl.robocup.org/
HSL 规则仓库：https://github.com/RoboCup-HumanoidSoccerLeague/HSL-Rules
2026 年规则文档：https://hcnwvqtaepc6.feishu.cn/wiki/PHPCwZCI8iPhDhksyzNcBFKRnlh
新参赛队指南：https://hsl.robocup.org/information-for-new-teams/
2026 参赛队资料汇总：https://hsl.robocup.org/qualified-teams/
官方 GameController（裁判盒）：https://github.com/RoboCup-HumanoidSoccerLeague/GameController
机器人检查工具：https://github.com/RoboCup-HumanoidSoccerLeague/RobotInspection
官方机器人支持项目：https://robotprogram.robocup.org/
【公告渠道】
邮件列表：https://lists.robocup.org/mm/lists/robocup-humanoid.lists.robocup.org/  必须订阅
Discord：https://discord.gg/67qGN8ycwz                                           必须进群



5 安全守则
机器人必须要在吊机上面
机器人在行走状态关节没自锁的情况下禁止双脚悬空
测试机器人的时候最好三人，一人推吊车（或者握住扶手） 一人操控遥控器（情况不对进阻尼） 
如果机器人出现危险动作（全身剧烈抖动）立马进阻尼（不要犹豫，练成肌肉记忆），如果没反应，使用Stop按钮（不太建议，基本所有的情况进阻尼都可以解决）一切以个人安全为先，机器人（全身铝合金，重达四十公斤）爆发力气很大切记
机器人开机前要注意把关节复位

