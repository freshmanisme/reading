import os

repository_path = r'C:\Users\guofei8\Desktop\git\GitHub\test_for_docsify'
doc_path = repository_path + r'\docs'

path_walker = os.walk(doc_path, topdown=True)


class TreeNode:
    def __init__(self, value, type, layer):
        self.value = value
        self.type = type  # 'file' or 'path'
        self.layer = layer
        self.children = dict()


class Tree:
    def __init__(self):
        self.root = TreeNode('root', 'path', 0)

    def addTreeNode(self, path, dirs, nondirs):
        pointer = self.root
        for i in path:
            if i not in pointer.children:
                pointer.children[i] = TreeNode(i, 'path', pointer.layer + 1)
            pointer = pointer.children[i]
        for i in dirs:
            pointer.children[i] = TreeNode(value='* ' + i, type='path', layer=pointer.layer + 1)
        for i in nondirs:
            file_name = '* [' + i.replace('.md','') + ']' + '(' + '/'.join(path) +'/'+ i + ')'  # 直接在file格式的叶节点内写入Markdown语句
            pointer.children[i] = TreeNode(value=file_name, type='file', layer=pointer.layer + 1)

    def add_all_tree_node(self, path_walker):
        for top, dirs, nondirs in path_walker:
            path = top.replace(repository_path, '').split('\\')[1:]
            self.addTreeNode(path, dirs, nondirs)

    def pre_order(self, root):
        return '' if (root is None) \
            else ((root.layer-2) * '    ' if root.layer>1 else '# ') + root.value + '\n' + \
                 ''.join([self.pre_order(i) for i in root.children.values()])


tree = Tree()
tree.add_all_tree_node(path_walker)
a = tree.pre_order(tree.root.children['docs'])
print(a)

