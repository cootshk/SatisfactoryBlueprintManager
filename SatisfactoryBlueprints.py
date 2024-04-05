"""Satisfactory Blueprint Parser, API, and more."""
from _Parser import Worker, BlueprintParser, Options
from Objects.Conveyors import is_conveyor
from _Classes import get_class

if __name__ == '__main__':
    import argparse
    import os
    parser = argparse.ArgumentParser(
        prog="Satisfactory Blueprint Info",
        description="Gets information about a satisfactory blueprint"
    )
    parser.add_argument("--file", "-f", default=None, required=False)
    parser.add_argument("--cli", "-c", action="store_true", required=False)
    args = parser.parse_args()
    if args.cli:
        print(f"Parsing {str(args.file)}!")
        assert os.path.isfile(args.file) and str(args.file).removesuffix("/").endswith(".sbp")
        p = BlueprintParser(Worker(), Options(args.file))
        print(p.objects)
    else:
        # GUI

        import tkinter as tk
        from tkinter.filedialog import askopenfilename
        window = tk.Tk()
        window.wm_title("SBM v1.0")
        greeting = tk.Label(text="Satisfactory Blueprint Manager")
        greeting.pack()
        #label = tk.Label(text="Blueprint File Path: ")
        submitbutton = tk.Button(
            text="Choose File",
            width=25,
            height=5,
            bg="blue",
            fg="yellow",
        )
        #label.pack()
        #submitbutton.pack()
        filetypes = (
            ('Satisfactory Blueprint Files', '*.sbp'),
            ('All files', '*.*'),
        )
        filename = askopenfilename(
            filetypes=filetypes,
            initialdir=os.path.expandvars(
                r'%LOCALAPPDATA%\FactoryGame\Saved\SaveGames\blueprints'
                ) if os.name == "nt" else None
            # C:\Users\___\AppData\Local\FactoryGame\Saved\SaveGames\blueprints\Atlass Factory
        )
        assert os.path.isfile(filename)

        p = BlueprintParser(Worker(), Options(filename, lang="en_us"))
        # Generate window to show blueprint contents
        #print(f"Blueprint data: \n{p.objects}")

        # Object Totals
        totals = {
            "conveyors": 0,
            "foundations": 0,
            "refiners": 0,
            "walls": 0,
            "storage": 0,
            "signs": 0,
            "extractors": 0,
        }

        for k,v in zip(p.objects.keys(), p.objects.values()):
            print({k: v})
            print()
            if is_conveyor({k:v}):
                totals["conveyors"] += 1

            get_class({k:v})
        print(f"Total conveyors: {totals['conveyors']}")

        # Run window
        window.mainloop()
