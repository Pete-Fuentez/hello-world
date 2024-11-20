def applyFunc(function_arg, data_arg):
    return function_arg(data_arg)

result1 = applyFunc(abs, -4)
print(result1)

import math
result2 = applyFunc(math.sqrt, 2)
print(result2)

