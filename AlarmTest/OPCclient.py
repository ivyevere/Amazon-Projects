import sys
sys.path.insert(0, "..")


from opcua import Client


if __name__ == "__main__":

    client = Client("opc.tcp://localhost:4840/freeopcua/server/")
    # client = Client("opc.tcp://admin@localhost:4840/freeopcua/server/") #connect using a user
    try:
        client.connect()

        # Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
        root = client.get_root_node()
        print("Objects node is: ", root)

        # Node objects have methods to read and write node attributes as well as browse or populate address space
        print("Children of root are: ", root.get_children())

        # getting a variable node using its browse path
        myvar = root.get_child(["0:Objects", "2:MyObject", "2:MyVariable"])
        obj = root.get_child(["0:Objects", "2:MyObject"])
        print("myvar is: ", myvar)
        print("myobj is: ", obj)

        # Stacked myvar access
        # print("myvar is: ", root.get_children()[0].get_children()[1].get_variables()[0].get_value())

    finally:
        client.disconnect()