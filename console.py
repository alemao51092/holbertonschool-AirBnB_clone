#!/usr/bin/python3
"shebang"
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    "instantation"

    prompt = "(hbnb) "
    classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review}

    def do_help(self, arg):
        "help function"
        return super().do_help(arg)

    def help_quite(self, arg):
        "quit"
        print("quit")

    def do_EOF(self, line):
        "End Of Function"
        return True

    def do_quit(self, arg):
        "Quit function"
        return True

    def emptyline(self):
        "emptyline function"
        pass

    def do_create(self, args):
        "create a new instance"
        arg = args.split()
        if not arg:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        else:
            instance = HBNBCommand.classes[arg[0]]()
            print(instance.id)
            instance.save()

    def do_show(self, args):
        " Prints str representation of an instance "
        arg = args.split()
        if not arg:
            print("** class name missing **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            try:
                eval(arg[0])
                try:
                    string_split = arg[1].split('.')
                    sto = storage.all()
                    print(sto[f"{string_split[0]}.{string_split[1]}"])
                except KeyError:
                    print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")

    def do_destroy(self, args):
        " Deletes an instance based on the class name and id "
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        else:
            try:
                eval(arg[0])
                try:
                    del storage.all()[f"{arg[0]}.{arg[1]}"]
                    storage.save()
                except Exception:
                    print("** no instance found **")
            except Exception:
                print("** class doesn't exist")

    def do_all(self, args):
        " Prints all str representation of all instances "
        arg = args.split()
        if len(args) >= 1:
            try:
                eval(args)()
                print(storage.all())
            except Exception:
                print("** class doesn't exist **")
        else:
            print(storage.all())

    def do_update(self, args):
        """ Updates an instance based on the class name and id """
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg[0] in HBNBCommand.classesclasses:
            if len(arg) > 1:
                key = arg[0] + '.' + arg[1]
                if key in storage.all():
                    if len(arg) > 2:
                        if len(arg) > 3:
                            setattr(storage.all()[key], arg[2], arg[3])
                            storage.all()[key].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
