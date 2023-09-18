class TreeNode:

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


class BinaryTree:

  def __init__(self):
    self.root = None

  # 1. Inserir um elemento em uma árvore binária de busca.
  def insert(self, value):
    self.root = self._insert_recursive(self.root, value)

  def _insert_recursive(self, node, value):
    if node is None:
      return TreeNode(value)
    if value < node.value:
      node.left = self._insert_recursive(node.left, value)
    else:
      node.right = self._insert_recursive(node.right, value)
    return node

  # 2. Percorrer a árvore, imprimindo os valores dos nós (inorder).
  def inorder_traversal(self):

    def _inorder(node):
      if node:
        _inorder(node.left)
        print(node.value, end=' ')
        _inorder(node.right)

    _inorder(self.root)
    print()

  # 3. Percorrer a árvore, imprimindo os valores dos nós, segundo a estratégia pré-ordem.
  def preorder_traversal(self):

    def _preorder(node):
      if node:
        print(node.value, end=' ')
        _preorder(node.left)
        _preorder(node.right)

    _preorder(self.root)
    print()

  # 4. Percorrer a árvore, imprimindo os valores dos nós, segundo a estratégia pós-ordem.
  def postorder_traversal(self):

    def _postorder(node):
      if node:
        _postorder(node.left)
        _postorder(node.right)
        print(node.value, end=' ')

    _postorder(self.root)
    print()

  # 5. Verificar se um certo valor n está presente na árvore.
  def contains(self, value):
    return self._contains_recursive(self.root, value)

  def _contains_recursive(self, node, value):
    if node is None:
      return False
    if value == node.value:
      return True
    elif value < node.value:
      return self._contains_recursive(node.left, value)
    else:
      return self._contains_recursive(node.right, value)

  # 6. Retornar o maior valor presente em uma árvore.
  def find_max(self):
    current = self.root
    while current.right:
      current = current.right
    return current.value

  # 7. Retornar o menor valor presente em uma árvore.
  def find_min(self):
    current = self.root
    while current.left:
      current = current.left
    return current.value

  # 8. Retornar a média dos valores presentes em uma árvore.
  def find_average(self):
    sum_values = self._sum_recursive(self.root)
    count_nodes = self._count_nodes_recursive(self.root)
    return sum_values / count_nodes if count_nodes > 0 else 0

  def _sum_recursive(self, node):
    if node is None:
      return 0
    return node.value + self._sum_recursive(node.left) + self._sum_recursive(
        node.right)

  def _count_nodes_recursive(self, node):
    if node is None:
      return 0
    return 1 + self._count_nodes_recursive(
        node.left) + self._count_nodes_recursive(node.right)

  # 9. Retornar a soma dos valores dos nós.
  def sum_of_values(self):
    return self._sum_recursive(self.root)

  # 10. Retornar o número de nós de uma árvore.
  def count_nodes(self):
    return self._count_nodes_recursive(self.root)

  # 11. Retornar o número de folhas de uma árvore.
  def count_leaves(self):
    return self._count_leaves_recursive(self.root)

  def _count_leaves_recursive(self, node):
    if node is None:
      return 0
    if node.left is None and node.right is None:
      return 1
    return self._count_leaves_recursive(
        node.left) + self._count_leaves_recursive(node.right)

  # 12. Retornar a altura de uma árvore.
  def get_height(self):
    return self._get_height_recursive(self.root)

  def _get_height_recursive(self, node):
    if node is None:
      return 0
    left_height = self._get_height_recursive(node.left)
    right_height = self._get_height_recursive(node.right)
    return 1 + max(left_height, right_height)


# Exemplo de uso:
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(8)
tree.insert(1)
tree.insert(4)
tree.insert(7)
tree.insert(9)

tree.inorder_traversal()
tree.preorder_traversal()
tree.postorder_traversal()

print("Contains 4:", tree.contains(4))
print("Contains 6:", tree.contains(6))

print("Max:", tree.find_max())
print("Min:", tree.find_min())
print("Average:", tree.find_average())
print("Sum of values:", tree.sum_of_values())
print("Number of nodes:", tree.count_nodes())
print("Number of leaves:", tree.count_leaves())
print("Height:", tree.get_height())
