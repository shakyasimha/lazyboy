import argparse 

def main():
    """
    Main driver function goes here
    """
    parser = argparse.ArgumentParser()
    # parser.add_argument("square", type=int, help="square two numbers")
    parser.add_argument("taskadd", help="Enter your task in the to-do list.")
    parser.add_argument("-v", "--verbose", action="store_true", choices=[0,1,2], help="increase output verbosity")
    # parser.add_argument("echo", help="echo the string you use in the command")
    # parser.add_argument("square", help="squares two numbers", type=int)
    args = parser.parse_args()
    # answer = args.square**2
    
    if args.verbose:
        print(f"You have added the task: {args.taskadd}")
    else:
        print(args.taskadd)
    
    
if __name__ == "__main__":
    main()