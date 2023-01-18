class TreeNode:
    def __init__(self,name,designation):
      self.name = name
      self.designation = designation
      self.data = f'{name} ({designation})'
      self.children = []
      self.parent = None


    def add_child(self,child):
       child.parent = self
       self.children.append(child)


    def get_level(self):
      level = 0

      p = self.parent 
      while p:
        level += 1
        p = p.parent

      return level


    def print_tree(self,keyword):
      spaces = ' ' * self.get_level() * 3

      prefix = spaces + '|-->' if self.parent else "--"

      data = ''

      if keyword == 'name':
         data = self.name
      elif keyword == 'designation':
         data = self.designation
      elif keyword == 'both':
         data = self.data
      else:
         raise Exception("No Argument provided in print_tree function")
      
      print(prefix + data)
      if self.children:
        for child in self.children:
            child.print_tree(keyword)



def build_product_tree():
  root = TreeNode("Nilupul","CEO")

  cto = TreeNode("Chinmay", 'CTO')
  hr_head = TreeNode("Gells",'HR head')

  i_head = TreeNode("Vishwa","InfraStructure Head")
  i_head.add_child(TreeNode("Dhaval","Cloud Manager"))
  i_head.add_child(TreeNode("Abhijit","App Manager"))

  cto.add_child(i_head)
  cto.add_child(TreeNode('Aamir',"Application Head"))

  hr_head.add_child(TreeNode("Peter","Recruitment Manager"))
  hr_head.add_child(TreeNode("Waqas","Policy Manager"))

  root.add_child(cto)
  root.add_child(hr_head)
  return root

if __name__ == '__main__':
  root = build_product_tree()
  root.print_tree('name')
  root.print_tree('designation')
  root.print_tree('both')
