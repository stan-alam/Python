import os.path
import shutil

def augmented_move(target_folder, *filename, verbose=True, **specific):
    """move *.* into target_folder - to allow specific to particular files"""

    def print_verbose(message, filename):
        """print this when verbose is true"""
        if verbose:
            print(message.format(filename))

    for filename in filenames:
      target_path = os.path.join(target_folder, filename)
      if filename in specific:
          if specific[filename] == "disregard":
              print_verbose("disregarding {0}", filename)
          elif specific[filename] =="copy":
              print_verbose("copying file {0}", filename)
              shutil.copyfile(filename, target_path)
    else:
         print_verbose("moving {0}", filename)
         shutil.move(filename, target_path)
