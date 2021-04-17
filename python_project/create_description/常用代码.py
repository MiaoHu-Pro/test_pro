import pandas as pd


#随机选择维度
sample_x_df = pd.DataFrame(sample_X)
#特征的选择
count  = round(column * max_feature)  # round() 方法返回浮点数x的四舍五入值。
n_feature = int(count)#取整
random_feature = random.sample(range(0,column),n_feature) # sample(x,y)函数的作用是从序列x中，随机选择y个不重复的元素。
#训练数据做子空间的选择
sample_X = sample_x_df[random_feature]#选择相应的特征（即去除没有被选择的特征）


#求列表中未出现的数据
n_sample_list = random.sample(range(0, n_sample), n_sample)
out_of_bag_index = list(set(n_sample_list) - set(index_list))#未出现的样本下标

a = [random.randint(0, 100) for _ in range(100)] #0-99 ,100个数中生成100个随机数
item = Counter(a)  # [4,2,1]
print(a)
print(set(item.keys()))


df = pd.DataFrame(diabetes)
print(df)
df.to_csv('./data_set/diabetes.csv', index=False, header=False, )


# 特征的选择
count = round(column * max_feature)  # round() 方法返回浮点数x的四舍五入值。
n_feature = int(count)  # 取整
random_feature = random.sample(range(0, column), n_feature)  # sample(x,y)函数的作用是从序列x中，随机选择y个不重复的元素。

#读取文件夹中的文件


# 1. 获取一个要重命名的文件夹的名字
file_read_path = './data_set_nor'

# 2. 获取那个文件夹中所有的文件名字
file_names = os.listdir(file_read_path)

for name in file_names: #遍历文件
    pass


#==============================多线程======================================================
def thread_fit(self, X, y):
    trees = []
    for i in range(self.n_estimators):
        # 创建基分类器
        tree = DecisionTreeClassifier(self.max_features, self.criterion, self.max_depth, self.min_samples_split,
                                      self.min_impurity_split)
        trees.append(tree)

    from sklearn.ensemble.forest import Parallel, delayed
    trees = Parallel(n_jobs=1, verbose=20,
                     backend="threading")(
        delayed(_parallel_build_trees)(tree, i, X, y, self.bootstrap)
        for i, tree in enumerate(trees))

    self.forest.extend(trees)

    print("thread_fit over ......", len(self.forest))

def _parallel_build_trees(tree,i, X, y,bootstrap):

    X, y = sampling_with_reset(X,y,bootstrap)
    print('训练树',i)
    tree.fit(X, y)  # 决策树
    return tree
#====================================================================================



#数据规范化

min_max_scaler = preprocessing.MinMaxScaler()
data = min_max_scaler.fit_transform(data[:, :-1])

data = np.column_stack((data, data_y))

print("数组规范化！")
print(data)





path = '../src/U.txt'
# 手写读取数据
f = open(path)
x = []
y = []
for d in f:
    d = d.strip()
    if d:
        d = d.split(' ')
        # 每个元素转为int
        new_numbers = []
        for n in d:
            new_numbers.append(int(n))
        d = new_numbers

        x.append(d)

x = np.array(x)

#============================================================
# # # 手写读取数据
# # f = file(path)
# # x = []
# # y = []
# # for d in f:
# #     d = d.strip()
# #     if d:
# #         d = d.split(',')
# #         y.append(d[-1])
# #         x.append(map(float, d[:-1]))
# # print '原始数据X：\n', x
# # print '原始数据Y：\n', y
# # x = np.array(x)

#当一个对象被创建时，计数器自动加1
class Stu(object):
    id = 0
    def __init__(self,number,name):
        self.number = number
        self.name = name
        self.idd = Stu.id
        Stu.id += 1





data = X_data[X_data[:,feature_index].argsort()] #按照指定的列排序

#计算gini系数
def gini(y):

    distribution = Counter(y)  # Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，
    s = 0.0
    total = len(y)
    for y_index, num_y in distribution.items():
        s += np.power(num_y / total, 2)

    return 1 - s

#使用Counter 统计每个元素出现多少次！
def entropy(Y):
    """ In information theory, entropy is a measure of the uncertanty of a random sample from a group. """

    distribution = Counter(Y)  # Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，
    s = 0.0
    total = len(Y)
    for y, num_y in distribution.items():
        probability_y = (num_y / total)
        s += probability_y * np.log(probability_y)
    return -s


#获取唯一值
import numpy as np
import pandas as pd

a = [[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3]]
a_1 = np.ravel(a)#二维数组变成1维数组 [1 1 1 1 1 2 2 2 2 2 3 3 3 3 3]
print(a_1)
# scores = np.unique(np.ravel(a))
scores = np.unique(a)#[获取唯一值]
print(type(scores))
print(scores.tolist()) #[1, 2, 3]


#余弦距离
def cos_distance(vector1,vector2):

    dot_product = 0.0
    normA = 0.0
    normB = 0.0
    for a,b in zip(vector1,vector2):
        dot_product += a*b
        normA += a**2
        normB += b**2
    if normA == 0.0 or normB==0.0:
        return None
    else:
        return dot_product /((normA*normB)**0.5)

