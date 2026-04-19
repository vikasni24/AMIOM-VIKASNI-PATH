def main():
    a = 5
    b = "10"
    
    print("The sum is: ")
    # Fix: convert str to int before adding
    print(a + int(b))

if __name__ == "__main__":
    main()