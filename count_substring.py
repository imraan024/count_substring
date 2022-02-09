def count_substring(string,sub_string):
    l=len(sub_string)
    count=0
    for i in range(len(string)-len(sub_string)+1):
        if(string[i:i+len(sub_string)] == sub_string ):
            count+=1
    return count

def main():
    string  = "tadadattaetadadadafa"
    sub_string = "dada"
    print("Number of occurrence: ", count_substring(string, sub_string))

if __name__ == "__main__":
    main()