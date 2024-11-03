class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "堆疊是空的"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "堆疊是空的"

    def is_empty(self):
        return len(self.stack) == 0

def is_balanced(parentheses):
    stack = Stack()
    matching_parentheses = {')': '(', '}': '{', ']': '['}

    for char in parentheses:
        if char in matching_parentheses.values():
            stack.push(char)
        elif char in matching_parentheses.keys():
            if stack.is_empty() or stack.pop() != matching_parentheses[char]:
                return False

    return stack.is_empty()

# 使用示例
if __name__ == "__main__":
    parentheses = "{[()]}"
    print(f"括號序列 {parentheses} 是否匹配：", is_balanced(parentheses))

    parentheses = "{[(])}"
    print(f"括號序列 {parentheses} 是否匹配：", is_balanced(parentheses))