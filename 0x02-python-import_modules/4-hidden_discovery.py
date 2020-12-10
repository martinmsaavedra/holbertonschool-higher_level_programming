#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    token = dir(hidden_4)
    for s in range(len(token)):
         if token[s][:2] != "__":
             print(token[s])
