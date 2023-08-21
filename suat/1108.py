class Solution:
    def interpret(self, command: str) -> str:
        parsed = ""
        i = 0
        
        while i < len(command):
          
            if command[i] == "G":
                parsed += command[i]
                i += 1
            elif command[i:i+2] == "()":
                parsed += "o"
                i += 2
            else:
                parsed += 'al'
                i += 4

        return parsed