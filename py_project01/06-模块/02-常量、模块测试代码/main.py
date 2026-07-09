# 1、导入模块中所有内容
from my_fun import *

# 2、使用模块中的内容
print("PI = ", PI)
print("NAME = ", NAME)

log_separator1()
log_separator2()

# ⚠️，如果不想导入模块中的某些内容，可以在 __all__ 中排除。
# log_separator3()
# log_separator4() 