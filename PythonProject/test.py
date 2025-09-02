######################################
## Autor:Qu Hongbin
## CreatedDate:2025-08-29
## File: test.py
#######################################
class GameConfig:
    # Set the weight of each reward item and use it in reward_manager
    # 设置各个回报项的权重，在reward_manager中使用
    REWARD_WEIGHT_DICT = {
        "tower_hp_point": 5.0,
        "forward": 0.01,
    }
class RewardStruct:
    def __init__(self, m_weight=0.0):
        self.cur_frame_value = 0.0
        self.last_frame_value = 0.0
        self.value = 0.0
        self.weight = m_weight
        self.min_value = -1
        self.is_first_arrive_center = True

def init_calc_frame_map():
    calc_frame_map = {}
    for key, weight in GameConfig.REWARD_WEIGHT_DICT.items():
        calc_frame_map[key] = RewardStruct(weight)
    return calc_frame_map
# calc_frame_map = init_calc_frame_map()
# print(calc_frame_map["tower_hp_point"])
 


def calculate_money_reward(main_money,enemy_money,main_moneyCnt,enemy_moneyCnt):
    if main_money > enemy_money and main_moneyCnt > enemy_moneyCnt:
        return 1
    return 0
money_reward = calculate_money_reward(3,2,6,5)

print(money_reward)