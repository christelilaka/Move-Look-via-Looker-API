import argparse
import looker_sdk
from helpers import MoveLook

old_instance = looker_sdk.init31("./ini_files/from_old_instance.ini")
new_instance = looker_sdk.init31("./ini_files/to_new_instance.ini")

parser = argparse.ArgumentParser(description="This app allows you to move one or many Looks from one Looker instance to another.")

parser.add_argument('-id', '--look_id', type=str, metavar="", help='Move one look, i.e. $ python app.py -id 12')
parser.add_argument('-li', '--list_IDs', type=str, metavar="", nargs='+', help='Move many Looks, i.e. $ python app.py -li 22, 12, 50, 33')
args = parser.parse_args()


if __name__ == '__main__':
    if args.look_id:
        id = args.look_id
        look = MoveLook(new_instance, old_instance, look_id=id)
        look.move()
        print(f"****** The Look with id: {id} has been moved ******")
    else:
        list_ids = args.list_IDs
        for id in list_ids:
            look = MoveLook(new_instance, old_instance, look_id=id)
            look.move()
            print(f"****** The Look with id: {id} has been moved ******")