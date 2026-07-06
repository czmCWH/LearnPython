# 案例1
# 需求：将用户输入的10个数字存储到一个列表中，并将列表中的数字进行排序，输出其中的最小值、最大值 和 平均值
nums = []
for i in range(10):
    num = int(input('请输入第%d个数字: ' % (i + 1)))
    nums.append(num)
    print(nums)
else:
    print("所有数据录入完成")

# ⚠️ min() 函数获取列表的最小值
# ⚠️ max() 函数获取列表的最大值
print('列表中最小值为：', min(nums))
print('列表中最大值为：', max(nums))
print('-----------------')
nums.sort()
print('排序后的列表为：%s' % nums)
print('最大值为：%d' % nums[-1])
print('最小值为：%d' % nums[0])
# ⚠️ len() 函数获取列表的长度1
# ⚠️ sum() 函数计算列表的和
print('平均值为：%d' % (sum(nums) / len(nums)))