#计算欧式距离 方法1 省时，高效
def euclidean_distance(vector1, vector2):
    d = 0
    for a, b in zip(vector1, vector2):
        d += (a - b) ** 2
    # return d ** 0.5
    return np.sqrt(d)
#计算欧式距离 方法2
def euclidean_distance_2(vector1, vector2):

    dis = np.linalg.norm(np.array(vector1) - np.array(vector2)) #

    return dis

#计算曼哈顿距离
def manhattan_distance(vector1,vector2):

    return sum(abs(np.array(vector1) - np.array( vector2)))




#计算两个向量的欧式距离
np.linalg.norm(np.array(x_for_subspace[j]) - np.array(self.circle[j])) #不同子空间进行相应的距离计算

#
# 规划操作
min_max_scaler = preprocessing.MinMaxScaler()
R3=min_max_scaler.fit_transform(R2)

#存储模型
def save_model(rf_model):
    with open('./rf_model.pkl', 'wb') as f:
        pickle.dump(rf_model, f)  # 保存模型


def load_model():
    # 重新加载模型进行预测
    with open('rf_model.pkl', 'rb') as f:
        model = pickle.load(f)  # 加载模型
    return model


##打印文件名，函数名，行号
import sys
def get_cur_info():
    print (sys._getframe().f_code.co_filename)  #当前文件名，可以通过__file__获得
    print (sys._getframe().f_code.co_name)  #当前函数名
    print (sys._getframe().f_lineno) #当前行号
get_cur_info()#打印文件名，函数名，行号

print('===',sys._getframe().f_code.co_filename,sys._getframe().f_code.co_name,sys._getframe().f_lineno,"===")


# 获取元素下标
sequence = [1,2,3,4,5,6,7,1,2,3,4,5,6]

print(sequence.index(2))  ###your_list为列表名称   your_item为需要修该的数据

print([ i for i, x in enumerate(sequence) if x == 2])



# k = [1.0,2.0,3.0,]
# 创建n个list
list_class = [[] for i in range(num_class)]

# 添加一列
#在arr_2 后加上一列
data_set = np.column_stack((arr_2, data_y))

#按列合并
data_set = np.vstack((arr_2, data_y))


# 数组数据保存到csv
save_path = './data_set/userJoinFlow_after_cut_off_v6.csv'
df = pd.DataFrame(data_set) # data_set 转为dataFrame ，然后写入csv
df.to_csv(save_path, sep=',', index=False, header=False)

#================================================================
#数据拆分，一个类存放到一个list中
# 第一步，分离数据集合，得到类别个数K
k = set(data[:, -1])

# 数据的行与列
row, column = data.shape
# 拆分矩阵

# 类别个数
num_class = len(k)

# k = [1.0,2.0,3.0,]
# 创建n个list
list = [[] for i in range(num_class)]
k_class = list(set(data[:, -1]))
# list[0] 中存放的是1类
# list[1] 中存放的是2类
# num_class 类别个数
# k_class 一个有序非重复列表 存放类标签
for c in range(num_class):
    for i in range(row):
        if (data[i, -1] == k_class[c]):
            calss_list[c].append(data[i].tolist())

#=================================================================
    #将list放入list中，并转为数组
    data_set = list() #
    for c in range(wkj_row):
        # print (list_class[c])
        data_set += list_class[c]

    #list 转为数组
    data_set = np.array(data_set)
    print(data_set)

#=================================================
#删除列
    data_y = data[:,-1] #获取标签列
    data_X = data[:,:-1] #获取非标签列

    data_df = pd.DataFrame(data_X) #转为dataframe

    row , column = data_df.shape

    print(data_df)
    # 删除偶数列
    data_df2 = data_df.drop([i for i in range(column) if i %2 != 0],axis= 1)

    print (data_df2)

    arr_2 = np.array(data_df2) #data_frame 转为array

    #添加一列
    data_set = np.column_stack((arr_2, data_y))

    print (data_set)

#========================================
# 还有for循环的用list解析的

# [对(x)的操作
# for x in 集合 if 条件]
#
# [对(x, y)的操作
# for x in 集合1 for y in 集合2 if 条件]
# 举一个简单的例子：

x = [1, 2, 3, 4]

y = [5, 6, 7, 8]

# 我想让着两个list中的偶数分别相加，应该结果是2 + 6, 4 + 6, 2 + 8, 4 + 8
#
# 下面用一句话来写

print([a + b for a in x for b in y if a % 2 == 0 and b % 2 == 0])

print ([ x for x in one if x%2==0 ])


#=================================================================
#一行一行写入文件
data_path = './data_set/userJoinFlow_v6_2.csv'

# 打开文件
data_file = open(data_path, 'w+', newline='')

# 写入文件
write_file = csv.writer(data_file)

# 第一步将数据集分开 ，一类用一个文件存储
n = len(c_dataset)
print(n)
n1, n2, n3, n4, n5, n6, n7 = 0, 0, 0, 0, 0, 0, 0
for i in range(n):
    if c_dataset[i, -1] == 2:
        n1 = n1 + 1
        write_file.writerow(c_dataset[i, :])
