import sys

input = sys.stdin.readline

n_jewely, n_bag = map(int, input().split())

jewel_weight_list, jewel_price_list = [], []
bag_capacity_list = []

for _ in range(n_jewely):
    a, b = map(int, input().split())
    jewel_weight_list.append(a)
    jewel_price_list.append(b)

for _ in range(n_bag):
    bag_capacity_list.append(int(input()))


print(f'[debug]  jewel_weight_list: {jewel_weight_list}')
print(f'[debug]  jewel_price_list: {jewel_price_list}')
print(f'[debug]  bag_capacity_list: {bag_capacity_list}')
