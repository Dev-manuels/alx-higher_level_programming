#!/usr/bin/python3
"""
script that adds all arguments to a Python list,
and then save them to a file
"""
if __name__ == "__main__":
    import sys

    load_from_json_file = __import__("6-load_from_\
       json_file").load_from_json_file
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

    """
    Check if the file already has a object stored in it,
    retrive the object if yes"""
    try:
        old_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        old_list = []
    """read the new args"""
    new_list = sys.argv[1:]

    """update the old args with the new one"""
    old_list.extend(new_list)
    """save the updated object to the JSON file"""
    save_to_json_file(old_list, "add_item.json")
