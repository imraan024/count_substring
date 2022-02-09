# Documentation
### Case: Write a program which will find all occurrences of a pattern in a text .Suppose there is a text “tadadattaetadadadafa” and a  pattern “dada”, now you have to find how many times “data” appear in “tadadattaetadadadafa” . Here the pattern (data) appears in text (tadadattaetadadadafa) 3 times.

**NOTE:** I think there is a typo on the problem statement. In the problem statement `data` appears in given text 3 times which is not true for the given string `tadadattaetadadadafa`. But the substring `dada` appears 3 times. So I solved this problem with substring `dada`

#### My Solution: [count_substring.py](https://www.example.com)
```
def count_substring(string,sub_string):
    l=len(sub_string)
    count=0
    for i in range(len(string)-len(sub_string)+1):
        if(string[i:i+len(sub_string)] == sub_string):
            count+=1
    return count

def main():
    string  = "tadadattaetadadadafa"
    sub_string = "dada"
    print("Number of occurrence: ", count_substring(string, sub_string))

if __name__ == "__main__":
    main()
```


1. At first I've impliment a function which takes two string(Main string and sub string) as parameter.

2. I have to match the sub string with main string to count how much time it appears. So I measure the length of sub string so that I can match it with main string's that length using loops.

3. I took a counter to increase its value by 1 when sub string matches with main strings explored part.

4. After exploring the whole main string I returned the counter value which indicates the actual number of matches.
