# diff
### Linux命令 diff
Linux中，我们常常用 diff 来比较两个文本文件，特别是同一个文件修改前后的差异。   
那么它的处理逻辑是什么样的，它的算法复杂度又如何？   

我们知道，diff 比较的是文件每行的差异。为了简化问题的难度，我们假设每行都只有一个字母，于是一个文件就简化为一个字符串。我们来看看，命令 diff 是如何比较两个字符串的。   
假设我们调用 diff 比较两个字符串"string" 和 "strength"，期待的效果如下：

	$ diff string strength
	| s
	| t
	| r
	- i
	+ e
	| n
	| g
	+ t
	+ h

#### 1.算法复杂度为 O(mn)

python实现：[diff_1.py](diff_1.py)

#### 2.算法复杂度为 O(nd)

#### 3.算法复杂度为 O(np)
