import shutil
import os.path

def augmented_move(
  target_folder, *filenames, verbose=False, **specific):
  """move all filenames into the target_folder for specific treatment of certain files"""

def print_verbose(message, filename):
  """print the message only if verbose is enabled"""
  if verbose:
    print(message.format(filename))

for filename in filenames:
  target_path = os.path.join(target_folder, filename)
  if filename in specific:
   if specific[filename] == "ignore":
       print_verbose("Ignoring {0}", filename)
   elif specific[filename] == "copy":
     print_verbose("copying {0}", filename)
     shututil.copyfile(filename, target_path)

  else:
    print_verbose("moving {0}", filename)
    shutil.move(filename, target_path)
