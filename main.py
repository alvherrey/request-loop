from request import request

def loop():
    for i in range(3):
        print("Lanzando peticion...")
        with open(f"result-{i}.json", "w") as f:
            f.write(str(request(i)))    

def main():
    loop()

if __name__ == '__main__':
    main()