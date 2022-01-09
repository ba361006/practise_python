import factory

def clientCode(factory: factory.FurnitureFactory):
    Chair = factory.createChair()
    Table = factory.createTable()

    print(Chair.sitOn())
    print(Table.putThingsOn())

if __name__ == "__main__":

    # 家具總公司根據客戶的古典風格，生產古典風格的桌子、椅子給客戶試試看
    print("Client is trying classic style furniture")
    clientCode(factory.ClassicFactory())

    print()

    # 家具總公司根據客戶的現代風格，生產現代風格的桌子、椅子給客戶試試看
    print("Client is trying modern style furniture")
    clientCode(factory.ModernFactory())