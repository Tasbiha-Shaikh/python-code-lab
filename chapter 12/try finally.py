def main():
    try:
        x = int(input("Hey enter the number: "))
        print(x)
        return
    except Exception as e:
        print(e)
        return
    finally:
        print("heyy this is finally")

main()

#finallu chalta hi chalta hai return ky bad bi chaly ga hi 
