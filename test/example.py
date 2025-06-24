from god import GodAgent

god = GodAgent()

# 加载世界观设定
world_background = "在一个被黑暗魔法笼罩的奇幻世界，玩家是最后的龙裔战士..."

# 配置初始状态
god.update_world_state(
    background=world_background
)

while True:
    narrative, options, new_role = god.generate_narrative()

    print("## 新剧情 ##")
    print(narrative)
    if new_role:
        print("\n## 新角色 ##")
        print(f"你遇到了{new_role[0]}!")
    print("\n## 玩家选项 ##")
    for i, opt in enumerate(options, 1):
        print(f"{i}. {opt}")
    print()

    # 更新玩家行动
    player_choice = int(input())

    info = (options[player_choice - 1], [])

    god.update_information(info)
