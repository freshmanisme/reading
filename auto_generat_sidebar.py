# 用二叉树自动print sidebar
import os

# repository_path = r'C:\Users\guofei8\Desktop\git\GitHub\reading'
# doc_path = repository_path + r'\docs'
#
# path_walker = os.walk(doc_path, topdown=True)
# # 返回一个 generator ，每个元素是一个 tuple，内容分别是
# # 目录，下级目录列表，下级文件列表
#
#
# #%%
# class TreeNode:
#     def __init__(self, value, type, layer):
#         self.value = value
#         self.type = type  # 'file' or 'path'
#         self.layer = layer
#         self.children = dict()
#
#
# class Tree:
#     def __init__(self):
#         self.root = TreeNode('root', 'path', 0)
#
#     def addTreeNode(self, path, dirs, nondirs):
#         pointer = self.root
#         for i in path:
#             if i not in pointer.children:
#                 pointer.children[i] = TreeNode(i, 'path', pointer.layer + 1)
#             pointer = pointer.children[i]
#         for i in dirs:
#             pointer.children[i] = TreeNode(value='* ' + i, type='path', layer=pointer.layer + 1)
#         for i in nondirs:
#             file_name = '* [' + i.replace('.md','') + ']' + '(' + '/'.join(path) +'/'+ i + ')'  # 直接在file格式的叶节点内写入Markdown语句
#             pointer.children[i] = TreeNode(value=file_name, type='file', layer=pointer.layer + 1)
#
#     def add_all_tree_node(self, path_walker):
#         for top, dirs, nondirs in path_walker:
#             path = top.replace(repository_path, '').split('\\')[1:]
#             self.addTreeNode(path, dirs, nondirs)
#
#     def pre_order(self, root):
#         return '' if (root is None) \
#             else ((root.layer-2) * '    ' if root.layer>1 else '# ') + root.value + '\n' + \
#                  ''.join([self.pre_order(i) for i in root.children.values()])
#
#
# tree = Tree()
# tree.add_all_tree_node(path_walker)
# a = tree.pre_order(tree.root.children['docs'])
# print(a)
#
# #%%
#
#
# # 用二叉树自动print sidebar
# import os
#
# repository_path = r'C:\Users\guofei8\Desktop\git\GitHub\reading'
# doc_path = repository_path + r'\docs'
#
# path_walker = os.walk(doc_path, topdown=True)
# # 返回一个 generator ，每个元素是一个 tuple，内容分别是
# # 目录，下级目录列表，下级文件列表


#%%
import os

class TreeNode:
    def __init__(self, value, type, layer):
        self.value = value
        self.type = type  # 'file' or 'path'
        self.layer = layer
        self.children = dict()


class Tree:
    def __init__(self,path):
        path_walker = os.walk(path, topdown=True)
        self.path1,path2='\\'.join(path.split('\\')[:-1]),path.split('\\')[-1]
        self.root = TreeNode(path2, 'path', 0)
        self.add_all_tree_node(path_walker)

    def addTreeNode(self, path, dirs, nondirs):
        pointer = self.root
        for i in path:
            if i not in pointer.children:
                pointer.children[i] = TreeNode(i, 'path', pointer.layer + 1)
            pointer = pointer.children[i]
        for i in dirs:
            pointer.children[i] = TreeNode(value='* ' + i, type='path', layer=pointer.layer + 1)
        for i in nondirs:
            file_name = '* [' + i.replace('.md','') + ']' + '(' + '/'.join(path) +'/'+ i + ')'
            # 直接在file格式的叶节点内写入Markdown语句
            pointer.children[i] = TreeNode(value=file_name, type='file', layer=pointer.layer + 1)

    def add_all_tree_node(self, path_walker):
        for top, dirs, nondirs in path_walker:
            path = top.replace(self.path1, '').split('\\')[1:]
            self.addTreeNode(path, dirs, nondirs)

    def pre_order(self, root):
        return '' if (root is None) \
            else ((root.layer-2) * '    ' if root.layer>1 else '# ') + root.value + '\n' + \
                 ''.join([self.pre_order(i) for i in root.children.values()])


path = r'C:\Users\guofei8\Desktop\git\GitHub\reading\docs'
tree = Tree(path)
a = tree.pre_order(tree.root.children['docs'])
# print(a)

#%%
head='''
<a href="http://www.guofei.site" target='blog'>
<img src="http://www.guofei.site/public/img/me.png"  alt="回到blog" height="64" width="64">
</a>

'''

tail='''

* 建站日志
    * [快速开始](建站日志/quickstart.md)
    * [多页文档](建站日志/more-pages.md)
    * [配置项](建站日志/configuration.md)
    * [主要配置](建站日志/themes.md)
    * [扩展Markdown语法<sup style="color:red">(new)<sup>](建站日志/markdown.md)
'''



content='\n'.join(a.split('\n')[1:])

f=open('_sidebar.md','w',encoding='utf-8')
# print(head+content)
# f.write(head+content.encode('utf-8').decode('utf-8'))
f.write(head+content+tail)
f.close()

