from collections import deque


class File:
  def __init__(self, name, size):
    self.name = name
    self.size = size

  def getSize(self):
    return self.size


class Directory:
  def __init__(self, name, parent=None):
    self.name = name
    self.children: list['Directory'] = []
    self.files: list[File] = []
    self.size = 0
    self.parent = parent

  def setFile(self, file: File):
    self.files.append(file)
    self.size += file.getSize()

  def setChild(self, folder: 'Directory'):
    self.children.append(folder)

  def getChildren(self):
    return self.children

  def getFiles(self):
    return self.files

  def getParent(self):
    return self.parent

  def getName(self):
    return self.name


class FileSystem:
  def __init__(self, root: Directory):
    self.root = root
    self.currentDir = root

  def cd(self, dir):
    match dir:
      case '..':
        if self.currentDir.getParent():
          self.currentDir = self.currentDir.getParent()
        else:
          self.currentDir = self.root
      case '/':
        self.currentDir = self.root
      case _:
        for child in self.currentDir.getChildren():
          if child.getName() == dir:
            self.currentDir = child
            break
    return


def buildFileSystem(commandList):
  root = Directory('/')
  fileSystem = FileSystem(root)
  currCommand = 0

  while currCommand < len(commandList):
    if commandList[currCommand][0] == '$':
      if commandList[currCommand][2:4] == 'cd':
        fileSystem.cd(commandList[currCommand][5:])
        currCommand += 1
      elif commandList[currCommand][2:4] == 'ls':
        currCommand += 1
        while currCommand < len(commandList) and commandList[currCommand][0] != '$':
          sizeOrDir, name = commandList[currCommand].split(' ')
          if sizeOrDir == 'dir':
            fileSystem.currentDir.setChild(
                Directory(name, fileSystem.currentDir))
          else:
            fileSystem.currentDir.setFile(File(name, int(sizeOrDir)))
          currCommand += 1

  fileSystem.cd('/')
  return fileSystem


def traverseFileSystem(fileSystem: FileSystem):
  queue = deque([fileSystem.root])

  while len(queue) > 0:
    current = queue.popleft()
    print('Folder:', current.getName())
    print('Size:', current.size)
    for child in current.getChildren():
      queue.append(child)
    print('Files in folder:')
    for file in current.getFiles():
      print(file.name, 'with size:', file.size)
    print('\n')


def totalDirectorySizes(root: Directory):
  children = root.getChildren()

  if len(children) == 0:
    return root.size

  for child in children:
    root.size += totalDirectorySizes(child)

  return root.size


def totalSizeLessThanLimit(root: Directory, limit):
  children = root.getChildren()

  if len(children) == 0:
    if root.size <= limit:
      return root.size
    else:
      return 0

  sum = 0

  for child in children:
    sum += totalSizeLessThanLimit(child, limit)

  if root.size <= limit:
    sum += root.size

  return sum


def sizeOfDirectoryToDelete(root: Directory, minSize):
  queue = deque([root])
  candidates = []

  while len(queue) != 0:
    current = queue.popleft()
    if current.size >= minSize:
      candidates.append(current.size)

    for child in current.getChildren():
      queue.append(child)

  return min(candidates)


if __name__ == '__main__':
  file = open('testCase.txt', 'r')
  lines = [line.strip() for line in file.readlines()][1:]

  fileSystem = buildFileSystem(lines)

  usedDiskSpace = totalDirectorySizes(fileSystem.root)

  print(totalSizeLessThanLimit(fileSystem.root, 100000))

  totalDiskSpace = 70000000
  spaceRequired = 30000000

  spaceRemaining = totalDiskSpace - usedDiskSpace
  spaceToDelete = spaceRequired - spaceRemaining

  print(sizeOfDirectoryToDelete(fileSystem.root, spaceToDelete))
