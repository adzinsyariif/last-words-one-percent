import os

LINE = "At 1% I finally get it — tell my charger I loved him, even if he only visited when I was dying inside."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
